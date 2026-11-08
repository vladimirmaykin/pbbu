import tkinter as tk
from tkinter import ttk, filedialog
import requests
import threading
import time
import csv


class CryptoTrackerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Crypto Tracker")
        self.root.geometry("550x450")
        self.root.resizable(False, False)

        # Состояние сортировки для колонки цены
        self.price_sort_reverse = False
        # Словарь для хранения исходных данных (id_item: (name, ticker, price_float, change_float))
        self._tree_data = {}

        # Настройка стилей
        style = ttk.Style(root)
        style.theme_use('clam')
        style.configure("Treeview.Heading", font=("Arial", 11, "bold"))
        style.configure("Treeview", font=("Arial", 10), rowheight=25)

        # Заголовок
        title_label = tk.Label(root, text="Курсы криптовалют к USD", font=("Arial", 14, "bold"))
        title_label.pack(pady=10)

        # Панель инструментов
        toolbar_frame = tk.Frame(root)
        toolbar_frame.pack(padx=10, pady=(0, 5), fill=tk.X)

        # Кнопка ручного обновления
        self.refresh_button = ttk.Button(toolbar_frame, text="Обновить сейчас", command=self.update_data)
        self.refresh_button.pack(side=tk.LEFT, padx=(0, 5))

        # Кнопка экспорта в CSV
        self.export_button = ttk.Button(toolbar_frame, text="Экспорт в CSV", command=self._export_to_csv)
        self.export_button.pack(side=tk.LEFT)

        # Метка статуса
        self.status_label = tk.Label(toolbar_frame, text="Обновление...", font=("Arial", 9), fg="gray")
        self.status_label.pack(side=tk.RIGHT)

        # Область с таблицей и прокруткой
        frame = tk.Frame(root)
        frame.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)

        self.tree = ttk.Treeview(frame, columns=("Name", "Ticker", "Price", "24h"), show='headings', height=18)
        # ВАЖНО: к колонке Price привязываем команду сортировки
        self.tree.heading("Name", text="Название")
        self.tree.heading("Ticker", text="Тикер")
        self.tree.heading("Price", text="Цена (USD)", command=self._sort_by_price)
        self.tree.heading("24h", text="24h %")

        # Настройка выравнивания и ширины колонок
        self.tree.column("Name", width=200, anchor=tk.W)
        self.tree.column("Ticker", width=80, anchor=tk.CENTER)
        self.tree.column("Price", width=120, anchor=tk.E)
        self.tree.column("24h", width=100, anchor=tk.E)

        # Полоса прокрутки
        scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Список ID криптовалют на CoinGecko, которые мы хотим отслеживать
        self.coins = [
            'bitcoin', 'ethereum', 'tether', 'binancecoin', 'ripple',
            'solana', 'cardano', 'dogecoin', 'polkadot', 'tron'
        ]

        # Запускаем первый запрос и запускаем цикл автообновления
        self.update_data()
        self.root.after(60000, self.auto_update)

    def fetch_data(self):
        """Запрашивает данные у API CoinGecko в отдельном потоке."""
        try:
            # Используем endpoint /coins/markets для получения цен и процентов
            url = "https://api.coingecko.com/api/v3/coins/markets"
            params = {
                'vs_currency': 'usd',
                'ids': ','.join(self.coins),
                'order': 'market_cap_desc',
                'per_page': len(self.coins),
                'page': 1,
                'sparkline': 'false',
                'price_change_percentage': '24h'
            }

            # Устанавливаем таймаут, чтобы приложение не зависало при проблемах с сетью
            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            return {"error": str(e)}

    def update_data(self):
        """Метод теперь вызывается и по таймеру, и по нажатию кнопки."""
        # Блокируем кнопки на время запроса, чтобы избежать спама кликами
        self.refresh_button.config(state=tk.DISABLED)
        self.export_button.config(state=tk.DISABLED)
        self.status_label.config(text="Обновление...")
        self.root.update_idletasks()

        # Запрос в отдельном потоке, чтобы не блокировать GUI
        def worker():
            data = self.fetch_data()
            # Разблокируем кнопку после получения ответа
            self.root.after(0, self._populate_and_unlock, data)

        thread = threading.Thread(target=worker, daemon=True)
        thread.start()

    def _populate_and_unlock(self, data):
        """Вспомогательный метод для заполнения таблицы и разблокировки кнопок."""
        self.populate_table(data)
        self.refresh_button.config(state=tk.NORMAL)
        self.export_button.config(state=tk.NORMAL)

    def populate_table(self, data):
        """Заполняет Treeview полученными данными."""
        # Очищаем предыдущие записи
        self.tree.delete(*self.tree.get_children())
        self._tree_data.clear()

        if isinstance(data, dict) and data.get("error"):
            self.status_label.config(text=f"Ошибка API: {data['error']}", fg="red")
            return

        for coin in data:
            name = coin.get('name', 'N/A')
            ticker = coin.get('symbol', 'N/A').upper()
            price = coin.get('current_price', 0.0)
            change_24h = coin.get('price_change_percentage_24h', 0.0)

            # Форматирование цены
            price_str = f"${price:,.2f}".replace(",", " ")

            # Вставляем строку и сохраняем её ID
            item_id = self.tree.insert("", tk.END, values=(name, ticker, price_str, f"{change_24h:.2f}%"))

            # Сохраняем исходные числовые данные для сортировки
            self._tree_data[item_id] = (name, ticker, price, change_24h)

        # Настройка цветов для тегов (рост/падение)
        self.tree.tag_configure("up", foreground="#26a69a")
        self.tree.tag_configure("down", foreground="#ef5350")

        # Применяем теги для цвета процентов (требуется проход после вставки)
        for item_id in self.tree.get_children():
            change_val = self._tree_data[item_id][3]
            tag_name = "up" if change_val >= 0 else "down"
            self.tree.item(item_id, tags=(tag_name,))

        self.status_label.config(text=f"Последнее обновление: {time.strftime('%H:%M:%S')}", fg="black")

    def _sort_by_price(self):
        """Сортирует строки таблицы по числовому значению цены."""
        # Получаем список текущих ID строк
        data = [(item, self._tree_data[item][2]) for item in self.tree.get_children()]

        # Сортируем список кортежей по второму элементу (float цене)
        sorted_data = sorted(data, key=lambda x: x[1], reverse=self.price_sort_reverse)

        # Перемещаем элементы в Treeview согласно новому порядку
        for index, (item_id, _) in enumerate(sorted_data):
            self.tree.move(item_id, '', index)

        # Меняем направление для следующего клика
        self.price_sort_reverse = not self.price_sort_reverse

    def _export_to_csv(self):
        """Открывает диалог сохранения и записывает данные таблицы в файл."""
        # Открываем окно выбора файла. По умолчанию предлагаем имя с текущей датой
        file_path = filedialog.asksaveasfilename(
            defaultextension=".csv",
            filetypes=[("CSV files", "*.csv"), ("All files", "*.*")],
            initialfile=f"crypto_prices_{time.strftime('%Y-%m-%d_%H-%M')}.csv"
        )

        if not file_path:
            # Пользователь нажал "Отмена"
            return

        try:
            with open(file_path, mode='w', newline='', encoding='utf-8-sig') as csv_file:
                writer = csv.writer(csv_file, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)

                # Пишем заголовки
                headers = [self.tree.heading(col)["text"] for col in self.tree["columns"]]
                writer.writerow(headers)

                # Пишем данные строк
                for item_id in self.tree.get_children():
                    # Используем уже отформатированные строки из интерфейса
                    values = self.tree.item(item_id)["values"]
                    writer.writerow(values)

            self.status_label.config(text=f"Экспорт завершен: {file_path}", fg="green")
        except Exception as e:
            self.status_label.config(text=f"Ошибка записи CSV: {e}", fg="red")

    def auto_update(self):
        """Метод для периодического автоматического обновления."""
        self.update_data()
        self.root.after(60000, self.auto_update) # Повторяем через 60 секунд


def main():
    root = tk.Tk()
    app = CryptoTrackerApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
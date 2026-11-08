import tkinter as tk
from tkinter import ttk
import requests
import threading
import time


class CryptoTrackerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Crypto Tracker")
        self.root.geometry("550x450")
        self.root.resizable(False, False)

        # Настройка стилей для Treeview (таблицы)
        style = ttk.Style(root)
        # Используем встроенную тему для лучшей совместимости
        style.theme_use('clam')
        style.configure("Treeview.Heading", font=("Arial", 11, "bold"))
        style.configure("Treeview", font=("Arial", 10), rowheight=25)

        # Заголовок
        title_label = tk.Label(root, text="Курсы криптовалют к USD", font=("Arial", 14, "bold"))
        title_label.pack(pady=10)

        # Область с полосой прокрутки
        frame = tk.Frame(root)
        frame.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)

        self.tree = ttk.Treeview(frame, columns=("Name", "Ticker", "Price", "24h"), show='headings', height=18)
        self.tree.heading("Name", text="Название")
        self.tree.heading("Ticker", text="Тикер")
        self.tree.heading("Price", text="Цена (USD)")
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

        # Метка статуса
        self.status_label = tk.Label(root, text="Обновление...", font=("Arial", 9), fg="gray")
        self.status_label.pack(pady=5)

        # Список ID криптовалют на CoinGecko, которые мы хотим отслеживать
        self.coins = [
            'bitcoin', 'ethereum', 'tether', 'binancecoin', 'ripple',
            'solana', 'cardano', 'dogecoin', 'polkadot', 'tron'
        ]

        # Запускаем первый запрос и запускаем цикл автообновления
        self.update_data()
        self.root.after(60000, self.auto_update)  # 60000 мс = 60 секунд

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
            response.raise_for_status()  # Вызовет исключение для кодов ошибок 4xx и 5xx
            return response.json()
        except requests.exceptions.RequestException as e:
            return {"error": str(e)}

    def update_data(self):
        """Очищает таблицу и заполняет её новыми данными."""
        self.status_label.config(text="Обновление...")
        self.root.update_idletasks()

        # Запрос в отдельном потоке, чтобы не блокировать GUI
        def worker():
            data = self.fetch_data()
            self.root.after(0, self.populate_table, data)

        thread = threading.Thread(target=worker, daemon=True)
        thread.start()

    def populate_table(self, data):
        """Заполняет Treeview полученными данными."""
        # Очищаем предыдущие записи
        for row in self.tree.get_children():
            self.tree.delete(row)

        if isinstance(data, dict) and data.get("error"):
            self.status_label.config(text=f"Ошибка API: {data['error']}", fg="red")
            return

        for coin in data:
            name = coin.get('name', 'N/A')
            ticker = coin.get('symbol', 'N/A').upper()
            price = coin.get('current_price', 0.0)
            change_24h = coin.get('price_change_percentage_24h', 0.0)

            # Форматирование цены и процентов
            price_str = f"${price:,.2f}".replace(",", " ")
            change_color = "#26a69a" if change_24h >= 0 else "#ef5350"

            # Вставляем строку. Цвет меняется только для колонки с процентами через tag
            tag_name = "up" if change_24h >= 0 else "down"
            self.tree.insert("", tk.END, values=(name, ticker, price_str, f"{change_24h:.2f}%"), tags=(tag_name,))

        # Настройка цветов для тегов (рост/падение)
        self.tree.tag_configure("up", foreground="#26a69a")
        self.tree.tag_configure("down", foreground="#ef5350")

        self.status_label.config(text=f"Последнее обновление: {time.strftime('%H:%M:%S')}", fg="black")

    def auto_update(self):
        """Метод для периодического автоматического обновления."""
        self.update_data()
        self.root.after(60000, self.auto_update)  # Повторяем через 60 секунд


def main():
    root = tk.Tk()
    app = CryptoTrackerApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
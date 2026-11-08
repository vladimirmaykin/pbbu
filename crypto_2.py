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

        # Настройка стилей
        style = ttk.Style(root)
        style.theme_use('clam')
        style.configure("Treeview.Heading", font=("Arial", 11, "bold"))
        style.configure("Treeview", font=("Arial", 10), rowheight=25)

        # Заголовок
        title_label = tk.Label(root, text="Курсы криптовалют к USD", font=("Arial", 14, "bold"))
        title_label.pack(pady=10)

        # Панель инструментов для кнопки и статуса
        toolbar_frame = tk.Frame(root)
        toolbar_frame.pack(padx=10, pady=(0, 5), fill=tk.X)

        # Кнопка ручного обновления
        self.refresh_button = ttk.Button(toolbar_frame, text="Обновить сейчас", command=self.update_data)
        self.refresh_button.pack(side=tk.LEFT)

        # Метка статуса (перенесена в панель инструментов)
        self.status_label = tk.Label(toolbar_frame, text="Обновление...", font=("Arial", 9), fg="gray")
        self.status_label.pack(side=tk.RIGHT)

        # Область с таблицей и прокруткой
        frame = tk.Frame(root)
        frame.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)

        self.tree = ttk.Treeview(frame, columns=("Name", "Ticker", "Price", "24h"), show='headings', height=18)
        self.tree.heading("Name", text="Название")
        self.tree.heading("Ticker", text="Тикер")
        self.tree.heading("Price", text="Цена (USD)")
        self.tree.heading("24h", text="24h %")

        self.tree.column("Name", width=200, anchor=tk.W)
        self.tree.column("Ticker", width=80, anchor=tk.CENTER)
        self.tree.column("Price", width=120, anchor=tk.E)
        self.tree.column("24h", width=100, anchor=tk.E)

        scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Список ID криптовалют
        self.coins = [
            'bitcoin', 'ethereum', 'tether', 'binancecoin', 'ripple',
            'solana', 'cardano', 'dogecoin', 'polkadot', 'tron'
        ]

        # Запускаем первый запрос и цикл автообновления
        self.update_data()
        self.root.after(60000, self.auto_update)

    def fetch_data(self):
        try:
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
            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            return {"error": str(e)}

    def update_data(self):
        """Метод теперь вызывается и по таймеру, и по нажатию кнопки."""
        # Блокируем кнопку на время запроса, чтобы избежать спама кликами
        self.refresh_button.config(state=tk.DISABLED)
        self.status_label.config(text="Обновление...")
        self.root.update_idletasks()

        def worker():
            data = self.fetch_data()
            # Разблокируем кнопку после получения ответа
            self.root.after(0, self._populate_and_unlock, data)

        thread = threading.Thread(target=worker, daemon=True)
        thread.start()

    def _populate_and_unlock(self, data):
        """Вспомогательный метод для заполнения таблицы и разблокировки кнопки."""
        self.populate_table(data)
        self.refresh_button.config(state=tk.NORMAL)

    def populate_table(self, data):
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

            price_str = f"${price:,.2f}".replace(",", " ")
            change_color = "#26a69a" if change_24h >= 0 else "#ef5350"

            tag_name = "up" if change_24h >= 0 else "down"
            self.tree.insert("", tk.END, values=(name, ticker, price_str, f"{change_24h:.2f}%"), tags=(tag_name,))

        self.tree.tag_configure("up", foreground="#26a69a")
        self.tree.tag_configure("down", foreground="#ef5350")

        self.status_label.config(text=f"Последнее обновление: {time.strftime('%H:%M:%S')}", fg="black")

    def auto_update(self):
        self.update_data()
        self.root.after(60000, self.auto_update)


def main():
    root = tk.Tk()
    app = CryptoTrackerApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
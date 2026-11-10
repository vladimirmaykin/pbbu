from tkinter import *
from tkinter import messagebox as mb
from tkinter import ttk
import requests


def update_currency_label(event):
    code = target_combobox.get()
    name = tr_currencies[code]
    target_label.config(text=name)


def update_base_label(event):
    code = base_combobox.get()
    name = currencies[code]
    base_label.config(text=name)


def exchange():
    target_code = target_combobox.get().strip()
    base_code = base_combobox.get().strip()
    coins.clear()
    coins.append(base_code)
    if target_code and base_code:
        try:
            # Используем endpoint /coins/markets для получения цен
            url = "https://api.coingecko.com/api/v3/coins/markets"
            params = {
                'vs_currency': target_code,
                'ids': ','.join(coins),
                'order': 'market_cap_desc',
                'per_page': len(coins),
                'page': 1,
                'sparkline': 'false',
                'price_change_percentage': '24h'
            }
            # Устанавливаем таймаут, чтобы приложение не зависало при проблемах с сетью
            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()

            data = response.json()
            for coin in data:
                price = coin.get('current_price', 0.0)
                price_str = f"${price:,.2f}".replace(",", " ")
                mb.showinfo('Курс обмена',
                            f'Курс: {price_str} {target_code} за 1 {base_code}')
        except Exception as er:
             mb.showerror('Ошибка', f'{er}')
    else:
        mb.showwarning('Внимание', 'Введите код валюты')


currencies = {
    'bitcoin':'bitcoin',
    'ethereum':'ethereum',
    'tether':'tether',
    'binancecoin':'binancecoin',
    'ripple':'ripple',
    'solana':'solana',
    'cardano':'cardano',
    'dogecoin':'dogecoin',
    'polkadot':'polkadot',
    'tron':'tron'
}

tr_currencies = {
    'USD': 'Доллар США'
}

coins = []

root = Tk()
root.title('Курс обмена криптовалют к USD')
root.geometry('360x180')

Label(root, text='Криптовалюта').pack()
base_combobox = ttk.Combobox(root, values=list(currencies.keys()))
base_combobox.pack(pady=3, padx=10)
base_combobox.bind('<<ComboboxSelected>>', update_base_label)
base_label = ttk.Label()
base_label.pack()

Label(root, text='Целевая валюта' ).pack(padx=10)
target_combobox = ttk.Combobox(root, values=list(tr_currencies.keys()))
target_combobox.pack(pady=3, padx=10)
target_combobox.bind('<<ComboboxSelected>>', update_currency_label)
target_label = ttk.Label()
target_label.pack()

Button(text='Получить курс обмена к доллару',
       command=exchange).pack(pady=10, padx=10)

root.mainloop()

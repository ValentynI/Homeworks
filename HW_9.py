from bs4 import BeautifulSoup
import requests
a = int(input('Введіть кількість грн:'))
response = requests.get('https://minfin.com.ua/ua/currency/usd/')
if response.status_code == 200:
    soup = BeautifulSoup(response.text, features='html.parser')
    soup_list = soup.find_all('span', {'class': 'mfm-posr'})
    res = soup_list[-1]
    print(res.text)
    print( a / (float(input('Введіть курс'))))

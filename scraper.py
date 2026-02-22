import json
from datetime import datetime
import requests
from bs4 import BeautifulSoup

def get_bcv():
    try:
        url = "https://www.bcv.org.ve/"
        response = requests.get(url, verify=False)
        soup = BeautifulSoup(response.text, 'html.parser')
        dolar = soup.find(id="dolar").find('strong').text.strip().replace(',', '.')
        euro = soup.find(id="euro").find('strong').text.strip().replace(',', '.')
        return {"usd": dolar, "eur": euro}
    except:
        return {"usd": "0", "eur": "0"}

def main():
    precios = get_bcv()
    data = {
        "datetime": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
        "monedas": {
            "dolar_bcv": precios['usd'],
            "euro_bcv": precios['eur'],
            "binance_usdt": "Cargando..." 
        }
    }
    with open('data.json', 'w') as f:
        json.dump(data, f, indent=4)

if __name__ == "__main__":
    main()

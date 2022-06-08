import requests
import json


def get_data(amount):
    headers = {
        "apikey": "Ozi2nVyNFDjBNrlFEdCbML08ywqEsxJw"
    }

    to_usd = requests.request("GET",
                              f"https://api.apilayer.com/exchangerates_data/convert?to=USD&from=UAH&amount={amount}",
                              headers=headers)
    to_eur = requests.request("GET",
                              f"https://api.apilayer.com/exchangerates_data/convert?to=EUR&from=UAH&amount={amount}",
                              headers=headers)

    response_usd = json.loads(to_usd.text)
    response_eur = json.loads(to_eur.text)
    return response_usd['info']['timestamp'], response_usd['result'], response_eur['result']

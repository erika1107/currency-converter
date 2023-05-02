import requests

url = "https://currency-converter18.p.rapidapi.com/api/v1/convert"

from_currency = "USD"  # currency_1.get()
to_currency = "JPY"  # currency_2.get()
amount = "1"  # amount.get()
querystring = {"from": from_currency, "to": to_currency, "amount": amount}

headers = {
    "content-type": "application/octet-stream",
    "X-RapidAPI-Key": "5993f7ce6dmsh39e85effa93f4e9p1b4e25jsn8acfd458018b",
    "X-RapidAPI-Host": "currency-converter18.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)
response_data = response.json()
convert_amount = response_data['result']['convertedAmount']
print(convert_amount)

# Currency-converter

This microservice allows you to convert currencies by using currency converter API.

## Installation
1) Python
2) requests module (using 'pip install requests')

## Requesting data from the microservice
To convert a currency, you need to make a GET request to the microservice's API endpoint with these three variable.

1) from_currency : the currency you want to convert from (eg. USD). You can use get() function to get the data from your UI. (eg. currency_1.get())
2) to_currency: the currency you want to convert to. (eg. JPY). You can use get() function to get the data from your UI. (eg. currency_2.get())
3) amount: the amount of currency you want to convert. (eg. 100). You can use get() function to get the data from your UI. (eg. amount.get())

There is an example call:
```python
import requests

url = "https://currency-converter18.p.rapidapi.com/api/v1/convert"

from_currency = "USD"   # currency_1.get()
to_currency = "JPY"     # currency_2.get()
amount = "1"            # amount.get()
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

```

## Receiving data from the microservice


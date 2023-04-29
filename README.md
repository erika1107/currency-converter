# Currency-converter microservice communication contract

This microservice allows you to convert currencies by using currency converter API. It's written in Python and use currency converter API to send and receive data.

## Why the project useful
This project is useful for anyone who need to convert currencies for personal use or business use. 

## Installation
1) Python
2) requests module (you could use 'pip install requests')

## Requesting data from the microservice
To convert a currency, you need to make a GET request to the microservice's API endpoint with these three variables.

1) from_currency : the currency you want to convert from (eg. USD). You can use get() function to get the data from your UI. (eg. currency_1.get())
2) to_currency: the currency you want to convert to. (eg. JPY). You can use get() function to get the data from your UI. (eg. currency_2.get())
3) amount: the amount of currency you want to convert. (eg. 100). You can use get() function to get the data from your UI. (eg. amount.get())

There is an example call:
```python
import requests

def currency_convert():
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


```

## Receiving data from the microservice
The microservice will receive a JSON object which includes:
1) "result" : an object contains currencies and converted amount
2) "success" : a boolean whether the conversion is succussful.

Example:
```
{
    "result": {
        "from": "USD",
        "to": "JPY",
        "amount": 1,
        "convertedAmount": 134.02
    },
    "success": true
}
```
I use "json()" method to convert JSON object in Python, and get the convertedAmount from the JSON object. 
```
response_data = response.json()
convert_amount = response_data['result']['convertedAmount']
```
### Running the microservice
1) copy the whole currency_convert() function, and paste it to your main .py file.
2) modify the three variables: from_currency, to_currency, amount.
3) call the currency_convert() function from the UI - converter button, then the converted amount will be displayed to users.

## UML sequence diagram
![image](https://user-images.githubusercontent.com/78334822/235056428-f105400a-e4c9-46ef-925d-bb8f24f62d29.png)




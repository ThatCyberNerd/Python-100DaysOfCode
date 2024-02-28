import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = "YOUR OWN API"
NEWS_API_KEY = "YOUR OWN API"

TWILIO_SID = "YOUR OWN SID"
TWILIO_AUTH_TOKEN = "YOUR OWN TOKEN"

parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY,
}

response = requests.get(STOCK_ENDPOINT, params=parameters)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key,value) in data.items()]

yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]

day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]

difference = abs(float(day_before_yesterday_closing_price) - float(yesterday_closing_price))

diff_percent = (difference / float(yesterday_closing_price)) * 100

if diff_percent > 1:

    news_parameters = {
        "apiKey" : NEWS_API_KEY,
        "qInTitle" : COMPANY_NAME
    }
    news_response = requests.get(NEWS_ENDPOINT, params=news_parameters)
    articles = news_response.json()["articles"]
    three_articles = articles[:3]

    formatted_articles = [f"Headline : {article['title']}. \nBrief : {article['description']}" for article in three_articles]

    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    for article in formatted_articles:
        message = client.messages.create(
            body=article,
            from_="YOUR TWILIO VIRTUAL NUMBER",
            to="YOUR PHONE NUMBER"
        )

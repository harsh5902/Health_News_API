import requests
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

API_KEY = YOUR NEWS API KEY
account_sid = YOUR TWILIO ACCOUNT SID
auth_token = YOUR TWILIO AUTH TOKEN

twilio_mo_no = YOUR TWILIO MOBILE NUM

response = requests.get(url=f"https://newsapi.org/v2/top-headlines?country=in&category=health&apiKey={API_KEY}")
response.raise_for_status()
health_data = response.json()
#pprint.pprint(health_data)

for x in range(5):
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}
    client = Client(account_sid, auth_token, http_client=proxy_client)
    news = health_data["articles"][x]
    title = news['title']
    description = news['description']
    url = news["url"]
    messages = client.messages.create(
        body=f"\n\n{title}\n\n\n{description}\n\n{url}",
        from_=twilio_mo_no,
        to= YOUR MOBILE NUMBER
    )
    # print(title)
    # print(description)
    # print(url)

import requests
from bs4 import BeautifulSoup
token = "744913071:AAGxQNMyveBkJx5zbk5ufxVP4_F5cq-4K-w"
method_name = "getUpdates"
url = "https://api.telegram.org/bot{0}/{1}".format(token,method_name)
update = requests.get(url).json()
user_id = update["result"][0]["message"]["from"]["id"]
method_name = "sendmessage"
url1 = "https://finance.naver.com/sise/"
html1 = requests.get(url1).text
bs = BeautifulSoup(html1,'html.parser')
select = bs.select_one("#KOSPI_now")
msg = select.text
msg_url = "https://api.telegram.org/bot{0}/{1}?chat_id={2}&text={3}".format(token,method_name,user_id,msg)
print(msg)
print(requests.get(msg_url))
import requests
from datetime import datetime


def send_msg(**kwargs):
    token = "7135471388:AAFvEHqlJ8jHEUxRzWvjLaffYLVcbdcIE8g"  # bot token

    user_id = "5584238217"  # user id
    url_req = ("https://api.telegram.org/bot" + token + "/sendMessage" + "?chat_id=" +
               user_id +
               "&text=" +
               f"{datetime.now().strftime(f'<b>%d/%m/%y  %H : %M : %S {kwargs}</b>')}&parse_mode=HTML")
    response = requests.get(url_req)
    print(response.json())
2
import time
import os
import requests
from twilio.rest import Client
from dotenv import load_dotenv

import telegram


def get_status(user_id):
    vk_token = os.getenv('VK_TOKEN')
    vk_api = 'https://api.vk.com/method/'
    vk_metod = 'users.get'
    params = {
        "user_ids": user_id,
        "access_token": vk_token,
        "fields": "online",
        "v": "5.122"
    }
    user_staus = requests.post(f'{ vk_api }{ vk_metod }', params=params).json()
    result = user_staus['response'][0]['online']
    return result


def sms_sender(sms_text):
    to = os.getenv("NUMBER_TO")
    from_ = os.getenv("NUMBER_FROM")
    client = Client()
    sid = client.messages.create(to=to, from_=from_, body=sms_text)
    return sid.sid


if __name__ == "__main__":
    load_dotenv()
    vk_id = input("Введите id ")
    while True:
        if get_status(vk_id) == 1:
            sms_sender(f'{vk_id} сейчас онлайн!')
            break
        time.sleep(5)

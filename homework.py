import os
import time

import requests
from twilio.rest import Client

access_token = os.getenv('VK_token')
version = 5.92
url = 'https://api.vk.com/'
constants = {
    'account_sid': os.getenv('account_sid'),
    'auth_token': os.getenv('auth_token')
}
from_ = os.getenv('NUMBER_FROM')
to = os.getenv('NUMBER_TO')


def get_status(user_id):
    params = {
        'access_token': access_token,
        'v': version,
        'user_ids': user_id,
        'fields': 'online',
    }
    user_status = requests.post(
        f'{url}method/users.get', params=params)
    return user_status.json()['response'][0]['online']


def call_client():
    client = Client(constants)
    return(client)


def sms_sender(sms_text):
    client = call_client()
    message = client.messages.create(
        body=sms_text,
        from_=from_,
        to=to
    )
    return(message.sid)


if __name__ == '__main__':
    vk_id = input('Введите id ')
    while True:
        if get_status(vk_id) == 1:
            sms_sender(f'{vk_id} сейчас онлайн!')
            break
        time.sleep(5)

import os
import time

import requests
from twilio.rest import Client

access_token = os.getenv('VK_token')
version = 5.92
url = 'https://api.vk.com/method/'


def get_status(user_id):
    params = {
        'access_token': access_token,
        'v': version,
        'user_ids': user_id,
        'fields': 'online',
    }
    user_status = requests.post(
        f'{url}users.get', params=params)
    return user_status.json()['response'][0]['online']


class SendSms:
    def __init__(self):
        self.account_sid = os.getenv('account_sid')
        self.auth_token = os.getenv('auth_token')
        self.client = Client(self.account_sid, self.auth_token)
        self.body = self.sms_text,
        self.from_ = os.getenv('NUMBER_FROM')
        self.to = os.getenv('NUMBER_TO')

    def sms_sender(self, sms_text):
        self.message = self.client.messages.create(
            body=self.body,
            from_=self.from_,
            to=self.to
        )
        return(self.message.sid)


if __name__ == '__main__':
    vk_id = input('Введите id ')
    while True:
        if get_status(vk_id) == 1:
            SendSms.sms_sender(f'{vk_id} сейчас онлайн!')
            break
        time.sleep(5)

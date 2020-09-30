# -*- coding: utf-8 -*-
from datetime import datetime
import datetime
import requests

from core import app

print('Start app')


@app.route('/')
def main():
    url = 'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json'

    try:
        response = requests.get(url)
    except:
        raise Exception

    def check(resp):
        if resp.headers['Content-Type'] == 'application/json; charset=utf-8' and resp.status_code == 200:
            date = datetime.date.today()
            result = ''
            result += f'Дата создания запроса:  ' + date.strftime('%d/%m/%Y\n') + '\n'
            json_resp = resp.json()
            for index, key in enumerate(json_resp):
                result += f'{index + 1}. {key["txt"]} to UAH: {key["rate"]}\n'
            return result
        else:
            raise Exception

    return check(response)

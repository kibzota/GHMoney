from __future__ import absolute_import
from celery import task
from core.models import Currency, Stocks, Bitcoin
from django.conf import settings
import requests



def get_hg_data():
    response = requests.get("https://api.hgbrasil.com/finance?key={0}".format(settings.HG_KEY))
    return response.json() if response.status_code == 200 else None

@task()
def save_hg_data():
    hg_data = get_hg_data()
    if hg_data:
        currency = Currency()
        currency.save_currency_from_hg_api(hg_data)


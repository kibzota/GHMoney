import datetime

from django.db import models
# Create your models here.


class Currency(models.Model):
    dt_create = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=100, null=True)
    buy = models.DecimalField(max_digits=18, decimal_places=4, null=True)
    sell = models.DecimalField(max_digits=18, decimal_places=4, null=True)
    variation = models.FloatField(null=True)

    def save_currency_from_hg_api(self, hg_data):

        for val in hg_data["results"]["currencies"].keys():
            if val != "source":
                currency = Currency()
                currency.name = hg_data["results"]["currencies"][val]['name']
                currency.buy = hg_data["results"]["currencies"][val]['buy']
                currency.sell = hg_data["results"]["currencies"][val]['sell']
                currency.variation = hg_data["results"]["currencies"][val]['variation']
                currency.save()




class Bitcoin(models.Model):
    dt_create = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=100, null=True)
    format = models.CharField(max_length=100, null=True)
    last = models.DecimalField(max_digits=18, decimal_places=4, null=True)
    buy = models.DecimalField(max_digits=18, decimal_places=4, null=True)
    sell = models.DecimalField(max_digits=18, decimal_places=4, null=True)
    variation = models.FloatField(null=True)


class Stocks(models.Model):
    dt_create = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=100, null=True)
    location = models.CharField(max_length=100, null=True)
    points = models.DecimalField(max_digits=18, decimal_places=4, null=True)
    variation = models.FloatField(null=True)


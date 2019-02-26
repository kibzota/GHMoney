from django.db import models
# Create your models here.


class Currency(models.Model):
    dt_create = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=100)
    buy = models.DecimalField(max_digits=18, decimal_places=4)
    sell = models.DecimalField(max_digits=18, decimal_places=4)
    variation = models.FloatField()

    def save_currency_from_hg_api(self, hg_data):

        for val in hg_data["results"]["currencies"].keys():
            if val != "source":
                self.name = hg_data["results"]["currencies"][val]['name']
                self.buy = hg_data["results"]["currencies"][val]['buy']
                self.sell = hg_data["results"]["currencies"][val]['sell']
                self.variation = hg_data["results"]["currencies"][val]['variation']
                self.save()


class Bitcoin(models.Model):
    dt_create = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=100)
    format = models.CharField(max_length=100)
    last = models.DecimalField(max_digits=18, decimal_places=4)
    buy = models.DecimalField(max_digits=18, decimal_places=4)
    sell = models.DecimalField(max_digits=18, decimal_places=4)
    variation = models.FloatField()


class Stocks(models.Model):
    dt_create = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    points = models.DecimalField(max_digits=18, decimal_places=4)
    variation = models.FloatField()


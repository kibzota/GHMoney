from djongo import models
# Create your models here.


class Currency(models.Model):
    name = models.CharField(max_length=100)
    buy = models.DecimalField(max_digits=18, decimal_places=4)
    sell = models.DecimalField(max_digits=18, decimal_places=4)
    variation = models.FloatField()


class Bitcoin(models.Model):
    name = models.CharField(max_length=100)
    format = models.CharField(max_length=100)
    last = models.DecimalField(max_digits=18, decimal_places=4)
    buy = models.DecimalField(max_digits=18, decimal_places=4)
    sell = models.DecimalField(max_digits=18, decimal_places=4)
    variation = models.FloatField()


class Stocks(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    points = models.DecimalField(max_digits=18, decimal_places=4)
    variation = models.FloatField()


class Entry(models.Model):
    dt_create = models.DateTimeField(auto_now=True)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    stock = models.ForeignKey(Stocks, on_delete=models.CASCADE)
    bitcoin = models.ForeignKey(Bitcoin, on_delete=models.CASCADE)

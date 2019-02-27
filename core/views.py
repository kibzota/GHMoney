import datetime

from django.shortcuts import render
from core.models import Currency

def index(request):
    context = {}
    dolar_data = Currency.objects.all().filter(name='Dollar').order_by('dt_create')
    bitcoin_data = Currency.objects.all().filter(name='Bitcoin').order_by('dt_create')
    euro_data = Currency.objects.all().filter(name='Euro').order_by('dt_create')

    context["dolar_values"] = ["Dolar"]
    context["dolar_values"].extend([x.buy.__float__() for x in dolar_data])
    context["dolar_date"] = [x.dt_create.strftime("%d-%m-%Y %H:%m") for x in dolar_data]

    context["bitcoin_values"] = ["Bitcoin"]
    context["bitcoin_values"].extend([y.buy.__float__() for y in bitcoin_data])
    context["bitcoin_date"] = [y.dt_create.strftime("%d-%m-%Y %H:%m") for y in bitcoin_data]

    context["euro_values"] = ["Euro"]
    context["euro_values"].extend([z.buy.__float__() for z in euro_data])
    context["euro_date"] = [y.dt_create.strftime("%d-%m-%Y %H:%m") for y in bitcoin_data]
    context["euro_variation"] = euro_data.filter()

    context["dolar_yesterday_variation"] = retroative_variation(days_before=1, currency_name="Dollar")
    context["dolar_last_week_variation"] = retroative_variation(days_before=7, currency_name="Dollar")
    context["dolar_last_month_variation"] = retroative_variation(days_before=30, currency_name="Dollar")

    context["bitcoin_yesterday_variation"] = retroative_variation(days_before=1, currency_name="Bitcoin")
    context["bitcoin_last_week_variation"] = retroative_variation(days_before=7, currency_name="Bitcoin")
    context["bitcoin_last_month_variation"] = retroative_variation(days_before=30, currency_name="Bitcoin")

    context["euro_yesterday_variation"] = retroative_variation(days_before=1, currency_name="Euro")
    context["euro_last_week_variation"] = retroative_variation(days_before=7, currency_name="Euro")
    context["euro_last_month_variation"] = retroative_variation(days_before=30, currency_name="Euro")
    return render(request,'home/index.html',context)


def retroative_variation(days_before, currency_name):
    retroactive_date = datetime.datetime.now() - datetime.timedelta(days=days_before)
    result = Currency.objects.filter(
        dt_create__lte=retroactive_date).filter(name=currency_name).order_by('-dt_create')
    if result:
        return '{0:.2%}'.format(result.first().variation)
    else:
        return '-'

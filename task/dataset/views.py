import datetime
import csv
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Sum, FloatField, F, ExpressionWrapper
from .models import Dataset


# to read from CSV file
def load_data(request):
    with open('dataset.csv', 'r') as csvFile:
        reader = csv.reader(csvFile)
        next(reader, None)
        for csv_data in reader:
            _, created = Dataset.objects.get_or_create(
                date=csv_data[0],
                channel=csv_data[1],
                country=csv_data[2],
                os=csv_data[3],
                impressions=csv_data[4],
                clicks=csv_data[5],
                installs=csv_data[6],
                spend=csv_data[7],
                revenue=csv_data[8],
            )
        return HttpResponse('Data Successfully Stored in DB!')


# client API to provide result dataset
@csrf_exempt
def data(request):
    request_type = request.GET['attrs']
    if request_type == 'impressions':
        dataset = Dataset.objects.filter(date__lte=datetime.date(2017, 6, 1))\
            .values('channel', 'country')\
            .annotate(impressions=Sum('impressions'), clicks=Sum('clicks'))\
            .order_by('-clicks').all()

    elif request_type == 'installs':
        first_date = datetime.date(2017, 5, 1)
        last_date = datetime.date(2017, 5, 31)
        dataset = Dataset.objects.filter(date__range=(first_date, last_date), os__iexact='ios')\
            .values('date').annotate(installs=Sum('installs')).order_by('clicks').all()

    elif request_type == 'revenue':
        dataset = Dataset.objects.filter(date__startswith=datetime.date(2017, 6, 1), country__iexact='US')\
            .values('os').annotate(revenue=Sum('revenue')).order_by('-revenue').all()

    elif request_type == 'cpi':
        dataset = Dataset.objects.values('channel')\
            .annotate(cpi=ExpressionWrapper(Sum(F('spend')) / Sum(F('installs')), output_field=FloatField()),
                      spend=Sum('spend'))\
            .order_by('-cpi').all()
    else:
        dataset = 'Invalid Parameters. Please give Valid Parameters!'

    return HttpResponse(dataset)

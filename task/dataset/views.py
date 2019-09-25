import csv
from django.http import JsonResponse
from .models import Dataset


# Create your views here.
def index(request):
    with open('dataset.csv', 'r') as csvFile:
        reader = csv.reader(csvFile)
        next(reader, None)
        for data in reader:
            _, created = Dataset.objects.get_or_create(
                date=data[0],
                channel=data[1],
                country=data[2],
                os=data[3],
                impressions=data[4],
                clicks=data[5],
                installs=data[6],
                spend=data[7],
                revenue=data[8],
            )
    data = {'name':'m'}
    return JsonResponse(data)

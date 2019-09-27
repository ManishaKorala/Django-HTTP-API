from django.views.decorators.csrf import csrf_exempt
from .service import DatasetService
from django.http import HttpResponse


# landing page
def index(request):
    return HttpResponse('Welcome to Manisha Adjust Task')


# to load CSV data from file
def load_data(request):
    filename = 'dataset.csv'
    DatasetService.read_csv_data(filename)
    return HttpResponse('Data Successfully Stored in DB!')


# client API to provide result dataset
@csrf_exempt
def data(request):
    request_type = request.GET['attrs']
    result = DatasetService.evaluate_result(request_type)
    return HttpResponse(result)

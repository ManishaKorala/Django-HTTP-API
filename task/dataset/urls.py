from django.urls import path

from . import views

# URL endpoints
urlpatterns = [
    path('', views.index, name='index'),
    path('get_data', views.data, name='data'),
    path('load_data/', views.load_data, name='load_data')
]

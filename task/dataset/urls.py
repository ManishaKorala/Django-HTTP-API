from django.urls import path

from . import views

# URL endpoints
urlpatterns = [
    path('get_data', views.data, name='data'),
    path('load_data/', views.load_data, name='load_data')
]

from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('/<id>', views.details, name="details" ),
    path('/update/<id>', views.quantity, name='quantity')
    
]
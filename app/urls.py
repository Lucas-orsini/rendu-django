from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('/create', views.create, name='create'),
    path('/<id>', views.details ),
    path('/<id>/update', views.update ),
    path('/<id>/delete', views.delete ),
]
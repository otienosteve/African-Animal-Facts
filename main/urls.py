from django.urls import path
from . import views

urlpatterns=[
path('rand/',views.home),
path('all/',views.all),
path('update/',views.update)
]

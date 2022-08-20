from django.urls import path
from . import views

urlpatterns = [
    path('',views.getData),
    path('api/register/<str:email>/<str:password>',views.register)
]

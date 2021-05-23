from django.urls import path
from . import views

urlpatterns=[
        path("",views.self,name="selg_introduce")
        ]


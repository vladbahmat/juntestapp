from . import views
from django.urls import path

app_name="operations"

urlpatterns=[
    path('',views.homepage,name="homepage"),
    path('getData/',views.getData,name="getData"),
    path('getData/showResult/',views.showResult,name="showResult")
]
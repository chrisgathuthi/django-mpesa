from django.urls import path
from .views import  ExpressNumber


urlpatterns = [
    path("",ExpressNumber.as_view(),name="phone"),
]
from django.urls import path
from .views import  ExpressNumber, MpesaExpressCallBack, ValidationView


urlpatterns = [
    path("",ExpressNumber.as_view(),name="phone"),
    path("express",ExpressNumber.as_view(),name="phone"),
    path("stk-callback/", MpesaExpressCallBack.as_view(),name="express-callback"),
    path("validation-callback/", ValidationView.as_view(),name="validation-callback"),
]
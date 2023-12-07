from django.urls import path
from . import views

urlpatterns = [

    path('', views.PaymentData),
    path('<str:pk>', views.PatientSetting),
    path('delete/<str:pk>', views.PatientSetting),
    path('update/<str:pk>', views.PatientSetting),
    
]

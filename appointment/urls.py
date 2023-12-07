from django.urls import path
from . import views

urlpatterns = [

    path('', views.AppointmentData),
    path('<str:pk>', views.AppointmentSetting),
    path('delete/<str:pk>', views.AppointmentSetting),
    path('update/<str:pk>', views.AppointmentSetting),
    
]

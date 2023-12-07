from django.urls import path
from . import views

urlpatterns = [

    path('', views.ClinicInfoData),
    path('<str:pk>', views.ClinicInfoSetting),
    path('update/<str:pk>', views.ClinicInfoSetting),
    path('public/', views.PublicClinicData),
    
]

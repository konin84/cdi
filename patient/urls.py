from django.urls import path
from . import views

urlpatterns = [

    path('', views.PatientData),
    path('get/<str:pk>', views.PatientSetting),
    path('delete/<str:pk>', views.PatientSetting),
    path('update/<str:pk>', views.PatientSetting),

    path('view/message', views.MessageData),
    path('view/message/<str:pk>', views.MessageSetting),
    path('view/message/update/<str:pk>', views.MessageSetting),

    
]

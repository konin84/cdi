from django.urls import path
from . import views

urlpatterns = [

 
    path('', views.TreatmentData),
    path('<str:pk>', views.TreatmentSetting),
    path('updatestatus/<str:pk>', views.UpdateTreatmentStatus),
    path('updatepaymentstatus/<str:pk>', views.UpdateTreatmentPaymentStatus),
   
    path('intervention/', views.InterventionData),
    path('interventions/', views.PublicInterventionData),
    path('intervention/<str:pk>', views.InterventionSetting),
    path('intervention/update/<str:pk>', views.InterventionSetting),
    path('intervention/delete/<str:pk>', views.InterventionSetting),
    # path('company/logo/update/<str:pk>', views.companyLogoSetting),

]

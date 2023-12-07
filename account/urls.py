from django.urls import path
from . import views

urlpatterns = [
    
  path('listUsers', views.allUsers),
  path('adminSignup', views.SignUpAdministrator.as_view()),#Working with Admins
  path('doctorSignup', views.SignUpDoctor.as_view()),#Sign up with Doctors
  path('patientSignup', views.SignUpPatient.as_view()),#Sign up with patients
  path('cashierSignup', views.SignUpCashier.as_view()),#Sign up with Cashier
  path('accountantSignup', views.SignUpAccountant.as_view()),#Sign up with accountants

  path('accountant', views.allAccountants),#Working with accountants
  path('accountant/<str:pk>', views.accountant),
  path('admin', views.allAdmins),#Working with Admins
  path('admin/<str:pk>', views.admin),
  path('doctor', views.allDoctors),#Working with Doctors
  path('doctor/<str:pk>', views.doctor),
  path('patient', views.allPatients),#Working with patients
  path('patient/<str:pk>', views.patient), 
  path('cashier', views.allCashiers),#working with cashiers
  path('cashier/<str:pk>', views.cashier),


]
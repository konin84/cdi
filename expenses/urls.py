from django.urls import path
from . import views

urlpatterns = [

    path('',views.ExpenseData),
    path('<str:pk>',views.ExpenseSetting),
    path('update/<str:pk>',views.ExpenseSetting),

    path('get/types',views.ExpenseTypeData),
    path('get/type/<str:pk>',views.ExpenseTypeSetting),
    path('get/type/update/<str:pk>',views.ExpenseTypeSetting),

]

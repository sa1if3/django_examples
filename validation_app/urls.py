from django.urls import path
from validation_app import views

urlpatterns = [
    path('add_new_company/',views.add_new_company, name = "add_new_company"),
    path('',views.home, name = "home"),
]
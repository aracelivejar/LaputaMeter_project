from django.urls import path
from . import views

urlpatterns = [
    path('laptm_app/', views.laptm_app, name='laptm_app'),

]

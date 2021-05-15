from . import views
from django.urls import path


urlpatterns = [
    path('transaction/', views.transaction, name='transaction'),
    path('history/', views.history, name='history'),
    path('', views.home, name='home'),
    path('donate/', views.donate, name='donate'),
    path('contact/', views.contact, name='contact'),
    path('customer/', views.customer, name='customer'),
    path('form/<str:slug>/', views.form, name='form'),
]

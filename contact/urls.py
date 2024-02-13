from django.urls import path
from . import views

urlpatterns = [
    path('', views.ContactFormSubmitView.as_view(), name='contactform')
]
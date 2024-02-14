from django.urls import path
from . import views

urlpatterns = [
    path('', views.ContactFormSubmitView.as_view(), name='contactform'),
    path('form-submissions/', views.ContactView.as_view(), name='contact-submissions'),
]
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.contrib import messages
from django.urls import reverse_lazy
from .models import Contact
from .forms import ContactForm


class ContactFormSubmitView(CreateView):
    """
    CreateView to submit a new contact form submission.
    This allows users to submit general queries, complaints or 
    return queries
    """
    model = Contact
    template_name = 'contact/contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        messages.success(self.request, 'Successfully added your Query!')
        return super().form_valid(form)


class ContactView(ListView):
    """
    ListView to allow the admin user to view
    the contact form submissions on the front end
    """
    model = Contact
    queryset = Contact.objects.order_by('-created_on')
    template_name = 'contact/contact_submissions.html'
    context_object_name = 'contact_list'

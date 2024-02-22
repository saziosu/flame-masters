from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views import View
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.contrib import messages
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
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
    # redirect the user to the contact-success page
    success_url = reverse_lazy('contact-success')

    def form_valid(self, form):
        messages.success(self.request, 'Successfully added your Query!')
        return super().form_valid(form)


def contact_success(request):
    """
    A view for redirecting the user to a thank you page
    after submitting a query on the contact form
    """
    return render(request, 'contact/contact_success.html')


class ContactView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    """
    ListView to allow the admin user to view
    the contact form submissions on the front end
    """

    model = Contact
    queryset = Contact.objects.order_by('-created_on')
    template_name = 'contact/contact_submissions.html'
    context_object_name = 'contact_list'

    def test_func(self):
        """
        Method to only allow superuser access to the view
        https://docs.djangoproject.com/en/5.0/topics/auth/default/#django.contrib.auth.mixins.UserPassesTestMixin
        """
        if self.request.user.is_superuser:
            return True
        return False

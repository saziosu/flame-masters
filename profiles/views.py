from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from .forms import UserProfileForm
from checkout.models import Order


@login_required
def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            # toast message that the profile is successfully updated
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(
                request,
                'Failed to update profile. Please ensure the form is valid.')
    else:
        form = UserProfileForm(instance=profile)
    # render the orders
    orders = profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
    }

    return render(request, template, context)


def order_history(request, order_number):
    """
    A view for the user to view their order history
    """
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'Order: {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)

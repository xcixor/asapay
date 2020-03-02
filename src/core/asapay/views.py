from django.shortcuts import render
from .models import get_users, get_users_total

# Create your views here.

def dashboard(request):
    """renders the dashboard

    Arguments:
        request {object} -- django request object

    Returns:
        HttpResponse -- returns http response rendering the page
    """
    context = {
        'users': get_users,
        'total_users': get_users_total
    }
    return render(request, 'dashboard/dashboard.html', context)
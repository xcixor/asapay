from django.shortcuts import render
from .models import (
    get_users, get_users_total, get_airtime_purchases,
    get_kplc_purchases, get_airtime_purchases_total, get_kplc_purchases_total
    )

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
        'total_users': get_users_total,
        'airtime_purchases': get_airtime_purchases,
        'kplc_purchases': get_kplc_purchases,
        'total_airtime_purchases': get_airtime_purchases_total,
        'total_kplc_purchases': get_kplc_purchases_total
    }
    return render(request, 'dashboard/dashboard.html', context)
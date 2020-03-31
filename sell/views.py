from django.shortcuts import render
from .models import Customer, Trip, Policy, Term

def home(request):
    trip = Trip.objects.all()
    print(trip[0].trip_link)
    customers = Customer.objects.all()
    return render(request, 'home.html', {'customers': customers, 'trip':trip[0].trip_link, 'title': 'Product Surveys'})


def policy(request):
    policys = Policy.objects.all()
    return render(request, 'policy.html', {'policy': policys[0].content, 'title': 'Policy'})
def terms(request):
    term = Term.objects.all()
    return render(request, 'terms.html', {'term': term[0].content, 'title': 'Terms'})
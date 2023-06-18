from django.shortcuts import render

# Create your views here.

def base_view(request):
    return render(request , 'base.html')

def agent_page_view(request):
    return render(request, 'profileDetail.html')

def home(request):
    return render(request, 'index.html')

def product_detail_view (request):
    return render(request, 'Productdetial.html')

def add_listing_view (request):
    return render(request, 'AddListing.html')
def login_view (request):
    return render(request, 'loginPage.html')

def registration_view (request):
    return render(request, 'Registraion.html')

def agent_view (request):
    return render(request, 'listing/agent.html')
def buy_view (request):
    return render(request, 'listing/buy.html')

def expert_view (request):
    return render(request, 'listing/Expert.html')
def rent_view (request):
    return render(request, 'listing/rent.html')
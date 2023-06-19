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

def base_dashboard_view (request):
    
    return render(request, 'dashboard/base.html',{ 'class': 'active'})

def dashboard_view (request):
    return render(request, 'dashboard/Dashboard.html')

def dashboard_message_view (request):
    return render(request, 'dashboard/message.html')

def dashboard_profile_view (request):
    return render(request, 'dashboard/profile.html')

def dashboard_propertyListing_view (request):
    return render(request, 'dashboard/PropertyListing.html')

def dashboard_wishlist_view (request):
    return render(request, 'dashboard/Wishlist.html')

def dashboard_addListing_view (request):
    return render(request, 'dashboard/AddListing.html')
from django.contrib.auth import authenticate, login , logout
from django.shortcuts import render,redirect,HttpResponse , get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .filters import ProductPropertyModelFiler
from .models import *
from listing import models as mod
from listing.EmailBackEnd import EmailBackEnd
import random
# Create your views here.

def base_view(request):
    return render(request , 'base.html')

def agent_page_view(request , user_id):
    agentProfile = get_object_or_404(Agent , pk = user_id)
    agentRate = AgentRate.objects.filter(agent = user_id)
    viewNumber = agentRate.count()
    now = datetime.now()
    starCount = 0
    for i in agentRate:
        starCount += i.rate
    if starCount != 0:
        starCount = starCount // viewNumber
    starNullCount = 5 - starCount
    starNullCount = range(0 , starNullCount)
    starCount = range(0,starCount)
    context = {
        'agentProfile':agentProfile,
        'now':now,
        'agentRate':agentRate,
        'starCount':starCount,
        'starNullCount':starNullCount,
        'viewNumber':viewNumber

    }
    return render(request, 'profileDetail.html',context)

def expert_page_view(request , user_id):
    expertProfile = get_object_or_404(Expert , pk = user_id)
    context ={
        'expertProfile' : expertProfile
    }
    return render(request, 'ExpertProfile.html' , context)

def home(request):
    experts = Expert.objects.all()[:6]
    agents = Agent.objects.all()[:4]
    product_detail = ProductPropertyModel.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(product_detail, 3)
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    context = {
        'experts':experts,
        'agents':agents,
        'products':products
    }
    return render(request, 'index.html' , context)

def product_detail_view (request):
    return render(request, 'Productdetial.html')

def login_view (request):
    return render(request, 'loginPage.html')

def registration_view (request):
    return render(request, 'Registraion.html')

def agent_view (request):
    agent = Agent.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(agent, 4)
    try:
        agents = paginator.page(page)
    except PageNotAnInteger:
        agents = paginator.page(1)
    except EmptyPage:
        agents = paginator.page(paginator.num_pages)
    context = {
        'agents': agents
    }
    return render(request, 'listing/agent.html' , context)
def buy_view (request):
    productlist  = ProductPropertyModel.objects.filter(status = 'For Sale')
    filters = ProductPropertyModelFiler(request.GET , queryset = productlist)
    page = request.GET.get('page', 1)

    paginator = Paginator(filters.qs, 6)
    try:
        productlists = paginator.page(page)
    except PageNotAnInteger:
        productlists = paginator.page(1)
    except EmptyPage:
        productlists = paginator.page(paginator.num_pages)
    context = {
        "productlists": productlists,
        "filters" : filters
    }
    return render(request, 'listing/buy.html',context)

def expert_view (request):
    expert = Expert.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(expert, 6)
    try:
        experts = paginator.page(page)
    except PageNotAnInteger:
        experts = paginator.page(1)
    except EmptyPage:
        experts = paginator.page(paginator.num_pages)
    context = {
        'experts': experts
    }
    return render(request, 'listing/Expert.html',context)
def rent_view (request):
    productlist  = ProductPropertyModel.objects.filter(status = 'For Rent')
    filters = ProductPropertyModelFiler(request.GET , queryset= productlist)
    page = request.GET.get('page', 1)

    paginator = Paginator(filters.qs, 6)
    try:
        productlists = paginator.page(page)
    except PageNotAnInteger:
        productlists = paginator.page(1)
    except EmptyPage:
        productlists = paginator.page(paginator.num_pages)
    context = {
        "productlists": productlists,
        "filters": filters
    }
    return render(request, 'listing/rent.html' , context)


# Dashboard Pages
@login_required(login_url='/login')
def base_dashboard_view (request):
    user_obj = CustomUser.objects.filter( pk = request.user.id)
    context = {
        'user_obj': user_obj
    }
    return render(request, 'dashboard/base.html' , context)
@login_required(login_url='/login')
def dashboard_view (request):
    context = {}
    if request.user.user_type == 'Agent':
        agent_obj = Agent.objects.get(admin = request.user.id)
    message_obj = AgentMessage.objects.filter(agent = agent_obj.id)
    context = {
        "message": message_obj
    }
    return render(request, 'dashboard/Dashboard.html' , context)
@login_required(login_url='/login')
def dashboard_message_view (request):
    agent_obj = Agent.objects.get(admin = request.user.id)
    message_obj = AgentMessage.objects.filter(agent = agent_obj.id)
    context = {
        "message": message_obj
    }
    return render(request, 'dashboard/message.html', context)
@login_required(login_url='/login')
def dashboard_profile_view (request):
    user_obj = CustomUser.objects.get(pk = request.user.id)
    context = {
        "user_obj" : user_obj
    }
    return render(request, 'dashboard/profile.html' , context)
@login_required(login_url='/login')
def dashboard_propertyListing_view (request):
    agent_obj = Agent.objects.get(admin = request.user.id)
    productDetail = ProductPropertyModel.objects.filter(agent = agent_obj.id)
    page = request.GET.get('page', 1)

    paginator = Paginator(productDetail, 6)
    try:
        productDetails = paginator.page(page)
    except PageNotAnInteger:
        productDetails = paginator.page(1)
    except EmptyPage:
        productDetails = paginator.page(paginator.num_pages)
    context = {
        "productDetails": productDetails
    }
    return render(request, 'dashboard/PropertyListing.html' , context)
@login_required(login_url='/login')
def dashboard_wishlist_view (request):
    return render(request, 'dashboard/Wishlist.html')
@login_required(login_url='/login')
def dashboard_addListing_view (request):
    return render(request, 'dashboard/AddListing.html')
#End of Dashboard Pages


def productDetail (request , product_pk):
    productDetail = get_object_or_404(ProductPropertyModel , pk = product_pk)
    productRate = ProducttRate.objects.filter(product = product_pk)
    imageDetail = ProductImageModel.objects.filter(product = product_pk)
    viewNumber = productRate.count()
    now = datetime.now()
    starCount = 0
    for i in productRate:
        starCount += i.rate
    if starCount != 0:
        starCount = starCount // viewNumber
    starNullCount = 5 - starCount
    starNullCount = range(0 , starNullCount)
    starCount = range(0,starCount)
    context = {
        "productDetail": productDetail,
        "productRate" : productRate,
        "now" : now,
        "imageDetail" : imageDetail,
        "viewNumber" : viewNumber,
        "starCount" : starCount,
        'starNullCount' : starNullCount,
    }  
    return render(request,'Productdetial.html' , context)


@login_required(login_url='/login')
def addlisting(request):
    if request.method == 'POST':
        amenites = mod.ProductAmenitiesModel()
        amenites.Air_Conditioning = True if 'ari_condition' in request.POST else False
        amenites.Balcony = True if 'balcony' in request.POST else False
        amenites.Garden_Yard = True if 'yard' in request.POST else False
        amenites.Pool = True if 'poll' in request.POST else False
        amenites.Security_System = True if 'security_system' in request.POST else False
        amenites.Parking_Space = True if 'parking_space' in request.POST else False
        amenites.Basement = True if 'basement' in request.POST else False
        amenites.BBQ_Area = True if 'bbq_area' in request.POST else False
        amenites.Walk_in_Closet = True if 'walk_in_closet' in request.POST else False
        amenites.Central_Heating = True if 'centralHeating' in request.POST else False
        amenites.Deck_Patio = True if 'Deck_Patio' in request.POST else False
        amenites.Dishwasher = True if 'dishwasher' in request.POST else False
        amenites.Fireplace = True if 'fireplace' in request.POST else False
        amenites.Fitness_Center_Gym = True if 'fitness_Center_Gym' in request.POST else False
        amenites.Garage = True if 'garage' in request.POST else False
        amenites.Hardwood_Floors = True if 'hardwood_floors' in request.POST else False
        amenites.Laundry_Room = True if 'laundry_room' in request.POST else False
        amenites.Washer_Dryer_Hookups = True if 'washer_dryer_hookups' in request.POST else False
        amenites.Wheelchair_Accessible = True if 'wheelchair_accessible' in request.POST else False
        amenites.Pet_Friendly = True if 'pet_friendly' in request.POST else False
        amenites.High_Speed_Internet_Access = True if 'high_speed_internet_access' in request.POST else False
        amenites.Cable_Satellite_TV = True if 'cable_satellite_tV' in request.POST else False
        amenites.Fully_Furnished = True if 'fully_furnished' in request.POST else False
        amenites.Gated_Community = True if 'gated_community' in request.POST else False
        amenites.Tennis_Basketball_Court = True if 'tennis_basketball_court' in request.POST else False
        amenites.Playground = True if 'playground' in request.POST else False
        amenites.Elevator = True if 'elevator' in request.POST else False
        amenites.Waterfront_Access = True if 'waterfront_access' in request.POST else False
        amenites.Close_to_Public_Transportation = True if 'close_to_public_transportation' in request.POST else False
        amenites.Proximity_to_Schools = True if 'proximity_to_schools' in request.POST else False
        amenites.Nearby_Shopping_Restaurants = True if 'nearby_shopping_restaurants' in request.POST else False
        amenites.Access_to_Parks_Recreational_Areas = True if 'access_to_Parks_recreational_areas' in request.POST else False
        amenites.On_Site_Maintenance = True if 'on_site_maintenance' in request.POST else False
        amenites.On_Site_Management = True if 'on_site_management' in request.POST else False
        amenites.Hour_Security = True if 'hour_security' in request.POST else False
        amenites.Energy_Efficient_Appliances = True if 'energy_efficient_appliances' in request.POST else False
        amenites.Green_Building_Features = True if 'green_building_features' in request.POST else False
        amenites.Smart_Home_Technology = True if 'smart_home_technology' in request.POST else False
        amenites.Outdoor_Entertaining_Area = True if 'outdoor_entertaining_area' in request.POST else False
        amenites.Wine_Cellar = True if 'wine_cellar' in request.POST else False
        amenites.Home_Theater = True if 'home_theater' in request.POST else False
        amenites.Office_Study_Room = True if 'office_study_room' in request.POST else False
        amenites.Guest_House_In_Law_Suite = True if 'guest_house_in_law_suite' in request.POST else False
        amenites.Game_Room = True if 'game_room' in request.POST else False
        amenites.Vaulted_Ceilings = True if 'vaulted_ceilings' in request.POST else False
        amenites.Skylights = True if 'skylights' in request.POST else False
        amenites.Workshop_Studio_Space = True if 'workshop_studio_space' in request.POST else False
        amenites.Solar_Panels = True if 'solar_panels' in request.POST else False
        amenites.Mountain_City_View = True if 'mountain_city_view' in request.POST else False
        animt = amenites
        amenites.save()
        
        user_obj = get_object_or_404(CustomUser , pk = request.user.id)
        
        agent_obj = Agent.objects.get(admin = user_obj)

        productProperty = mod.ProductPropertyModel()
        productProperty.tile = request.POST['txt_title']
        productProperty.description = request.POST['txt_description']
        productProperty.type = request.POST['txt_type']
        productProperty.city = request.POST['txt_city']
        productProperty.status = request.POST['txt_states']
        productProperty.postal_Code = request.POST['txt_postalCode']
        productProperty.floor = request.POST['txt_floor']
        productProperty.bed = request.POST['txt_bed']
        productProperty.bath = request.POST['txt_bath']
        productProperty.room = request.POST['txt_room']
        productProperty.area = request.POST['txt_area']
        productProperty.lotarea = request.POST['txt_lotarea']
        productProperty.price = request.POST['txt_price']
        productProperty.grauge = request.POST['txt_grauge']
        productProperty.medai_url = request.POST['txt_media']
        productProperty.coverPhoto = request.FILES['image']
        productProperty.amenities = animt
        productProperty.agent = agent_obj
        prod = productProperty
        productProperty.save()
        images = request.FILES.getlist('images')
        for img in images:
            productImage = mod.ProductImageModel()
            productImage.image = img
            productImage.product = prod
            productImage.save()
        return redirect('addlisting')
    return render(request, 'addListing.html', {})

def dologin(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = EmailBackEnd.authenticate(request , email = email, password = password)
        if user != None:
            login(request , user)
            return redirect('dashboard')
        else:
            messages.error(request , "Email or password is incorrect!")
            return redirect ('login')
    
    return render(request , 'loginPage.html')

def dologout(request):
    logout(request)
    return redirect('login')

def register(request):
    if request.method == 'POST':
        name = request.POST.get('txtname')
        lname = request.POST.get('txtlname')
        userType = request.POST.get('txtusertype')
        profileImage = request.FILES['profileimage']
        phone = request.POST.get('txtphone')
        email = request.POST.get('txtemail')
        password = request.POST.get('txtpassword1')
        repassword = request.POST.get('txtpassword2')
        if password == repassword:
            if CustomUser.objects.filter(email = email).exists():
                messages.error(request ,'email is already exists')
                return redirect('register')
            else:    
                randomNumber = random.randint(1,10000)
                username = name + '-' + lname + str(randomNumber)
                username = username.lower()
                user = CustomUser.objects.create_user(username = username,email=email, password=password)
                user.first_name = name
                user.last_name = lname
                user.profile_image = profileImage
                user.user_type = userType
                city = request.POST.get('txtcity')

                location_obj = Location(
                    city = city,
                )
                location_obj.save()
                user.save()
                if userType == 'Agent':
                    agent_obj = Agent (
                        admin = user,
                        phone = phone,
                        location = location_obj
                    )
                    agent_obj.save()
                    return redirect('home')
                elif userType == 'User':
                    user_obj = Customer (
                        admin = user,
                        phone = phone,
                        location = location_obj
                    )
                    user_obj.save()
                elif userType == 'Expert':
                    expert_obj = Expert(
                        admin = user,
                        phone = phone,
                        location = location_obj
                    )
                    expert_obj.save()
                return redirect('login')
        else:
            messages.error(request , 'Password is not match')
            return redirect('register')
    return render(request , 'Registraion.html')

def productRateComment(request , product_id):
    if request.method == 'POST':
        comment = request.POST.get('comment')
        rating1 = request.POST.get('rating1')
        rating2 = request.POST.get('rating2')
        rating3 = request.POST.get('rating3')
        rating4 = request.POST.get('rating4')
        rating5 = request.POST.get('rating5')
        star = 0
        if rating1 != None:
            star = int(rating1)
        elif rating2 != None:
            star = int(rating2)
        elif rating3 != None:
            star = int(rating3)
        elif rating4 != None:
            star = int(rating4)
        elif rating5 != None:
            star = int(rating5)
        product_obj = get_object_or_404(ProductPropertyModel,pk = product_id)
        user_obj = get_object_or_404(CustomUser,pk = request.user.id)
        product_rate = ProducttRate(
            comment = comment,
            rate = star,
            product = product_obj,
            user = user_obj
        )

        product_rate.save()
        return redirect('home')
    return render(request,'Productdetial.html')

def agentRateComment (request , agent_id):
    if request.method == 'POST':
        comment = request.POST.get('comment')
        rating1 = request.POST.get('rating1')
        rating2 = request.POST.get('rating2')
        rating3 = request.POST.get('rating3')
        rating4 = request.POST.get('rating4')
        rating5 = request.POST.get('rating5')
        star = 0
        if rating1 != None:
            star = int(rating1)
        elif rating2 != None:
            star = int(rating2)
        elif rating3 != None:
            star = int(rating3)
        elif rating4 != None:
            star = int(rating4)
        elif rating5 != None:
            star = int(rating5)
        agent_obj = get_object_or_404(Agent, pk = agent_id)
        user_obj = get_object_or_404(CustomUser, pk = request.user.id)

        agent_rate = AgentRate (
            comment = comment,
            rate = star,
            agent = agent_obj,
            user = user_obj
        )
        agent_rate.save()
        return redirect('home')
    return render(request,'profileDetail.html')

def agentContact (request , agent_id):
    if request.method == 'POST':
        fullname = request.POST.get('txtfullname')
        phone = request.POST.get('txtphone')
        service = request.POST.get('txtservice')
        proptype  = request.POST.get('txtproptype')
        message = request.POST.get('txtmessage')
        user_obj = get_object_or_404(CustomUser , pk = request.user.id)
        agent_obj = get_object_or_404(Agent , pk = agent_id)

        agentContact_obj = AgentMessage (
            fullname = fullname,
            phone = phone,
            service = service,
            propType = proptype,
            message = message,
            agent = agent_obj,
            user = user_obj
        )
        agentContact_obj.save()
        return redirect('home')
    return render(request , 'profileDetail.html')

def product_delete(request, product_id):
    product = get_object_or_404(ProductPropertyModel , pk = product_id)
    if request.method == 'POST':
        product.delete()
        return redirect('dashboard')
    return render(request , 'dashboard/PropertyListing.html')

def product_update (request , product_id):
    if request.method == 'POST':
        item = get_object_or_404(ProductPropertyModel , pk = product_id)
        if request.method == 'POST':
            isactive = request.POST.get('is_active')
            item.isactive = True if isactive == '1' else False
            item.status = request.POST.get('status')
            item.save()
            return redirect('dashboard')
    return render(request, 'dashboard/PropertyListing.html')

def search_banner(request):
    if request.method == 'POST':
        search = request.POST.get('txtsearch')
        search = search.lower()
        if search == 'rent':
            return redirect('rent')
        elif search == 'buy':
            return redirect('buy')
        else:
            return render('home')
    return render(request, 'index.html')
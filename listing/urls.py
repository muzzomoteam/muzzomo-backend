from django.urls import path
from .views import *
urlpatterns =[
    path('',home , name='home'),
    path('base-view/' , base_view , name='base'),
    path('agent-page-view/' , agent_page_view  , name='agentpage'),
    path('product-detail/' , product_detail_view , name='productdetail'),
    path('add-listing-view/' , add_listing_view , name='addlisting'),
    path('login-view/' , login_view , name='login'),
    path('register-view/' , registration_view , name='register'),
    path('agent-view/' ,agent_view , name='agent'),
    path('buy-view/' , buy_view , name='buy'),
    path('expert-view/',expert_view , name='expert'),
    path('rent-view/' , rent_view , name='rent'),
]
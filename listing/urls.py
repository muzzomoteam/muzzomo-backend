from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns =[
    path('',home , name='home'),
    path('base-view/' , base_view , name='base'),
    path('Profile/<int:user_id>' , agent_page_view  , name='agentpage'),
    path('ExpertProfile/<int:user_id>', expert_page_view , name='ExpertProfile'),
    path('product-detail/' , product_detail_view , name='productdetail'),
    path('addlisting/' , addlisting , name='addlisting'),
    path('login' , dologin , name='login'),
    path('dologout' , dologout , name='dologout'),
    path('register' , register , name='register'),
    path('agent-view/' ,agent_view , name='agent'),
    path('buy-view/' , buy_view , name='buy'),
    path('expert-view/',expert_view , name='expert'),
    path('rent-view/' , rent_view , name='rent'),
    path('base-dashboard-view/',base_dashboard_view , name='baseDashboard'),
    path('dashboard',dashboard_view , name='dashboard'),
    path('dashboard-message-view/',dashboard_message_view , name='dashboardMessage'),
    path('dashboard-profile-view/',dashboard_profile_view, name='dashboardProfile'),
    path('dashboard-propertyListing-view/' , dashboard_propertyListing_view , name='dashboardPropertyListing'),
    path('dashboard-wishlist-view/' , dashboard_wishlist_view , name='dashboardWishlist'),
    path('dashboard-addListing-view/' , dashboard_addListing_view , name='dashboardAddListing'),
    path('productDetailselect/<int:product_pk>' , productDetail , name='productDetailselect'),
    path('productCommnets/<int:product_id>' , productRateComment , name='productCommnets'),
    path('agentComments/<int:agent_id>' , agentRateComment ,name = 'agentComments'),
    path('agentContact/<int:agent_id>', agentContact , name='agentContact'),
    path('productDelete/<int:product_id>', product_delete , name='productDelete'),
    path('productUpdate/<int:product_id>' , product_update , name='productUpdate'),
    path('search-banner', search_banner , name='search-banner'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
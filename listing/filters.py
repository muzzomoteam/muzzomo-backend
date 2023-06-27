import django_filters
from django import forms
from .models import *

class ProductPropertyModelFiler(django_filters.FilterSet):
    city = django_filters.CharFilter(lookup_expr='icontains' , label='City', widget=forms.TextInput(attrs={'placeholder':'City','class': 'form-control'}))
    type = django_filters.CharFilter(lookup_expr='icontains' , label='Type', widget=forms.TextInput(attrs={'placeholder':'Status','class': 'form-control'}))
    status = django_filters.CharFilter(lookup_expr='icontains' , label='Status', widget=forms.TextInput(attrs={'placeholder':'Type','class': 'form-control'}))
    price = django_filters.CharFilter(lookup_expr='icontains' , label='Price', widget=forms.TextInput(attrs={'placeholder':'Price','class': 'form-control'}))

    class Meta:
        model = ProductPropertyModel

        fields = ['city' , 'type' , 'status', 'price']

class AgentFilter(django_filters.FilterSet):
   rate = django_filters.CharFilter(lookup_expr="icontains" , label="Name" , widget=forms.TextInput(attrs={'placeholder':'Rating','class': 'form-control'}))
   class Meta:
        model = Agent
        fields = ['rate']
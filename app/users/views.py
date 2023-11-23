from typing import Any
from django.shortcuts import render
from django.views import View
from django.http.response import HttpResponse
from django.views.generic.base import TemplateView

from app.product.models import Product
from app.partners.models import Partner, Client

from .forms import RegistrationForm, LoginForm



class MainPageView(TemplateView):
    template_name = 'main_page.html'
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['latest_products'] = Product.objects.all()[:5]
        context['partners'] = Partner.objects.all()[:5]
        context['clients'] = Client.objects.all()[:5]
        return context
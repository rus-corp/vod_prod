from typing import Any
from django.shortcuts import render
from django.views import generic
from django.core.paginator import Paginator

from .models import Product, Category, MainCategory





class ProductView(generic.ListView):
    queryset = Product.objects.all()
    template_name = 'products/test.html'

    
    
    
def main_categories_view(request, main_category=None, category=None, product=None):
    main_category_list = MainCategory.objects.all()
    category_list = None
    if main_category:
        main_category_obj = MainCategory.objects.get(slug=main_category)
        category_list = Category.objects.filter(main_category=main_category_obj)
    product_list = None
    if category:
        category_obj = Category.objects.get(slug=category)
        product_list = Product.objects.filter(category=category_obj)
    context = {
        'main_category_slug': main_category,
        'main_categories': main_category_list,
        'categories': category_list,
        'products': product_list,
    }
    return render(request, 'catalog.html', context)
        










#     context = {'main_categories': main_categories}
#     return render(request, 'products/main_categories.html', context)
    
    
# def categories_view(request, main_category_slug=None):
#     main_category = MainCategory.objects.get(slug=main_category_slug)
#     categories = Category.objects.filter(main_category=main_category)
#     context = {
#         'main_category': main_category,
#         'categories': categories
#     }
#     return render(request, 'products/categories.html', context)
    
    
# def product_view(request, main_category_slug, category_slug=None):
#     category = Category.objects.get(slug=category_slug)
#     categories = Category.objects.all()
#     products = Product.objects.filter(category=category)
#     context = {
#         'categories': categories,
#         'products': products
#     }
#     return render(request, 'products/products.html', context)
    
    
    
    
    
    
    
# def products_all(request, main_category=None):
#     if not main_category:
#         main_category_obj = MainCategory.objects.all()
#         categories = Category.objects.filter(main_category=main_category_obj)
#         products = Product.objects.filter(category=1)
#     else:
#         main_category_obj = MainCategory.objects.get(slug=main_category)
#         categories = Category.objects.filter(main_category=main_category_obj)
#         products = Product.objects.filter(category=1)
#     if 'category' in request.GET:
#         category_obj = Category.objects.get(slug=request.GET['category'])
#         products = Product.objects.filter(category=category_obj)
#     context = {
#         'main_categories': main_category_obj,
#         'categories': categories,
#         'products': products
#     }
#     return render(request, 'products/catalog.html', context)
    
    
    
    
    
    
    # main_category_list = MainCategory.objects.all()
    # category_list = None
    # product_list = None
    # if main_category:
    #     main_category_obj = MainCategory.objects.get(slug=main_category)
    #     category_list = Category.objects.filter(main_category=main_category_obj)
    #     product_list = None
    # if category:
    #     category_obj = Category.objects.filter(slug=category)
    #     product_list = Product.objects.filter(category=category_obj)
    # context = {
    #     'main_categories': main_category_list,
    #     'categories': category_list,
    #     'products': product_list
    # }
    # return render(request, 'products/catalog.html', context)
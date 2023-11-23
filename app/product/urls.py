from django.urls import path


from .views import ProductView, main_categories_view


app_name = 'product'


urlpatterns = [
    path('', main_categories_view, name='main_category'),
    path('<str:main_category>/', main_categories_view, name='main_categories'),
    path('<str:main_category>/<str:category>/', main_categories_view, name='categories'),
    # path('<str:main_category>/<str:category>/', main_categories_view, name='products'),
]
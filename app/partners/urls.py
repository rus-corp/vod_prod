from django.urls import path


from app.product.views import ProductView


app_name = 'partners'

urlpatterns = [
    path('test/', ProductView.as_view(), name='test')
]
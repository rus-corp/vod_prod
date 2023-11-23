from django.urls import path


from .views import MainPageView

app_name = 'users'


urlpatterns = [
    path('', MainPageView.as_view(), name='main_page')
]
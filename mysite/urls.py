from django.urls import path
from .import views

app_name = 'mysite'
urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("register/", views.register, name="register"),
    path('logout/',views.logout_request,name='logout'),
    path("login/", views.login_request, name="login"),
    # path('lang/',views.localization,name='lang')
    
]
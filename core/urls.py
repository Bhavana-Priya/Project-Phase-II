"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from app.views import (
    home, index, search, predict, ticker, signup, login_view, about_us, 
    show_qr, generate_qr, verify_otp ,clear_confetti, gemini_chat_api,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),  
    path('index/', index, name='index'),  
    path('signup/', signup, name='signup'),  
    path('login/', login_view, name='login'),  # Custom login view
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),  
    path('about/', about_us, name='about'),  
    path('search/', search, name='search'),  
    path('show_qr/', show_qr, name='show_qr'),
    path('predict/<str:ticker_value>/<str:number_of_days>/', predict, name='predict'),  
    path('ticker/', ticker, name='ticker'),  
    path('generate_qr/', generate_qr, name='generate_qr'),
    path('verify_otp/', verify_otp, name='verify_otp'),
    path('clear-confetti/',clear_confetti, name='clear_confetti'),
    path('gemini-chat-api/',gemini_chat_api, name='gemini_chat_api'),

]







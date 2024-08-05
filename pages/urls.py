# pages/urls.py
from django.urls import path, include
from django.contrib.auth import views as auth_views

from .views import home_page_view, home_page_template, login_template, secret_template

urlpatterns = [
        path("", include("allauth.urls")),
        path("", home_page_template),
        path("accounts/login/", login_template, name='login'),
	path('accounts/logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
	path('secret', secret_template)
        ]


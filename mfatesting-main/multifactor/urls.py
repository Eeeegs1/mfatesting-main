from django.urls import path
from matplotlib import test

from . import views
from .factors import totp


app_name = 'multifactor'

urlpatterns = [
    path('', views.List.as_view(), name="home"),
    path('<str:action>:<slug:ident>/', views.List.as_view(), name="action"),
    path('help/', views.Help.as_view(), name="help"),
    path('authenticate/', views.Authenticate.as_view(), name="authenticate"),
    path('add/', views.Add.as_view(), name="add"),
    path('rename/<int:pk>/', views.Rename.as_view(), name="rename"),
    path('totp/new/', totp.Create.as_view(), name="totp_start"),
    path('totp/auth/', totp.Auth.as_view(), name="totp_auth"),
]

from django.urls import path

from . import views
urlpatterns = [
    path('dashboard',views.dashboard_page, name = 'dashboard_page'),
    path('api/dashboard',views.dashboard_api, name = 'dashboard_api'),
    ]

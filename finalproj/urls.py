from . import views
from django.urls import path

urlpatterns = [
    path('',views.home,name="home"),
    path('shop-detail/',views.detail,name="detail"),
    path('shop-listing/',views.listing,name="list")
]

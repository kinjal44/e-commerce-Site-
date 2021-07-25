from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path("", views.index, name="ShopHome"),
    path("about/", views.about, name="AboutUs"),
    path("contact/", views.contact, name="ContactUs"),
    path("tracker/", views.tracker, name="TrackingStatus"),
    path("search/", views.search, name="Search"),
    path("productView/<int:myid>", views.productView, name="productView"),
    path("checkout/", views.checkout, name="Checkout"),
    #path("handleRequest/", views.handleRequest, name="handleRequest"),

]
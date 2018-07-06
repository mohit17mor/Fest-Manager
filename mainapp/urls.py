from django.contrib import admin
from django.urls import path,include
from mainapp import views

app_name='mainapp'

urlpatterns = [
    path('', views.dashboard, name = 'dashboard'),
    path('auth/', views.auth, name = 'auth'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('contract/create/', views.create_contract, name = 'create_contract'),
    path('cart/', views.cart, name = 'cart'),
    path('contract/addtocart/<int:id>', views.add_to_cart, name = 'add_contract_to_cart'),
    path('logout/', views.logout_view, name = 'logout'),
    path('contract/remove/<int:id>/', views.remove_contract,name='remove_contract'),
    path('contract/removefromcart/<int:id>/', views.remove_from_cart, name = 'remove_from_cart'),
    path('contract/edit/<int:id>/', views.edit_contract, name = 'edit_contract'),
    path('contract/addtocart/package1', views.add_package1, name = 'add package 1'),
    path('contract/addtocart/package2', views.add_package2, name = 'add package 2'),
    path('contract/addtocart/package3', views.add_package3, name = 'add package 3'),
]

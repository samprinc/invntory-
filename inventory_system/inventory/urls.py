from django.urls import path
from . import views
from .views import CustomLoginView

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('add-product/', views.add_product, name='add_product'),
    path('make-sale/', views.make_sale, name='make_sale'),
    path('accounts/login/', CustomLoginView.as_view(), name='login'),
    path('products/', views.product_list, name='product_list'),
    
]
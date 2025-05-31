from django.urls import path
from . import views
from .views import CustomLoginView

urlpatterns = [
    path('', views.dashboard, name='dashboard'),            # Root URL → dashboard
    path('dashboard/', views.dashboard, name='dashboard'),  # Optional duplicate route
    path('add-product/', views.add_product, name='add_product'),
    path('make-sale/', views.make_sale, name='make_sale'),
    path('login/', CustomLoginView.as_view(), name='login'),  # login path should be /login/ (not accounts/login)
    path('products/', views.product_list, name='product_list'),
]

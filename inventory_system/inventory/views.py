# Step 3: Views (inventory/views.py)
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Product, Sale
from .forms import ProductForm, SaleForm
from django.contrib.auth.views import LoginView


def dashboard(request):
    products = Product.objects.all()
    sales = Sale.objects.order_by('-sold_at')[:5]
    return render(request, 'inventory/dashboard.html', {'products': products, 'sales': sales})

from django.contrib import messages

@login_required
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Product added successfully!")
            return redirect('dashboard')
    else:
        form = ProductForm()
    return render(request, 'inventory/add_product.html', {'form': form})

@login_required
def make_sale(request):
    if request.method == 'POST':
        form = SaleForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Sale recorded successfully!")
            return redirect('make_sale')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = SaleForm()

    return render(request, 'inventory/make_sale.html', {'form': form})

@login_required
def account(request):
    return render(request, 'inventory/account.html')

from .models import Product  # Make sure you have a Product model

def product_list(request):
    products = Product.objects.all()
    return render(request, 'inventory/product_list.html', {'products': products})


class CustomLoginView(LoginView):
    template_name = 'registration/login.html'  # Adjust path to your login template
    redirect_authenticated_user = True
    def get_success_url(self):
        return self.request.GET.get('next', 'dashboard')  # Redirect to dashboard or next URL

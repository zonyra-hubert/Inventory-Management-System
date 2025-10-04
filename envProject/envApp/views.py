from django.shortcuts import render,redirect
from .forms import ProductForm
from .models import Product
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.contrib.auth.models import User
from .forms import RegisterForm

# Create your views here.

@login_required
def product_create_view(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    return render(request, 'envApp/product_form.html', {'form': form})

@login_required
def product_list_view(request):
    products = Product.objects.all()
    return render(request, 'envApp/product_list.html', {'products': products})

@login_required
def product_update_view(request, product_id):
    product = Product.objects.get(product_id=product_id)
    form = ProductForm(instance=product)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    return render(request, 'envApp/product_form.html', {'form': form})

@login_required
def product_delete_view(request, product_id):
    product = Product.objects.get(product_id=product_id)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'envApp/product_confirm_delete.html', {'product': product})

# REMOVED @login_required from register_view
def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = User.objects.create_user(username=username, password=password)
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'envApp/register.html', {'form': form})  # Changed to envApp/

# REMOVED @login_required and kept only ONE login_view function
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            next_url = request.POST.get('next') or request.GET.get('next') or 'home'
            return redirect(next_url)
        else:
            error_message = 'Invalid credentials'
            return render(request, 'envApp/login.html', {'error': error_message})
    else:
        # Handle GET requests (display login form)
        return render(request, 'envApp/login.html')

@login_required            
def logout_view(request):
    if request.method=='POST':
        logout(request)
        return redirect('login')
    else:
        return redirect('home')

# home view - using decorator 
@login_required
def home_view(request):
    return render(request, 'envApp/home.html')

# protected view using mixin
class ProtectedView(LoginRequiredMixin, View):
    login_url = '/login/'  # Fixed: added the login URL
    
    redirect_field_name = 'redirect_to'
    
    def get(self, request):
        return render(request, 'registration/protected.html')




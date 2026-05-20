from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import Product, Order
from .forms import ProductForm, OrderForm
from django.contrib.auth import logout
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.forms import inlineformset_factory
from .models import Product, Order, ProductImage
from .forms import ProductForm, OrderForm, ProductImageForm

def home(request):

    products = Product.objects.all()

    return render(request, 'home.html', {
        'products': products
    })

@login_required
def dashboard(request):

    products = Product.objects.all()

    return render(
        request,
        'dashboard/dashboard.html',
        {
            'products': products
        }
    )


def admin_login(request):

    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None and user.is_superuser:

            login(request, user)

            return redirect('dashboard')

    return render(request, 'dashboard/login.html')

@login_required
def add_product(request):
    ProductImageFormSet = inlineformset_factory(
        Product, ProductImage, form=ProductImageForm, extra=4, max_num=10, can_delete=True
    )
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        formset = ProductImageFormSet(request.POST, request.FILES)
        if form.is_valid() and formset.is_valid():
            product = form.save()
            # حفظ الصور
            for img_form in formset:
                if img_form.cleaned_data.get('image'):
                    image = img_form.save(commit=False)
                    image.product = product
                    image.save()
            return redirect('dashboard')
    else:
        form = ProductForm()
        formset = ProductImageFormSet()
    return render(request, 'dashboard/add_product.html', {
        'form': form,
        'formset': formset,
    })



def product_details(request, id):
    product = get_object_or_404(Product, id=id)
    product_images = product.images.all()  # جلب جميع الصور المرتبطة
    form = OrderForm()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.product = product
            order.save()
            return render(request, 'order_success.html')
    return render(request, 'product_details.html', {
        'product': product,
        'product_images': product_images,
        'form': form,
    })

@login_required
def orders(request):

    all_orders = Order.objects.all().order_by('-id')

    return render(
        request,
        'dashboard/orders.html',
        {
            'orders': all_orders
        }
    )

def delete_product(request, id):

    product = Product.objects.get(id=id)

    product.delete()

    return redirect('dashboard')

def admin_logout(request):

    logout(request)

    return redirect('admin_login')

@login_required
def update_order_status(request, id, status):

    order = Order.objects.get(id=id)

    order.status = status

    order.save()

    return redirect('orders')

@login_required
def delete_order(request, id):

    order = Order.objects.get(id=id)

    order.delete()

    return redirect('orders')
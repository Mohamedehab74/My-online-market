from django.shortcuts import render, get_object_or_404 , redirect
from .models import Product

def product_list(request):
    products = Product.objects.all()
    return render(request, 'store/product_list.html', {'products': products})

def expensive_products(request):
    products = Product.objects.filter(price__gt=100)
    return render(request, 'store/product_list.html', {'products': products})

def food_products(request):
    products = Product.objects.filter(category="FD")
    return render(request, 'store/product_list.html', {'products': products})

def search_products(request):
    query = request.GET.get('q', '')
    if query:
        products = Product.objects.filter(name__icontains=query)
    else:
        products = Product.objects.all()
    return render(request, 'store/product_list.html', {'products': products, 'query': query})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'store/product_detail.html', {'product': product})

def create_product(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        category = request.POST.get('category')
        description = request.POST.get('description')
        available_until = request.POST.get('available_until')
        image = request.FILES.get('image')  
        
        Product.objects.create(
            name=name,
            price=price,
            category=category,
            description=description,
            available_until=available_until,
            image=image
        )
        return redirect('product_list')

    return render(request, 'store/create_product.html')
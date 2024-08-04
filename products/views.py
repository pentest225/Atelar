from django.shortcuts import render

# Create your views here.

def products(request):
    print("On The Product Details Page")
    return render(request, 'product/products.html')

def product_details(request):
    print("On The Product Details Page")
    return render(request, 'product/product-detail.html')
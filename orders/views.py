from django.shortcuts import render

# Create your views here.
def orders(request):
    print("Order List")
    return render(request,'orders/order-list.html')

def checkout(request):
    return render(request,'orders/checkout.html')

def order_complete(request):
    print("On The Order Complete Page")
    return render(request,'orders/order-completed.html')
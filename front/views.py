from django.shortcuts import render


# Create your views here.
def index(request):
    #TODO:LISTE DES INFORMATIONS A AFFICHER DANS LE CAROUSEL
    #TODO: LISTE DES TOP CATEGORIE
    #TODO: LIST DES TOP PRODUITS
    #TODO: LIST DES OFFRES SPÉCIALE

    print("On The Index Page")
    return render(request, 'index4.html')


def about(request):
    print("On The About Page")
    return render(request, 'about.html')


def contact(request):
    print("On The Contact Page")
    return render(request, 'contact-us.html')


def my_account(request):
    print("On The My Account Page")
    return render(request, 'my-account.html')


def wishlist(request):
    print("On The Wishlist Page")
    return render(request, 'wishlist.html')



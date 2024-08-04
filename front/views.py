from django.shortcuts import render
from .models import BannerSection


# Create your views here.
def index(request):
    #TODO:LISTE DES INFORMATIONS A AFFICHER DANS LE CAROUSEL
    banners = BannerSection.objects.all()
    #TODO: LISTE DES TOP CATEGORIE
    #TODO: LIST DES TOP PRODUITS
    #TODO: LIST DES OFFRES SPÉCIALE
    #print(banners.first().banner_image.url)
    print(banners.first().banner_title)
    print(banners.first().banner_image)

    return render(request, 'index4.html', {"banners": banners, "patrick": "Dagouaga Patrick"})


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

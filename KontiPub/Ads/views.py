from django.shortcuts import render, redirect
from .models import Administrateur, Ads
import os
from django.conf import settings

categoryNames=[
    "Evenement",
    "Restauration",
    "Beauté",
    "Nuit"
]

# Create your views here.
def Index(request): 
    return render(request, "index.html")

def Beauty(request):
    events = Ads.objects.filter(category="Beauté")
    return render(request, "beaute.html", context={"events":events})

def Evenement(request):
    events = Ads.objects.filter(category="Evenement")
    return render(request, "evenement.html", context={"events":events })

def Restauration(request):
    events = Ads.objects.filter(category="Restauration")
    return render(request, "restauration.html", context={"events":events })

def Nuit(request):
    events = Ads.objects.filter(category="Nuit")
    return render(request, "nuit.html", context={"events":events })

def Pricing(request):
    return render(request, "pricing.html")

def Contact(request):
    return render(request, "contact.html")

def About(request):
    return render(request, "about.html")

def Login(request):
    return render(request, "login.html")

def Register(request):
    # ad= Administrateur(name="Aline FOka",email="alinef@gmail.com", password="digitalCollege")
    # ad.save()
    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        description = request.POST.get('Description')
        address = request.POST.get('adress')
        country = request.POST.get('country')
        state = request.POST.get('state')
        city = request.POST.get('city')
        category = request.POST.get('categorie')
        date_event = request.POST.get('date')
        hour = request.POST.get('heure')
        avatar = request.FILES.get('images')  
        img_path = os.path.join(settings.MEDIA_ROOT,avatar.name)
        with open(img_path, 'wb') as img_file:
                for chunk in avatar.chunks():
                    img_file.write(chunk)
        # Traitez les données comme vous le souhaitez, par exemple, en les enregistrant dans un modèle Ads
        ad= Administrateur.objects.get(pk=1)
        ad = Ads(
            productName=name,
            price=price,
            description=description,
            address=address,
            country=country,
            state=state,
            city=city,
            category=category,
            date_event=date_event,
            hour=hour,
            admin=ad,
            avatar=avatar
        )
        ad.save()

    obj={"categories":categoryNames}
    return render(request, "signup.html", context=obj)

def AdsDetail(request, id):
    return render(request, "browse-ads-details.html")
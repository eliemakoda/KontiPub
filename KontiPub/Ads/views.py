from django.shortcuts import render, redirect
from .models import Administrateur, Ads
import os
from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail,EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags

categoryNames=[
    "Evenement",
    "Restauration",
    "Beauté",
    "Nuit"
]
def sendmails( tmp):
        my_subject = "Email de KONTIPUB"
        my_recepient = ["fokaalinegrace@gmail.com"] #replace by tmp.email
        html_message = render_to_string("email.html", context=tmp)
        plain_message = strip_tags(html_message)
        message = EmailMultiAlternatives(
            subject=my_subject,
            body=plain_message,
            from_email=settings.EMAIL_HOST_USER,
            to=my_recepient
        )
        #  {"username":username,"email":email, "phone":phone,"subject":subject,"message":message}
        message.attach_alternative(html_message, "text/html")
        message.send(fail_silently=False)

# Create your views here.
def Index(request): 
    events= Ads.objects.all()[:8]
    return render(request, "index.html", context={
        "events": events,
        "categories":categoryNames
    })

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
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        tmp_data= {"username":username,"email":email, "phone":phone,"subject":subject,"message":message}
        sendmails(tmp_data)
    return render(request, "contact.html")

def About(request):
    return render(request, "about.html")

def Login(request):
    if request.method == "POST":
        email= request.POST.get("email")
        password= request.POST.get('password')
        print("password: ", password)
        print("Email: ", email)
        try:
            ad= Administrateur.objects.get(email=email,password=password )
            obj={"categories":categoryNames}
            return render(request,"signup.html",context=obj)    
        except Administrateur.DoesNotExist:
            redirect('login')
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
    target= Ads.objects.get(pk=id)
    ads= Ads.objects.filter(category=target.category)
    return render(request, "browse-ads-details.html", context={"event":target, "ads":ads})



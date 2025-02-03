from django.shortcuts import render
from gestionPedidos.models import Articulos
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings

def articulos(request):
    articulos = Articulos.objects.all()
    return render(request,"articulos.html",{"articulos":articulos})

def RideSphere(request):
    return render(request,"RideSphere.html",{"proyecto":"Mi Proyecto"})

def  inicio(request):
    return render(request,"inicio.html",{"proyecto":"Mi Proyecto"})

def busqueda_productos(request):
    return render(request,"busqueda_productos.html")

def buscar (request):
    producto=request.GET.get('prd', '').strip()
    if producto:
        articulos=Articulos.objects.filter(nombre__icontains=producto)
        if articulos.exists():
            return render(request, "articulos.html", {"articulos":articulos, "mensaje": f"Resultados para '{producto}'"})
        else:
            return render(request, "busqueda_productos.html", {"mensaje": "NO SE ENCONTRARON ARTÍCULOS CON ESE NOMBRE."}) 
    else:
        #Si no se ingreso nada en el formulario
        return render(request, "busqueda_productos.html",{"mensaje":"Por favor ingrese un valor para buscar."})
                   
def contacto (request):
    if request.method =='POST':
        subject= request.POST["asunto"]
        message= request.POST["mensaje"]+""+ request.POST["email"]
        email_from =settings.EMAIL_HOST_USER
        recipient_list =["deadpolitojunior@gmail.com"]
        send_mail(subject, message, email_from, recipient_list)
        return render(request,"Gracias.html")
    return render(request,"contacto.html")


  
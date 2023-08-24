from django.shortcuts import render
from .models import PostHome
from django.shortcuts import render, redirect
from .forms import FormularioContacto
from django.core.mail import EmailMessage

# Create your views here.
def home(request):
    welcomes = PostHome.objects.all()
    formulario_contacto = FormularioContacto()

    if request.method == "POST":
        formulario_contacto = FormularioContacto(data=request.POST)
        if formulario_contacto.is_valid():
            nombre=request.POST.get("nombre")
            email=request.POST.get("email")
            contenido=request.POST.get("contenido")

            email=EmailMessage("Mensaje desde App Django",
            "El usuario de nombre {} con la direccion {} te escribe lo siguiente: \n\n {}".format(nombre,email,contenido),
            "",["olavafletes@gmail.com"], reply_to=[email])

            try:
                email.send()

                return redirect("/?valido")
            except:
                return redirect("/?novalido")


    return render(request, "OlavaFletesApp/home.html", {'miFormulario' : formulario_contacto, 'welcomes': welcomes})
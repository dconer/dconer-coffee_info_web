from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ContactForm
from django.core.mail import EmailMessage
# Create your views here.


def contact(request):
    # Crear la plantilla vacia
    contact_form = ContactForm()

    if request.method == "POST":
        # Si se envia los datos mediante post, se rellenara la plantilla
        # Con el objetivo de verificar los datos enviados
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')
            # sent t0 our test email
            email = EmailMessage(
                "La Caffetiera: Nuevo mensaje de contacto de la página web",
                body=f"De {name} <{email}>\n\nEscribió:\n\n{content}",
                from_email="no_contestar@imbox.mailtrap.io",
                to=["a20185061@pucp.edu.pe"],
                reply_to=[email]
            )
            try:
                email.send()
                return redirect(reverse('contact')+"?ok")  # /contact/?ok

            except:
                # /contact/?ok
                return redirect(reverse('contact')+"?fail_to_send_message")

    return render(request, 'contact/contact.html', {'form': contact_form})

from django.shortcuts import render,redirect
from django.conf import settings
from django.core.mail import send_mail,BadHeaderError
from django.http import HttpResponse,HttpResponseRedirect
from .forms import ContactForm


# Create your views here.

def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def post(request):
    return render(request,'post.html')

def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form_email = form.cleaned_data.get("email")
        form_message = form.cleaned_data.get("message")
        form_full_name = form.cleaned_data.get("full_name")
        subject = 'Site Contact form'
        from_email = settings.EMAIL_HOST_USER
        to_email = [form_email,from_email]  
        contact_message = "%s: %s via %s"%(
            form_full_name,
            form_message,
            form_email)

        try:
            send_mail(subject,contact_message,from_email,to_email)
        except BadHeaderError:
            return HttpResponse('Invalid header found!')
        return redirect('success')

    context = {"form":form,}

    return render(request,"contact.html",context)



def success(request):
    return render(request,'success.html')



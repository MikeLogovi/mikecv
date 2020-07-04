from django.shortcuts import render,redirect,HttpResponseRedirect,HttpResponse
from .models import *
from googletrans import Translator
from .forms import *
from django.contrib import messages
from django.utils.translation import gettext_lazy as _
t=Translator()
def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def resume(request):
    context={'rcategories':ResumeCategory.objects.all(),'scategories':SkillCategory.objects.all()}
    return render(request,'resume.html',context)

def certifications(request):
    certification_categories=CertificationCategory.objects.all
    context={'certification_categories':certification_categories}
    return render(request,'certifications.html',context)

def services(request):
    ser=Service.objects.all
    clients=Client.objects.all
    customers=Customer.objects.all
    context={'ser':ser,'clients':clients,'customers':customers}
    return render(request,'services.html',context)
    #return HttpResponse(services)
def portfolio(request):
    portfolios=Portfolio.objects.all
    context={'portfolios':portfolios}
    return render(request,'portfolio.html',context)

def contact(request):
    if request.method=='POST':
        next = request.POST.get('next', '/')
        form=Contact(request.POST)
        if form.is_valid():
            message= Message()
            message.name=request.POST['name']
            message.email=request.POST['email']
            message.comment=request.POST['comment']
            message.save()
            messages.success(request,_('Your message has been sent successfully.We will respond you soon'))
            return HttpResponseRedirect(next)
        else:
            return redirect('/')
    return render(request,'contact.html')
    
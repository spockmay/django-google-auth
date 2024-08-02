from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
def home_page_view(request):
    return HttpResponse("Hello, world!")

def home_page_template(request):
    return render(request=request,
            template_name='pages/main.html')

def login_template(request):
    return render(request=request,
            template_name='pages/login.html')

@login_required
def secret_template(request):
    return render(request=request,
            template_name='pages/secret.html')

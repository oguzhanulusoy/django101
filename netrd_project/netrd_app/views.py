from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='/error')
def test_view(request):
    user = User.objects.get(id=request.user.id)
    return HttpResponse("Kullanici adi = " + user.username)

def error_view(request):
    return HttpResponse('Kullanici login olmamis')


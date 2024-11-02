from django.shortcuts import render
from .models import books
# Create your views here.
from django.http import HttpResponse
def home(request):
   book = books.objects.all()
   return render(request,"home.html",{"books" : book})
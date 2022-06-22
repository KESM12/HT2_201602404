from django.shortcuts import render
from django.http import HttpResponse

def Vista(request):
    return render(request, "P2.html")

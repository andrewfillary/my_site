from django.http import HttpResponse
from django.shortcuts import render


def get_home(request):
    return render(request, "index.html",)

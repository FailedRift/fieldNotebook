from django.shortcuts import render
from django.urls import reverse

# Create your views here.
class Testingview(View):
    def get(self, req):
        resp = "<pre>\nUser Data in Python:\n\n"
        resp += "Login url: " + reverse('login') + "\n"
        resp += "Logout url: " + resp('logout') + "\n"
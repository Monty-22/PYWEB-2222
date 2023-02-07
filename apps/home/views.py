

from django.shortcuts import render
from django.views import View


class IndexShopView(View):
   def get(self, request):
       return render(request, 'home/index.html')

class AboutShopView(View):
   def get(self, request):
       return render(request, 'home/about.html')

class ContactShopView(View):
   def get(self, request):
       return render(request, 'home/contact.html')



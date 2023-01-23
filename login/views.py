from django.shortcuts import render
from django.http import JsonResponse
from datetime import datetime

from django.views import View
from django.http import HttpResponse


class IndexView(View):
    def get(self, request):
        return render(request, 'login/index.html')

class LoginView(View):
    def get(self, request):
        return  render(request, 'index.html')

    def post(self,request):
        return JsonResponse(request.Post, json_dumps_params={'indent': 4})
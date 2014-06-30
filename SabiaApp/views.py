from django.shortcuts import render_to_response
from SabiaApp.models import *

from django.http import HttpResponse

def inicio(request):  
    return render_to_response('index.html')

def main_page(request):  
    return render_to_response('main_page.html')
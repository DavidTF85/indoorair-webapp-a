from django.http import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse


def index(request):

    return render(request,"homepage/index.html",{},)

def contact_page(request):

    return render(request,"homepage/contact.html",{},)

def get_version_api(request):

    return JsonResponse({'version': 'EVA-00'})

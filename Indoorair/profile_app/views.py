from django.shortcuts import render
from django.http import JsonResponse

def retrieve_profile_page(request):
    return render(request, "profile_app/retrieve.html",{},)

def update_profile_page(request):
    return render(request, "profile_app/update.html",{},)
def update_profile_api(request):

  return JsonResponse({

       })
def retrieve_profile_api(request):

  return JsonResponse({

       })

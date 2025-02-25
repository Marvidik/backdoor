from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from .models import ModelStatus

def ping(request):
    # Assuming there's only one instance of ModelStatus
    model_status = ModelStatus.objects.first()
    
    if model_status and model_status.is_active:
        return JsonResponse({"message": "Pong!"}, status=200)
    else:
        return JsonResponse({"error": "Forbidden"}, status=403)
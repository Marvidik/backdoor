from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ModelStatus  # Adjust the import based on your project structure

class PingView(APIView):
    def get(self, request):
        # Assuming there's only one instance of ModelStatus
        model_status = ModelStatus.objects.first()
        
        if model_status and model_status.is_active:
            return Response({"message": "Pong!"}, status=status.HTTP_200_OK)
        else:
             return Response({"error": "Model is inactive"}, status=status.HTTP_226_IM_USED) 
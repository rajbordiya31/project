from django.contrib.auth import authenticate
from .jwtapp import generate
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json

@csrf_exempt

def login_page(request):
    if request.method == "POST":
        data= json.loads(request.body)
        username = data.get("username")
        password = data.get("password")
        
        user = authenticate(username=username,password=password)

        if user is not None:
            payload = {
                "user_id" : user.id,
                "username":username
            }

            token = generate(payload)
            return JsonResponse({"token":token})
        else:
            return JsonResponse({"Error":"Invalid credentials"})
        
    return JsonResponse({"error": "Invalid request method"})
        

from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Staff                                         

@csrf_exempt
def Staff_Login(request):
    if request.method=='POST':
        try:
            data = json.loads(request.body)
            username = data.get("UserName")
            password = data.get("UserPassword")
            if not username or not password:
                return JsonResponse({"success": False, "message": "username and password are required"}, status=400)
        
            try:
                user = Staff.objects.get(UserName=username)
            except Staff.DoesNotExist:
                return JsonResponse({"success": False, "message": "User not found"}, status=404)

            if password != user.UserPassword:
                return JsonResponse({"success": False, "message": "Invalid password"}, status=401)

            return JsonResponse({"success": True, "message": "Login successful"}, status=200)

        except json.JSONDecodeError as e:
            return JsonResponse({"success": False, "message": "Invalid JSON", "details": str(e)}, status=400)

    return JsonResponse({"success": False, "message": "Only POST requests are allowed"}, status=405)

    x
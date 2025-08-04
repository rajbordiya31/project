from django.shortcuts import render

# Create your views here.
from .models import Student
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .authenticate import token_required


@csrf_exempt
@token_required

def add_student(request):
    if request.method == "POST":
        try:
            data =json.loads(request.body)
            student = Student(
                name=data.get("name"),
                age=data.get("age"),
                mob=data.get("mob")
            )
            student.save()
            return JsonResponse({"message": "Student added successfully"})
        except Exception as e:
            return JsonResponse({"error": str(e)})
    return JsonResponse({"error": "Invalid request method"})

@token_required
def get_student(request):
    
    if request.method == "GET":
        try:
            student = Student.objects.all().values()
            return JsonResponse(list(student),safe=False)
        except Exception as e:
            return JsonResponse({"error":str(e)})

@csrf_exempt
@token_required

def update_data(request,id):
    if request.method =="PUT":
        try:
            student = Student.objects.get(id=id)
            data=json.loads(request.body)
            student.name =data.get("name",student.name)
            student.age = data.get("age",student.age)
            student.mob=data.get("mob",student.mob)
            student.save()
            return JsonResponse({"Message":"Updated Successfully"})
        except Student.DoesNotExist:
            return JsonResponse({"Message" : "Student doesnot exist"})
        
        except Exception as e:
            return JsonResponse({"Error":str(e)})
        
@csrf_exempt
@token_required

def delete_data(request,id):
    if request.method == "DELETE":
        try:
            student = Student.objects.get(id=id)
            student.delete()
            return JsonResponse({"message": "Student deleted successfully"})
        except Student.DoesNotExist:
            return JsonResponse({"error": "Student not found"})
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
    return JsonResponse({"error": "Invalid request method"})
        






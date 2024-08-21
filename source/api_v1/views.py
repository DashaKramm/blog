import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
@csrf_exempt
def calculate(request, operation):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            A = float(data.get("A"))
            B = float(data.get("B"))
            if operation == "add":
                result = A + B
            elif operation == "subtract":
                result = A - B
            elif operation == "multiply":
                result = A * B
            elif operation == "divide":
                if B == 0:
                    raise ZeroDivisionError("Division by zero!")
                result = A / B
            else:
                return JsonResponse({"error": "Invalid operation!"}, status=400)
            return JsonResponse({"answer": result})
        except (TypeError, ValueError):
            return JsonResponse({"error": "Inputs must be valid numbers!"}, status=400)
        except ZeroDivisionError as e:
            return JsonResponse({"error": str(e)}, status=400)

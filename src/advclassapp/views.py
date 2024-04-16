from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

@csrf_exempt
def checkindex(request):
    print("custom request data", request.custom_data)
    raise Exception("exception raised from the views")
    return JsonResponse({"message":"request data verified succesfully"})

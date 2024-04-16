from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

@csrf_exempt
def checkindex(request, operation=None):
    print("custom request data", request.custom_data)
    if request.operation == 'update':
        raise Exception("exception raised from the views")
    return JsonResponse({"message":"request data verified succesfully"})

"""output""" #{"number":2}
{"msg": "exception raised from the views"}
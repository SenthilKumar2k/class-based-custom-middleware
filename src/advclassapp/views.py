from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http import JsonResponse
from rest_framework.views import APIView
import pdb

# @csrf_exempt
# def checkindex(request, operation=None):
#     print("custom request data", request.custom_data)
#     # pdb.set_trace()
#     if request.operation == 'update':
#         raise Exception("exception raised from the views")
#     return JsonResponse({"message":"request data verified succesfully"})

"""output""" #{"number":2}
#{"msg": "exception raised from the views"}

#@csrf_exempt
class CheckIndexView(APIView):
    def get(self, request, *args, **kwargs):
        print("custom request data", request.custom_data)
        # pdb.set_trace()
        if request.operation == 'update':
            raise Exception("exception raised from the views")
        return JsonResponse({"message":"request data verified succesfully"})


from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

@csrf_exempt
def index(request):
    print("index call",request.POST)
    return JsonResponse({'message':'set request data succesfully'})


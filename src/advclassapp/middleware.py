import json
from django.http import JsonResponse, HttpResponse

class Checkrequestdata:
    def __init__(self, get_response):
        self.get_response=get_response
    def __call__(self, request):
        print(f"request data={request.body}")
        try:
            data=json.loads(request.body)
            number=data.get('number')
            if number and int(number)%2:
                return JsonResponse({"message":"failed from the middleware"})
        except json.JSONDecodeError:
            return JsonResponse({"message":"invalid json data format"})
        request.custom_data={"data":number}
        print("start check request data")
        response=self.get_response(request)
        print("end check request data")
        return response

    def process_view(request, view_fun, *args , **kwargs):
        # This is called after Djagno figures which view to call
        # but this is called before the view is called.
        print("process view of check even")
        #return JsonResponse({"msg" : "Returned from the Django middleware CheckEvent's process_view"})
        #return HttpResponse("Returned from the Django middleware CheckEvent's process_view")
        return None
    
    def process_exception(self, request, exception):
        print("checkeven exception")
        msg=str(exception)
        return JsonResponse({"msg":msg},status=400)
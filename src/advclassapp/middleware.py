import json
import inspect
from django.http import JsonResponse, HttpResponse
from .views import CheckIndexView

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

    def process_view(self,request, view_func, *args , **kwargs):
        # This is called after Djagno figures which view to call
        # but this is called before the view is called.
        print("process view of check even")
        print(view_func.__class__.__name__)
        #if view_func.__class__.__name__=='CheckIndexView':
        if inspect.isclass(view_func) and issubclass(view_func, CheckIndexView)
            print("process view of check view name")
            number=request.custom_data.get('data')
            print(number)
            if number is not None and int(number) % 2==0:
                request.operation='update'

        #return JsonResponse({"msg" : "Returned from the Django middleware CheckEvent's process_view"})
        #return HttpResponse("Returned from the Django middleware CheckEvent's process_view")
        return None
    
    def process_exception(self, request, exception):
        print("checkeven exception")
        msg=str(exception)
        return JsonResponse({"msg":msg},status=400)
    

"""input"""
#raw json  {"number":2}


"""output"""
# request data=b'{\n"number":2\n}'
# start check request data
# process view of check even
# process view of check view name
# 2
# custom request data {'data': 2}
# checkeven exception
# end check request data
# Bad Request: /checkdata/
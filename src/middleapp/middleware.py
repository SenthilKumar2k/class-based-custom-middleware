import json

# class Setrequestdata:
#     def __init__(self, get_response):
#         print('setrequest data initalized')
#         self.get_response=get_response
#     def __call__(self, request):
#         print(f'request.post={request.POST}')
#         data=request.POST.get('number')
#         request.POST={'data':data}
#         print('start of set request data')
#         response=self.get_response(request)
#         print('end of set request')
#         return response


"""input"""
#form-data  key=number value=2

"""output"""
# setrequest data initalized
# request.post=<QueryDict: {'number': ['2']}>
# start of set request data
# index call {'data': '2'}
# end of set request

class Setrequestdata:
    def __init__(self, get_response):
        print("set request data intitalized")
        self.get_response=get_response
    def __call__(self, request):
        print(f"request data={request.body}")
        data=json.loads(request.body)
        number=data.get('number')
        request.custom_data={'data':number}
        print("start set request data")
        response=self.get_response(request)
        print("end set request data")
        return response
    

"""input"""
#raw json  {"number":2}
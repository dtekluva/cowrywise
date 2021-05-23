from django.http.response import HttpResponse
from main.models import *
import json


# Create your views here.

def make(request):

    if request.method == 'GET':
        task = UUID.create_new_uuid()
        
        data = UUID.get_all().get("uuids")

        response = json.dumps(data)
        return HttpResponse(response, content_type="application/json", status= 201)

    else:
        data = {
        'status' : False,
        'message' : 'Unsuccessful'
    }
        response = json.dumps(data)

        return HttpResponse(response, content_type="application/json", status= 201)
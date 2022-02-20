from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
import utils
from django.conf import settings


# Create your views here.
def index(request: HttpRequest):
    collection = utils.get_db_handle(settings.MONGO_USERNAME, settings.MONGO_PASSWORD)

    results = collection.find()
    s = 'You have these ids:<br><br>'
    print('find: get all')
    for r in results:
        s += 'id: ' + str(r['_id']) + '<br>'
        print(r)
        print(r['_id'])
    return HttpResponse(s)

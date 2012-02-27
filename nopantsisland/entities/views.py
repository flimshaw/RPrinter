from django.http import HttpResponse
from django.shortcuts import render_to_response
from models import Entity
import time, datetime

def test(request):
    t = datetime.datetime.utcnow()
    ohnow = time.mktime(t.timetuple())
    entities = Entity.objects.raw_query({ 
            'created_on' : {'$lte': t}, 
            'data.type' : 'message', 
            'data.nick' : {'$in': ['ashley', 'choey']}
            })[:500]
    return render_to_response('entities/test.html', {'entities': entities})

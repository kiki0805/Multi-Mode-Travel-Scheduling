from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.utils.encoding import smart_str, smart_unicode
from scheme.service import AmapService


def scheme(request):
    if request.META.has_key('HTTP_X_FORWARDED_FOR'):  
        ip =  request.META['HTTP_X_FORWARDED_FOR']  
    else:  
        ip = request.META['REMOTE_ADDR']  
    print AmapService(ip)
    data = request.GET
    data = request.body
    origin =  data['origin']
    destination = data['destination']
    mode_id = data['mode_id']
    duration = data['duration']
    begin_time = data['begin_time']
    end_time = data['end_time']
    return JsonResponse(data)

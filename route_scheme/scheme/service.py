from tags.models import Tag
from accounts.models import UserProfile
from accounts.serializers import UserProfileSerializer
import requests

class AmapService(object):
    key = "c2764dad2a322cf712ed630b82d44ad6"
    @classmethod
    def get_adcode_from_ip(cls, ip):
        url = "http://restapi.amap.com/v3/ip?"
        parameters = "key=%s&ip=%s" % (cls.key, ip)
        url += parameters
        res = requests.get(url,)
        print parameters

        

    @classmethod
    def get_weather(cls, ip):
        url = "http://restapi.amap.com/v3/weather/weatherInfo?"
        adcode = cls.get_adcode_from_ip(ip)
        parameters = "key=%s&adcode=%s" % (cls.key, adcode)
        url += parameters
        users = UserProfileSerializer(UserProfile.objects.all(), many=True).data
        user = UserProfileSerializer(user.profile).data
        print users, user
        # user = UserProfileSerializer(data=)
        # user.save()

#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
import requests
import json

class AmapService(object):
    key = "c2764dad2a322cf712ed630b82d44ad6"

    mode = {
        '1':'walking',
        '2':'transit',
        '3':'driving',
        '4':'bicycling',
        '5':['walking',2],
    }

    @classmethod
    def get_adcode_from_ip(cls, ip):
        url = "http://restapi.amap.com/v3/ip"
        payload = {'key':cls.key, 'ip':ip}

        res = requests.get(url, params=payload).json()
        if res['status']=='1':
            return res['adcode']
        else:
            return ''

    @classmethod
    def get_weather(cls, adcode):
        url = "http://restapi.amap.com/v3/weather/weatherInfo"
        payload = {'key': cls.key, 'city': adcode, 'extensions': 'base'}
        res = requests.get(url, params=payload).json()
        if res['status']=='1':
            info = res['lives'][0]
            if info['weather'] not in [u'晴',u'多云',u'阴',u'阵雨',u'小雨']:
                return 0 # 0 不适合徒步骑行
            elif (int(info['temperature'])<0 or int(info['temperature'])>33):
                return 0
            else:
                return 1 # 都能选择

        else:
            return '' # 请求错误

    @classmethod
    def get_route(cls,mode,origin, destination, city): # origin
        if mode =='1': # walking
            url = 'http://restapi.amap.com/v3/direction/'+cls.mode['1']
            payload = {
                'key':cls.key,
                'origin':str(origin[0])+','+str(origin[1]),
                'destination':str(destination[0])+','+str(destination[1]),
            }

            res = requests.get(url, params = payload).json()
            if res['status']=='1':
                duration = int(res['route']['paths'][0]['duration'])
                distance = int(res['route']['paths'][0]['distance'])
                cost = 0

                res = {
                    'duration':duration,
                    'distance':distance,
                    'cost':cost,
                }

                return res
            else:
                return ''

        if mode=='2': # 换成公交或者地铁
            url = 'http://restapi.amap.com/v3/direction/'+cls.mode['2']+'/integrated'
            payload = {
                'key':cls.key,
                'origin':str(origin[0])+','+str(origin[1]),
                'destination':str(destination[0])+','+str(destination[1]),
                'city':str(city),
            }

            res = requests.get(url, params = payload).json()

            print res
            if res['status']=='1':
                cost = float(res['route']['taxi_cost'])
                distance = float(res['route']['distance'])
                duration = 0
                for i in res['route']['transits']:
                    duration = duration + float(i['duration'])

                res = {
                    'duration':duration,
                    'distance':distance,
                    'cost':cost,
                }

                return res
            else:
                return ''

        if mode=='3':
            url = 'http://restapi.amap.com/v3/direction/'+cls.mode['3']
            payload = {
                'key':cls.key,
                'origin':str(origin[0])+','+str(origin[1]),
                'destination':str(destination[0])+','+str(destination[1]),
            }

            res = requests.get(url, params = payload).json()

            if res['status']=='1':
                duration = int(res['route']['paths'][0]['duration'])
                distance = int(res['route']['paths'][0]['distance'])
                cost = 0

                res = {
                    'duration':duration,
                    'distance':distance,
                    'cost':cost,
                }

                return res

            else:
                return ''

        if mode=='4':
            url = 'http://restapi.amap.com/v4/direction/'+cls.mode['4']
            payload = {
                'key':cls.key,
                'origin':str(origin[0])+','+str(origin[1]),
                'destination':str(destination[0])+','+str(destination[1]),
            }

            res = requests.get(url, params = payload).json()


            if res:
                duration = int(res['data']['paths'][0]['duration'])
                distance = int(res['data']['paths'][0]['distance'])
                cost = 0

                res = {
                    'duration':duration,
                    'distance':distance,
                    'cost':cost,
                }

                return res
            else:
                return ''

        if mode=='5':
            url = 'http://restapi.amap.com/v3/direction/'+cls.mode['5'][0]
            payload = {
                'key':cls.key,
                'origin':str(origin[0])+','+str(origin[1]),
                'destination':str(destination[0])+','+str(destination[1]),
            }

            res = requests.get(url, params = payload).json()

            if res['status']=='1':
                res['route']['paths'][0]['duration'] = str(cls.mode['5'][1] * int(res['route']['paths'][0]['duration']))

                duration = int(res['route']['paths'][0]['duration'])
                distance = int(res['route']['paths'][0]['distance'])
                cost = 0

                res = {
                    'duration':duration,
                    'distance':distance,
                    'cost':cost,
                }



                return res
            else:
                return ''

    @classmethod
    def findLocation(cls,keyword,midpoint):
        url = 'http://restapi.amap.com/v3/place/around'

        payload = {
            'key':cls.key,
            'location':str(midpoint[0])+','+str(midpoint[1]),
            'extensions':'base',
            'keywords':keyword,
        }

        res = requests.get(url, params = payload).json()
        if res['status'] == '1':
            if res['pois']:
                location = res['pois'][0]['location'].split(',')
                location = [float(i) for i in location]
                name = res['pois'][0]['name']

                res = {
                    'location':location,
                    'name':name
                }
                return res



        else:
            return ''


amap = AmapService();
# print amap.get_adcode_from_ip('119.20.11.1')
print amap.get_weather('110101')
print amap.get_route('5',[116.434307,39.90909],[116.534446,39.90916],'北京')
print amap.findLocation('肯德基',[116.434307,39.90909])

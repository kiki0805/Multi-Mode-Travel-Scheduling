import recommend
from testapi import AmapService


def route_generator(origin, desination, user_tags, total_time):
    r_tags = recommend.recommend(user_tags)
    r_location = []
    waypoints = []
    # get recommend location
    for tag in r_tags:
        r_location.append(AmapService.findLocation(tag, [(origin[0] + desination[0])/2, (origin[1] + desination[1])/2]))

    # suppose in every location we spend 1 hour    
    temp_duration = AmapService.get_route('3',origin, r_location[0]['location'],'上海')['duration'] + AmapService.get_route('3', r_location[0]['location'], desination,'上海')['duration'] + 3600    
    if temp_duration < total_time:
        waypoints.append(r_location[0])
    
    temp_duration = AmapService.get_route('3',origin, r_location[0]['location'],'上海')['duration'] + AmapService.get_route('3', r_location[0]['location'], r_location[1]['location'],'上海')['duration'] + AmapService.get_route('3', r_location[1]['location'], desination,'上海')['duration'] + 3600*2
    if temp_duration < total_time:
        waypoints.append(r_location[1])

    temp_duration = AmapService.get_route('3',origin, r_location[0]['location'],'上海')['duration'] + AmapService.get_route('3', r_location[0]['location'], r_location[1]['location'],'上海')['duration'] + AmapService.get_route('3', r_location[1]['location'], r_location[2]['location'],'上海')['duration'] + AmapService.get_route('3', r_location[2]['location'], desination,'上海')['duration'] + 3600*3
    if temp_duration < total_time:
        waypoints.append(r_location[2])


    temp_duration = AmapService.get_route('3',origin, r_location[0]['location'],'上海')['duration'] + AmapService.get_route('3', r_location[0]['location'], r_location[1]['location'],'上海')['duration'] + AmapService.get_route('3', r_location[1]['location'], r_location[2]['location'],'上海')['duration'] + AmapService.get_route('3', r_location[2]['location'], r_location[3]['location'],'上海')['duration'] + AmapService.get_route('3', r_location[3]['location'], desination,'上海')['duration'] + 3600*4
    if temp_duration < total_time:
        waypoints.append(r_location[3])


    temp_duration = AmapService.get_route('3',origin, r_location[0]['location'],'上海')['duration'] + AmapService.get_route('3', r_location[0]['location'], r_location[1]['location'],'上海')['duration'] + AmapService.get_route('3', r_location[1]['location'], r_location[2]['location'],'上海')['duration'] + AmapService.get_route('3', r_location[2]['location'], r_location[3]['location'],'上海')['duration'] + AmapService.get_route('3', r_location[3]['location'], r_location[4]['location'],'上海')['duration'] + AmapService.get_route('3', r_location[4]['location'], desination,'上海')['duration'] + 3600*5
    if temp_duration < total_time:
        waypoints.append(r_location[4])
    
    print(waypoints)

#TEST
route_generator([116.434307,39.90909],[116.534446,39.90916],set(['KTV','桌游店','游乐场','体育场','体育馆']), 36000)

    
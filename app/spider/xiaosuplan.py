import requests
import json
from flask import jsonify

def location_encode(location):
    location_request = requests.get(
                                    f'https://restapi.amap.com/v3/geocode/geo?'
                                    f'address={location}&output=JSON'
                                    f'&key=cadfefb3243a9a8c45140bc96e82e0d3'
                                   )
    location_dict = location_request.json()
    location_code = location_dict['geocodes'][0]['location']
    return location_code

def route_plan(src, dest):
    src_code = location_encode(src)
    dest_code = location_encode(dest)
    res = requests.get(
                        f'https://restapi.amap.com/v3/direction/transit/integrated'
                        f'?key=cadfefb3243a9a8c45140bc96e82e0d3&extensions=all&'
                        f'origin={src_code}&destination={dest_code}&city=010&output=JSON&strategy=0'
                      )
    route_list = []
    re = res.json()
    if int(re['status']) == 1:
        if re['route']['transits']:
            transit = re['route']['transits'][0]#只截取第一条线路
            for route in transit['segments']:
                if route['bus']['buslines']:
                    route_list.append(route['bus']['buslines'][0]['name'])
            time = dict(duration=transit['duration'])
            route_list.append(time)
        else:
            print("no way")
    else:
        print('error', src, dest)
    return route_list

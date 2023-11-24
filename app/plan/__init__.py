from app.spider.xiaosuplan import route_plan
from app.libs.error_code import Error
from app.attractions.lanuage_revert import chinese_to_english, english_to_chinese
from app.models.njlink import NJLink
from itertools import permutations
from math import ceil
import json

class Plan:
    INF = 100000000
    max_perday = 4
    min_perday = 2
    @staticmethod
    def dict_slice(dict, number):
        dict_slice = {}
        keys = dict.keys()
        for k in list(keys)[0:number]:
            # print('字典截取',k)
            dict_slice[k] = dict[k]
        return dict_slice
    @staticmethod
    def artificial_deep_clone(src_list):
        dest_list = [x for x in range(0, len(src_list))]
        for x in range(0, len(src_list)):
            dest_list[x] = src_list[x]
        return dest_list


    def __init__(self, day, attractions_await, src):
        self.day = day
        self.is_reasonable = True
        self.attractions_origin = Plan.artificial_deep_clone(attractions_await)
        self.attractions_await = attractions_await
        self.attractions_await_english = [chinese_to_english[name] for name in attractions_await]
        self.src = src
        self.final_arrange = []

    def __judge_time(self):
        attractions_perday = len(self.attractions_await) / self.day
        if attractions_perday > Plan.max_perday or attractions_perday < Plan.min_perday:
            self.is_reasonable = False
            raise Error("时间不合理")

    def arrange_attractions_perday(self):#一开始先向上取整看最后一天的安排情况 再向下取整看最后一天安排的情况
        total = len(self.attractions_await)
        number_perday = [x for x in range(0, self.day)]
        up_last_day = total - (ceil(total / float(self.day)) * (self.day - 1))
        low_last_day = total - int(total / self.day) * (self.day - 1)
        if up_last_day <= 4 and up_last_day >= 2:
            for x in range(0, self.day - 1):
                number_perday[x] = ceil(total / float(self.day))
            number_perday[x + 1] = up_last_day
        elif low_last_day <= 4 and low_last_day >= 2:
            for x in range(0, self.day - 1):
                number_perday[x] = int(total / self.day)
            number_perday[x + 1] = low_last_day
        return number_perday

    def search_for_closest(self, src):
        min_duration = Plan.INF
        attractions_perday = []
        for attraction in self.attractions_await:
            route_and_duration = route_plan(src, attraction)
            duration = route_and_duration[-1]['duration']
            if int(duration) < int(min_duration):
                min_duration = duration
                closest_route = route_and_duration
                closest_route.append({'src_name': src, 'destination_name': attraction })
        closest_attraction_name = closest_route[-1]['destination_name']
        attractions_perday.append(closest_route)
        self.final_arrange.append(attractions_perday)
        self.attractions_await.remove(closest_attraction_name)
        self.attractions_await_english.remove(chinese_to_english[closest_attraction_name])
        return closest_attraction_name

    def involve_node(self, link_dict, number):
        dict_sorted = {k: v for k, v in sorted(link_dict.items(), key=lambda item: item[1][-1]['duration'])}
        attractions_already = Plan.dict_slice(dict_sorted, number)
        keys = list(attractions_already.keys())
        for key in keys:
            name = key[3:]
            self.attractions_await.remove(english_to_chinese[name])
            self.attractions_await_english.remove(name)
        return [key[3:] for key in list(attractions_already.keys())]

    def __mid__arrange(self):#给出出发点到第一个点的情况，再给出每天应该包括的景点
        mid_arrange = []#景点安排到每一天的情况
        self.__judge_time()
        number_perday = self.arrange_attractions_perday()
        for x in range(0, self.day):
            closest_attraction_name = self.search_for_closest(self.src[x]['srcName'])
            link = NJLink.query.filter_by(src=chinese_to_english[closest_attraction_name]).first()
            link.to_dict(self.attractions_await)
            attractions_already = self.involve_node(link.dict, number_perday[x]-1)
            attractions_already.insert(0, chinese_to_english[closest_attraction_name])
            attractions_already.insert(0, self.src[x]['srcName'])
            mid_arrange.append(attractions_already)
        return mid_arrange

    def judge_duration(self, src, destination_list, min_duration):
        duration = 0
        temp_arrange = []
        link = NJLink.query.filter_by(src=src).first()
        link.to_dict(self.attractions_origin)
        src_dict = link.dict
        for destionation in destination_list:
            destionation_key = 'to_'+destionation
            src_dict[destionation_key].append({'src_name': english_to_chinese[src],'destination_name': english_to_chinese[destionation]})
            temp_arrange.append(src_dict[destionation_key])
            duration += int(src_dict[destionation_key][-2]['duration'])
            link = NJLink.query.filter_by(src=destionation).first()
            link.to_dict(self.attractions_origin)
            src_dict = link.dict
            src = destionation
        return duration, temp_arrange

    def arrange(self):
        index = 0
        mid_arrange = self.__mid__arrange()
        # print('已经安排好了的', self.final_arrange)
        for attractions_perday in mid_arrange:
            full_arrange_await = attractions_perday[2:]
            full_arrange_ready = list(permutations(full_arrange_await, len(full_arrange_await)))
            min_duration = Plan.INF
            for singular_list in full_arrange_ready:
                duration, temp_arrange = self.judge_duration(attractions_perday[1], singular_list, min_duration)
                if duration < min_duration:
                    best_arrange = temp_arrange
                    min_duration = duration
            # print('最好的安排', best_arrange)
            for per_arrange in best_arrange:
                self.final_arrange[index].append(per_arrange)
            index = index + 1
        print('final_arrange----------------->', self.final_arrange)
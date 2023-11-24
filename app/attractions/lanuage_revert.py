from math import ceil
from itertools import permutations
chinese_to_english = {
                      '南京中山陵': 'sunyatsen_mausoleum', '南京明孝陵': 'mingxiaolin_mausoleum',
                      '南京牛首山': 'niushoushan', '南京大报恩寺': 'dabaoen_temple', '南京红山森林动物园': 'hongshan_forest_zoo',
                      '南京钟山风景名胜区': 'zhongshan_scenic_area', '南京栖霞山': 'qixiashan', '南京银杏湖乐园': 'ginkgo_lake_paradise',
                      '南京秦淮河': 'qinhuai_river', '南京玄武湖':'xuanwu_lake', '南京博物院': 'nanjin_museum',
                      '南京方山': 'fangshan', '南京明城墙': 'ming_dynasty_city_wall', '南京百家湖': 'baijia_lake',
                      '南京新街口': 'xinjiekou', '南京大屠杀遇难同胞纪念馆': 'nanjing_massacre_memorial_and_museum',
                      '南京欢乐谷': 'nanjing_happy_valley', '南京眼': 'nanjing_eye', '南京老门东': 'laomendong',
                      '南京海底世界': 'nanjing_underwater_world', '南京瞻园': 'zhanyuan',
                      '南京大学鼓楼校区': 'nju_gl', '南京林业大学': 'nfu', '南京航空航天大学明故宫校区': 'nuaa_mgg',
                      '南京东南大学四牌楼校区': 'seu_spl', '南京天印湖': 'tianyin_lake','南京夫子庙': 'confucian_temple'
                      }
english_to_chinese = dict([(value,key) for (key,value)in chinese_to_english.items()])


# def arrange_attractions_perday(total, day):
#     number_perday = [x for x in range(0,day)]
#     up_last_day = total - (ceil(total / float(day)) * (day - 1))
#     low_last_day = total - int(total / day) * (day - 1)
#     if up_last_day <= 4 and up_last_day >= 2:
#         for x in range(0, day - 1):
#             # print(x)
#             # print(ceil(total / float(day)))
#             number_perday[x] = ceil(total / float(day))
#         number_perday[x+1] = up_last_day
#     elif low_last_day <= 4 and low_last_day >= 2:
#         for x in range(0, day - 1):
#             number_perday[x] = int(total / day)
#         number_perday[x+1] = low_last_day
#     return number_perday

# res = arrange_attractions_perday(9,3)
# print(res)


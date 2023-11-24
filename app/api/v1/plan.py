from app.libs.redprint import Redprint
from flask import request
from flask import jsonify
from app.models.base import db
from app.models.traveller import Traveller
from app.libs.error_code import Error
from app.spider.xiaosuplan import route_plan
from app.plan import Plan
api = Redprint('plan')

@api.route('/arrange', methods=['POST'])
def plan_arrange():
    travel_day = request.json['time']
    travel_attractions = request.json['attractions']
    travel_src = request.json['srcArray']
    plan = Plan(travel_day, travel_attractions, travel_src)
    plan.arrange()
    return jsonify(plan.final_arrange)
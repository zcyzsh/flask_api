from app.libs.redprint import Redprint
from flask import request
from flask import jsonify
import json
from app.models.base import db
from app.models.njlink import NJLink
from app.models.traveller import Traveller
from app.libs.error_code import Error
from app.spider.xiaosuplan import route_plan
from app.attractions import attractionsOfCities
from app.models.base import db
api = Redprint('sudo')

@api.route('/addplan', methods=['GET'])
def add():
    for src in attractionsOfCities['njc']:
        link = NJLink()
        link.src = src['english_name']
        for dest in attractionsOfCities['njc']:
            if src['chinese_name'] != dest['chinese_name']:
                result = route_plan(src['chinese_name'], dest['chinese_name'])
                setattr(link, 'to_'+dest['english_name'], json.dumps(result))

                print(len(json.dumps(result)))
        with db.auto_commit():
            db.session.add(link)
    return 'success'
@api.route('/testplan', methods=['GET'])
def test():
    link = NJLink.query.filter_by(src="confucian_temple").first()
    print(json.loads(link.to_sunyatsen_mausoleum))
    print(type(json.loads(link.to_sunyatsen_mausoleum)))
    return link.to_sunyatsen_mausoleum
from app.models.base import db, Base
from sqlalchemy import Column, Integer, String, Float, Boolean
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import login_manager
from flask import current_app
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from math import floor
from app.libs.enums import PendingStatus
from app.libs.error_code import Error
from app.attractions.lanuage_revert import chinese_to_english
import json


class NJLink(Base):
    id = Column(Integer, primary_key=True)
    src = Column(String(62))
    to_confucian_temple = Column(String(500), default='未知')
    to_sunyatsen_mausoleum = Column(String(500), default='未知')
    to_mingxiaolin_mausoleum = Column(String(500), default='未知')
    to_niushoushan = Column(String(500), default='未知')
    to_dabaoen_temple = Column(String(500), default='未知')
    to_hongshan_forest_zoo = Column(String(500), default='未知')
    to_zhongshan_scenic_area = Column(String(500), default='未知')
    to_qixiashan = Column(String(500), default='未知')
    to_ginkgo_lake_paradise = Column(String(500), default='未知')
    to_qinhuai_river = Column(String(500), default='未知')
    to_xuanwu_lake = Column(String(500), default='未知')
    to_nanjin_museum = Column(String(500), default='未知')
    to_fangshan = Column(String(500), default='未知')
    to_ming_dynasty_city_wall = Column(String(500), default='未知')
    to_baijia_lake = Column(String(500), default='未知')
    to_xinjiekou = Column(String(500), default='未知')
    to_nanjing_massacre_memorial_and_museum = Column(String(500), default='未知')
    to_nanjing_happy_valley = Column(String(500), default='未知')
    to_nanjing_eye = Column(String(500), default='未知')
    to_laomendong = Column(String(500), default='未知')
    to_nanjing_underwater_world = Column(String(500), default='未知')
    to_zhanyuan = Column(String(500), default='未知')
    to_nju_gl = Column(String(500), default='未知')
    to_nfu = Column(String(500), default='未知')
    to_nuaa_mgg = Column(String(500), default='未知')
    to_seu_spl = Column(String(500), default='未知')
    to_tianyin_lake = Column(String(500), default='未知')

    def to_dict(self, attractions_await):
        self.dict = {}
        for key in attractions_await:
            key_english = 'to_'+chinese_to_english[key]
            if key_english != 'to_'+self.src:
                try:
                    self.dict[key_english] = json.loads(self.__dict__[key_english])
                except:
                    print(key)
                    raise Error('序列化失败')
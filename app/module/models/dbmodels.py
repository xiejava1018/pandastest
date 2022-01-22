# -*- coding: utf-8 -*-
"""
    :author: XieJava
    :url: http://ishareread.com
    :copyright: © 2019 XieJava <xiejava@ishareread.com>
    :license: MIT, see LICENSE for more details.
"""
from app.exts import db

class StaffInfo(db.Model):
    __tablename__='staff'
    staff_id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    staff_name=db.Column(db.String(64))
    staff_age=db.Column(db.String(2))
    staff_gender=db.Column(db.String(2))
    staff_salary=db.Column(db.String(255))
    staff_depatment_id=db.Column(db.String(2))

    def __repr__(self):
        return '<StaffInfo %r,staff_name:%s>' % (self.staff_id,self.staff_name)
        StaffInfo.metadata.drop_all()
        StaffInfo.metadata.create_all()

    def to_json(self):
        """将实例对象转化为json"""
        item = self.__dict__
        if "_sa_instance_state" in item:
            del item["_sa_instance_state"]
        return item

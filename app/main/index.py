# -*- coding: utf-8 -*-
"""
    :author: XieJava
    :url: http://ishareread.com
    :copyright: © 2019 XieJava <xiejava@ishareread.com>
    :license: MIT, see LICENSE for more details.
"""
import json
from flask import render_template, flash, redirect, url_for, request, current_app, Blueprint, abort, make_response, \
    jsonify
from app.module.models.dbmodels import StaffInfo

from app.exts import db
index_bp=Blueprint('index',__name__)

@index_bp.route('/',methods=['GET'])
def index():
    return 'hello'


@index_bp.route('/getstaff',methods=['GET'])
def getstaff():
    staffInfo=StaffInfo();
    staffs=staffInfo.query.all()
    staff_list=[]
    for staff in staffs:
        staff_list.append(staff.to_json())
    return jsonify(staff_list)
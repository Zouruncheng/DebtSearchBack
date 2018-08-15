from flask import request, jsonify, make_response

from app.libs.cors import allow_cross_domain
from app.libs.redprint import Redprint
from app.libs import sql_api


api = Redprint('debt')


@api.route('/newspapers',methods=['GET'])
def get_newspaper():
    """1.报纸公告接口"""
    res = {
        'code':0,
        'msg':'',
        'result':{}
    }
    args = request.args.to_dict()
    page = int(args.get('page'))
    limit_start = (page - 1) * 10
    limit_end = page  * 10

    query = '%'+args.get('query','')+'%'
    sql = 'select * from newspapers where `DESC` like "%s" order by `UPDATE_TIME` DESC limit %s,%s;' %(query,limit_start,limit_end)
    total = sql_api.query_sql("select count(*) from newspapers where `DESC` like '%s'" %(query,))[0][0]
    data = sql_api.query_sql(sql,1)
    print(sql)
    res['result']['list'] = data
    res['result']['page'] = page
    res['result']['page_size'] = 10
    res['result']['total'] = total

    return jsonify(res)



@api.route('/gdfae',methods=['GET'])
def get_guangdongfae():
    """2.广东fae接口"""
    res = {
        'code':0,
        'msg':'',
        'result':{}
    }
    args = request.args.to_dict()
    page = int(args.get('page'))
    limit_start = (page - 1) * 10
    limit_end = page  * 10

    query = '%'+args.get('query','')+'%'
    sql = 'select * from gdfae where `describe` like "%s" order by `updatetime` DESC limit %s,%s;' %(query,limit_start,limit_end)
    total = sql_api.query_sql("select count(*) from gdfae where `describe` like '%s'"%(query,))[0][0]
    data = sql_api.query_sql(sql,1)
    print(sql)
    res['result']['list'] = data
    res['result']['page'] = page
    res['result']['page_size'] = 10
    res['result']['total'] = total

    return jsonify(res)

@api.route('/sftaobao',methods=['GET'])
def get_taobao():
    """3.司法拍卖接口"""
    res = {
        'code':0,
        'msg':'',
        'result':{}
    }
    args = request.args.to_dict()
    page = int(args.get('page'))
    limit_start = (page - 1) * 10
    limit_end = page  * 10

    query = '%'+args.get('query','')+'%'
    sql = 'select * from sftaobao where `debtor` like "%s" order by `updatetime` DESC limit %s,%s;' %(query,limit_start,limit_end)
    total = sql_api.query_sql("select count(*) from sftaobao where `debtor` like '%s'" %(query))[0][0]
    data = sql_api.query_sql(sql,1)
    print(sql)
    res['result']['list'] = data
    res['result']['page'] = page
    res['result']['page_size'] = 10
    res['result']['total'] = total
    return jsonify(res)


@api.route('/utrust',methods=['GET'])
def get_utrust():
    """4.粤财接口"""
    res = {
        'code':0,
        'msg':'',
        'result':{}
    }
    args = request.args.to_dict()
    page = int(args.get('page'))
    limit_start = (page - 1) * 10
    limit_end = page  * 10

    query = '%'+args.get('query','')+'%'
    sql = 'select * from utrust where `debtor` like "%s" order by `updatetime` DESC limit %s,%s;' %(query,limit_start,limit_end)
    total = sql_api.query_sql("select count(*) from utrust")[0][0]
    data = sql_api.query_sql(sql,1)
    print(sql)
    res['result']['list'] = data
    res['result']['page'] = page
    res['result']['page_size'] = 10
    res['result']['total'] = total
    return jsonify(res)












#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pymysql
from app.config.secure import DB_CONFIG


def get_db_res(conn, sql, cur_type=0, data=None):
    cur = None
    res = []
    if cur_type == 1:
        cur = conn.cursor(pymysql.cursors.DictCursor)
        # cur = conn.cursor(cursorclass=pymysql.cursors.DictCursor)
    elif cur_type == 2:
        cur = conn.cursor(cursorclass=pymysql.cursors.SSCursor)
    else:
        cur = conn.cursor()

    if data:
        cur.execute(sql, data)
    else:
        cur.execute(sql)
    res = cur.fetchall()
    cur.close()
    return res


def query_sql(sql,cur_type=0):
    """数据库查操作"""
    try:
        conn = pymysql.connect(**DB_CONFIG)
    except Exception as e:
        print('Exception connecting[%s] ,[%s]' % (DB_CONFIG["host"], str(e)))
        return None
    res = get_db_res(conn,sql,cur_type)
    return res


def insert_sql(sql,data):
    """数据库insert操作"""
    try:
        conn = pymysql.connect(**DB_CONFIG["host"])
    except Exception as e:
        print('Exception connecting[%s] ,[%s]' % (DB_CONFIG["host"], str(e)))
        return None
    res = get_db_res(conn,sql,data=data)
    conn.commit()
    return res
#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3

def connect():
    con = sqlite3.connect('data.db')
    con.row_factory = sqlite3.Row
    return con

def get_productos():
    con = connect()
    c = con.cursor()
    query = """SELECT codigo,nombre,descripcion,marca,color FROM productos"""
    result = c.execute(query)
    prod = result.fetchall()
    con.close()
    return prod


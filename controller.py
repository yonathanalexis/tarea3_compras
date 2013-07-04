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
#actualiza la base de dato con respecto a los datos ingresado
def editar_producto(codigo,nombre,descripcion,marca,color):
    exito = False
    con = connect()
    c = con.cursor()
    query1= """SELECT id_producto FROM productos WHERE codigo=?"""
    id_producto=resultado = c.execute(query,[codigo])	
    query = "UPDATE productos SET codigo=?,nombre=?,descripcion=?,marca=?,color=? WHERE id_producto=?"
    try:
        resultado = c.execute(query,[codigo,nombre,descripcion,marca,color,id_producto])
        con.commit()
        exito = True
    except sqlite3.Error as e:
        exito = False
        print "Error:", e.args[0]
    con.close()
    return exito
#elimina una fila  de la base de datos de la tabla productos con respecto a el primary key
def delete(dato):
    exito = False
    con = connect()
    c = con.cursor()
    query = "DELETE FROM productos WHERE id_producto = ?"
    try:
        resultado = c.execute(query, [dato])
        con.commit()
        exito = True
    except sqlite3.Error as e:
        exito = False
        print "Error:", e.args[0]
    con.close()
    return exito

#inserta una fila en la base de datos con los datos ingresados
def agregar_producto(codigo,nombre,descripcion,marca,color):
    exito = False
    con = connect()
    c = con.cursor()
    values = [codigo,nombre,descripcion, marca,color]
    query = "INSERT INTO productos (codigo,nombre,descripcion,marca,color) VALUES (?,?,?,?,?)"
    try:
        resultado1 = c.execute(query, values)
        con.commit()
        exito = True
    except sqlite3.Error as e:
        exito = False
        print "Error:", e.args[0]
    con.close()
    return exito

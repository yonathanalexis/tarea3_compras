#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3

def connect():
    con = sqlite3.connect('data.db')
    con.row_factory = sqlite3.Row
    return con
def agr_compra(cantidad,precio,total,codigo):
    exito = False
    con = connect()
    c = con.cursor()
    query1= """SELECT id_producto FROM productos WHERE codigo=?"""
    resultado = c.execute(query1,[codigo])
    id_producto=resultado.fetchone()
    query = " INSERT INTO compra_has_producto (fk_id_producto,cantidad,precio_unitario,total) VALUES (?,?,?,?)"
    try:
        c.execute(query,[id_producto[0],cantidad,precio,total])
        con.commit()
        exito = True
    except sqlite3.Error as e:
        exito = False
        print "Error:", e.args[0]
    con.close()
    return exito
def get_prod_compra():
    con = connect()
    c = con.cursor()
    query = """SELECT a.codigo,a.nombre,a.descripcion,a.marca,a.color,b.cantidad,b.precio_unitario,b.total FROM productos a,compra_has_producto b WHERE a.id_producto=b.fk_id_producto """
    result = c.execute(query)
    prod = result.fetchall()
    con.close()
    return prod
def get_productos():
    con = connect()
    c = con.cursor()
    query = """SELECT codigo,nombre,descripcion,marca,color FROM productos"""
    result = c.execute(query)
    prod = result.fetchall()
    con.close()
    return prod
def get_compra():
    con = connect()
    c = con.cursor()
    query = """SELECT a.fecha,a.proveedor,a.numero_factura,a.descripcion,b.total FROM compra a, compra_has_producto b"""
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
    resultado = c.execute(query1,[codigo])
    id_producto=resultado.fetchone()	
    query = "UPDATE productos SET codigo=?,nombre=?,descripcion=?,marca=?,color=? WHERE id_producto=?"
    try:
        resultado = c.execute(query,[codigo,nombre,descripcion,marca,color,id_producto[0]])
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
    query = "DELETE FROM productos WHERE codigo = ?"
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
    values = [codigo,nombre,descripcion,marca,color]
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
def buscar_compra(word_c,word_p):
    con = connect()
    c = con.cursor()
    query = """SELECT a.fecha, a.proveedor, a.numero_factura, a.descripcion
            FROM compra a,produtos b
            WHERE (a.codigo LIKE '%'||?||'%' OR a.nombre LIKE '%'||?||'%' OR b.fecha LIKE '%'||?||'%' OR b.proveedor LIKE '%'||?||'%'OR b.numero_factura LIKE '%'||?||'%' )"""

    result = c.execute(query, [word_p, word_p, word_c, word_c, word_c])
    seleccion= result.fetchall()
    con.close()
    return seleccion
def buscar_compra_realizada(word):
    con = connect()
    c = con.cursor()
    query = """SELECT a.nombre, a.marca, b.precio_unitario, b.cantidad, b.total
            FROM produtos a,compra_has_producto b
            WHERE (a.codigo LIKE '%'||?||'%' OR a.nombre LIKE '%'||?||'%' OR a.marca LIKE '%'||?||'%' OR a.color LIKE '%'||?||'%'OR a.descripcion LIKE '%'||?||'%' )"""

    result = c.execute(query, [word,word,word,word,word])
    seleccion= result.fetchall()
    con.close()
    return seleccion
def buscar_producto(word):
    con = connect()
    c = con.cursor()
    query = """SELECT a.codigo, a.nombre, a.descripcion, a.marca,a.color
            FROM productos a
            WHERE (a.codigo LIKE '%'||?||'%' OR a.nombre LIKE '%'||?||'%' OR a.marca LIKE '%'||?||'%' )"""

    result = c.execute(query, [word, word, word])
    seleccion= result.fetchall()
    con.close()
    return seleccion

#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3
"""
Funciones para usar la Base de Datos
"""
def connect():
    con = sqlite3.connect('data.db')
    con.row_factory = sqlite3.Row
    return con

def agr_compra(cantidad,precio,total,codigo):
    """
    Funcion para agregar compra un nuevo item a la la tabla de compras
    """
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

def agr_dato(fecha,proveedor,descripcion):
    """
    
    """
    exito = False
    con = connect()
    c = con.cursor()
    todos=[fecha,proveedor,-1,descripcion]
    query1= """INSERT INTO compra (fecha,proveedor,numero_factura,descripcion) VALUES (?,?,?,?)"""
    resultado = c.execute(query1,todos)
    con.commit()
    query3= """SELECT * FROM compra WHERE numero_factura=?"""
    resultado = c.execute(query3,[-1])
    con.commit()
    id_compra=resultado.fetchone()
    print(id_compra[0])
    query2="""UPDATE compra SET numero_factura=?"""
    c.execute(query2,[id_compra[0]])
    con.commit()
    con.close()
    return id_compra[0]

def get_prod_compra(codigo):
    """
    Funcion para obetenr los un producto y su respectiva compra
    """
    con = connect()
    c = con.cursor()
    query = """SELECT a.codigo,a.nombre,a.marca,b.cantidad,b.precio_unitario,b.total FROM productos a,compra_has_producto b, compra c WHERE b.fk_id_compra=? """
    result = c.execute(query,[codigo])
    prod = result.fetchall()
    con.close()
    return prod

def get_id_compra():
    """
    Funcion para obtener una compra a traves de un id
    """
    con = connect()
    c = con.cursor()
    query = """SELECT b.fk_id_compra,b.total FROM productos a,compra_has_producto b WHERE a.id_producto=b.fk_id_producto """
    result = c.execute(query)
    prod = result.fetchall()
    con.close()
    return prod

def get_productos():
    """
    Funcion para obtener un producto
    """
    con = connect()
    c = con.cursor()
    query = """SELECT codigo,nombre,descripcion,marca,color FROM productos"""
    result = c.execute(query)
    prod = result.fetchall()
    con.close()
    return prod

def get_compra():
    """
    Funcion para obtener una compra
    """
    con = connect()
    c = con.cursor()
    query = """SELECT id_compra,fecha,proveedor,numero_factura,descripcion FROM compra """
    result = c.execute(query)
    prod = result.fetchall()
    con.close()
    return prod

def cambiar_precios(key,cantidad,precio,descuento):
    """
    Funcion para cambiar el precio de un producto comprado
    """
    con = connect()
    c = con.cursor()
    pre=precio*(descuento/100)
    tot=pre*cantidad
    query = """UPDATE compras_has_productos SET cantidad=?,precio_unitario=pre,total=tot WHERE fk_id_producto=? """
    result = c.execute(query,[cantidad,key])
    prod = result.fetchall()
    con.close()
    return prod

def get_compra_unitaria(codigo):
    """
    Funcion para obtener una compra
    """
    con = connect()
    c = con.cursor()
    query = """SELECT a.nombre, a.marca, b.precio_unitario,b.cantidad, b.total, b.fk_id_producto FROM productos a,compra_has_producto b WHERE b.fk_id_producto=a.id_producto AND b.fk_id_compra=? """
    result = c.execute(query,[codigo])
    prod = result.fetchall()
    con.close()
    return prod

def editar_producto(codigo,nombre,descripcion,marca,color):
    """
    Actualiza la base de dato con respecto a los datos ingresado
    """
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

def delete(dato):
    """
    Elimina una fila  de la base de datos de la tabla productos con respecto a el primary key
    """
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

def borrar_compra(dato):
    """
    Funcion para borrar una compra realizada
    """
    exito = False
    con = connect()
    c = con.cursor()
    query = "DELETE FROM compra WHERE numero_factura = ?"
    try:
        resultado = c.execute(query, [dato])
        con.commit()
        exito = True
    except sqlite3.Error as e:
        exito = False
        print "Error:", e.args[0]
    con.close()
    return exito

def agregar_producto(codigo,nombre,descripcion,marca,color):
    """
    inserta una fila en la base de datos con los datos ingresados
    """
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
    """

    """
    con = connect()
    c = con.cursor()
    query = """SELECT a.fecha, a.proveedor, a.numero_factura, a.descripcion
            FROM compra a,productos b, compra_has_producto c
            WHERE (((b.codigo LIKE '%'||?||'%'AND c.fk_id_compra=a.id_compra AND c.fk_id_producto=b.id_producto) OR (b.nombre LIKE '%'||?||'%' AND c.fk_id_compra=a.id_compra AND c.fk_id_producto=b.id_producto )) AND(a.fecha LIKE '%'||?||'%' OR a.proveedor LIKE '%'||?||'%'OR a.numero_factura LIKE '%'||?||'%') )"""

    result = c.execute(query, [word_p, word_p, word_c, word_c, word_c])
    seleccion= result.fetchall()
    con.close()
    return seleccion

def buscar_compra_realizada(word):
    """
    Funcion para filtrar compras en la grilla 
    """
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
    """
    Funcion para filtrar los productos en la grilla
    """
    con = connect()
    c = con.cursor()
    query = """SELECT a.codigo, a.nombre, a.descripcion, a.marca,a.color
            FROM productos a
            WHERE (a.codigo LIKE '%'||?||'%' OR a.nombre LIKE '%'||?||'%' OR a.marca LIKE '%'||?||'%' )"""

    result = c.execute(query, [word, word, word])
    seleccion= result.fetchall()
    con.close()
    return seleccion

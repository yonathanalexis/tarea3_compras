#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3

def connect():
    con = sqlite3.connect('data.db')
    con.row_factory = sqlite3.Row
    return con
def tomar_id(codigo):
    con = connect()
    c = con.cursor()
    query1= """SELECT id_producto FROM productos WHERE codigo=?"""
    resultado = c.execute(query1,[codigo])
    id_producto=resultado.fetchone()
    con.close()
    print id_producto[0]
    return id_producto[0]
def agr_compra(cantidad,precio,total,codigo,id_compra):

    exito = False
    con = connect()
    c = con.cursor()
    query1= """SELECT id_producto FROM productos WHERE codigo=?"""
    resultado = c.execute(query1,[codigo])
    id_producto=resultado.fetchone()
    query = " INSERT INTO compra_has_producto (fk_id_compra,fk_id_producto,cantidad,precio_unitario,total) VALUES (?,?,?,?,?)"
    try:
        c.execute(query,[id_compra,id_producto[0],cantidad,precio,total])
        con.commit()
        exito = True
    except sqlite3.Error as e:
        exito = False
        print "Error:", e.args[0]
    con.close()
    return exito

def agr_dato(fecha,proveedor,descripcion):#crea una compra con los datos ingresados como proveedor y descripcion y la fecha desde el pc
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
    query2="""UPDATE compra SET numero_factura=? WHERE id_compra=?"""
    
    c.execute(query2,[id_compra[0],id_compra[0]])
    con.commit()
    con.close()
    return id_compra[0]

def get_prod_compra(id_compra,id_produc):
    con = connect()
    c = con.cursor()
    query = """SELECT a.codigo,a.nombre,a.marca,b.cantidad,b.precio_unitario,b.total FROM productos a,compra_has_producto b WHERE b.fk_id_compra=? AND a.id_producto=b.fk_id_producto"""
    result = c.execute(query,[id_compra])
    con.commit()
    prod = result.fetchall()
    con.close()
    return prod
def get_id_compra():
    con = connect()
    c = con.cursor()
    query = """SELECT b.fk_id_compra,b.total FROM productos a,compra_has_producto b WHERE a.id_producto=b.fk_id_producto """
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
    query = """SELECT id_compra,fecha,proveedor,numero_factura,descripcion FROM compra """
    result = c.execute(query)
    prod = result.fetchall()
    con.close()
    return prod
def cambiar_precios(codigo,key,cantidad,precio,total):
    """
    Funcion para cambiar el precio de un producto comprado
    """
    exito=False
    con = connect()
    c = con.cursor()
    #pre=precio*(descuento/100)
    #tot=pre*cantidad
    query = """UPDATE compra_has_producto SET cantidad=?,precio_unitario=?,total=? WHERE fk_id_producto=? AND fk_id_compra=? """
    try:
        result = c.execute(query,[cantidad,precio,total,key,codigo])
        prod = result.fetchall()
        con.commit()
        exito = True
    except sqlite3.Error as e:
        exito = False
        print "Error:", e.args[0]
    con.close()
    return exito
def get_compra_unitaria(codigo):
    con = connect()
    c = con.cursor()
    query = """SELECT a.nombre, a.marca, b.precio_unitario,b.cantidad, b.total, b.fk_id_producto FROM productos a,compra_has_producto b WHERE b.fk_id_producto=a.id_producto AND b.fk_id_compra=? """
    result = c.execute(query,[codigo])
    prod = result.fetchall()
    con.close()
    return prod
def editar_compra(precio,cantidad,total,codigo,id_compra):
    exito = False
    con = connect()
    c = con.cursor()
    query1= """SELECT id_producto FROM productos WHERE codigo=?"""
    resultado = c.execute(query1,[codigo])
    id_producto=resultado.fetchone()	
    query = "UPDATE compra_has_producto SET precio_unitario=?,cantidad=?,total=? WHERE fk_id_compra=? AND fk_id_producto=?"
    try:
        resultado = c.execute(query,[cantidad,precio,total,id_compra,id_producto[0]])
        con.commit()
        exito = True
    except sqlite3.Error as e:
        exito = False
        print "Error:", e.args[0]
    con.close()
    return exito
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
def editar_prov_des(proveedor,descripcion,codigo):#SSSSSSSSSSSSSSS
    """
    Actualiza la base de dato con respecto a los datos ingresado en una compra
    """
    exito = False
    con = connect()
    c = con.cursor()
    query = "UPDATE compra SET proveedor=?,descripcion=? WHERE id_compra=?"
    try:
        resultado = c.execute(query,[proveedor,descripcion,codigo])
        con.commit()
        exito = True
    except sqlite3.Error as e:
        exito = False
        print "Error:", e.args[0]
    con.close()
    return exito
def eliminar_prod_compra(codigo):
    exito = False
    con = connect()
    c = con.cursor()
    query = "DELETE FROM compra_has_producto WHERE codigo = ?"
    try:
        resultado = c.execute(query, [dato])
        con.commit()
    except sqlite3.Error as e:
        exito = False
        print "Error:", e.args[0]
    con.close()
    return exito
def cancelar_compra(id_compra):
    con = connect()
    c = con.cursor()
    query1 = "DELETE FROM compra WHERE id_compra = ?"
    c.execute(query1, [id_compra])
    query = "DELETE FROM compra_has_producto WHERE fk_id_compra = ?"
    c.execute(query, [id_compra])
    con.commit()
    con.close()
def borrar_prod_com(dato):
    """
    Elimina una fila  de la base de datos de la tabla compra_has_producto con respecto a el primary key
    """
    exito = False
    con = connect()
    c = con.cursor()
    query = "DELETE FROM compra_has_producto WHERE fk_id_producto = ?"
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
    exito = False
    con = connect()
    c = con.cursor()
    	
    query2 = "DELETE FROM compra WHERE id_compra= ?"
    c.execute(query2, [dato])
    con.commit()
    query = "DELETE FROM compra_has_producto WHERE fk_id_compra = ?"
    try:
        c.execute(query, [dato])
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
def buscar_compra_realizada(word,codigo):#;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
	"""
	Funcion para filtrar compras en la grilla
	"""
	con = connect()
	c = con.cursor()
	query = """SELECT a.nombre, a.marca, b.precio_unitario,b.cantidad, b.total, b.fk_id_producto
	FROM productos a,compra_has_producto b
	WHERE ((a.codigo LIKE '%'||?||'%' OR a.nombre LIKE '%'||?||'%' OR a.marca LIKE '%'||?||'%' OR a.color LIKE '%'||?||'%'OR a.descripcion LIKE '%'||?||'%') AND (b.fk_id_producto=a.id_producto AND b.fk_id_compra=?))"""

	result = c.execute(query, [word,word,word,word,word,codigo])
	seleccion= result.fetchall()
	con.close()
	return seleccion
def buscar_compra(word_c,word_p):
	"""
	busca una compra con un filtro de productos
	"""
	con = connect()
	c = con.cursor()
	query = """SELECT a.id_compra,a.fecha, a.proveedor, a.numero_factura, a.descripcion
	FROM compra a,productos b, compra_has_producto c
	WHERE (((b.codigo LIKE '%'||?||'%'AND c.fk_id_compra=a.id_compra AND c.fk_id_producto=b.id_producto) OR (b.nombre LIKE '%'||?||'%' AND c.fk_id_compra=a.id_compra AND c.fk_id_producto=b.id_producto )) AND((a.fecha LIKE '%'||?||'%' OR a.proveedor LIKE '%'||?||'%'OR a.numero_factura LIKE '%'||?||'%') AND (c.fk_id_compra=a.id_compra AND c.fk_id_producto=b.id_producto) ) )"""

	result = c.execute(query, [word_p, word_p, word_c, word_c, word_c])
	seleccion= result.fetchall()
	print(seleccion)
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

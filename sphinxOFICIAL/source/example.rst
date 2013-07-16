Controller:
===============
en esta clase  realiza toda la administración de la base de datos
se realizan las query necesarias mediante las funciones


funciones y query 
----------------


listado de funciones:

 * def agr_compra(cantidad,precio,total,codigo):
	inserta y agrega una compra
 * get_prod_compra():
	selecciona la fila completa de un producto
 * def get_productos():
	selecciona todos los productos
 * def editar_producto(codigo,nombre,descripcion,marca,color):
 	selecciona un producto y lo edita
 * def delete(dato): 
	elimina de la tabla productos de acuerdo al codigo del producto
 * def agregar_producto(codigo,nombre,descripcion,marca,color):
	agrega todos los parametros de un nuevo producto  en la tabla productos
 * buscar_producto(word):
	selecciona un producto 


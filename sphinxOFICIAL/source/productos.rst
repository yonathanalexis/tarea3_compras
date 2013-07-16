clase Productos:
**************************

en esta clase se crea la tabla compra_as_producto
y la tabla productos

Metodos propios de la clase
=============================

 * c.execute("""CREATE TABLE compra_has_producto (fk_id_compra integer,fk_id_producto integer,cantidad integer,precio_unitario integer,total integer,FOREIGN KEY (fk_id_compra) REFERENCES compra(id_compra),FOREIGN KEY (fk_id_producto) REFERENCES productos(id_producto))""")




*	c.execute("""CREATE TABLE productos (id_producto integer primary key AUTOINCREMENT,codigo text,nombre text,descripcion text,marca text,color text)""")
	
*crea la tabla productos con id_producto como primary key AUTOINCREMENT para que cada vez que se ingrese un nuevo producto
	id_producto sea primary key 

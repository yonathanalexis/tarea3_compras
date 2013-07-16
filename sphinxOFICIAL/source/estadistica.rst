clase estadistica:
===============

esta clase es una de las más importantes debido a que en ella
se trabaja con el historial de compras realizados por la empresa


funciones
----------------


listado de funciones más importantes:

 * def buscar_compra(self):
	busca una compra en la base de datos , busca de acuerdo a la compra y al producto que se compro
	recibe parametro de la clase controller de la funcion buscar_compra(arg1,arg2)
 *def eliminar_compra(self):
	función para eliminar una compra seleccionada del historial de compras, llama a la funcion borrar_compra()
	de la clase controller
 *def editar_compra_unitaria(self):
	funcion para poder editar una compra seleccionada, debe seleccionarce la compra desde la grilla, en caso contrario aparece
	un mensaje de error

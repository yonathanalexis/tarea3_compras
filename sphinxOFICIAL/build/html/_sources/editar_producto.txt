Clase editar_producto:
===============
ecuando a un producto se le realiza un descuento es necesario editarlo y almacenar su nuevo valor

funciones y query
----------------


listado de funciones mas importantes:

* def agregar_cambios(self):
		precio=self.ui.line_precio.text()
		cantidad = self.ui.line_cantidad.text()
		descuento = self.ui.line_descuento.text()
		result = controller.cambiar_precios(self.key,cantidad,precio,descuento)
		if result:
			self.reject()
*toma el precio, la cantidad y el descuento y lo envia mediante la clase controller a la función
cambiar precios que recive estos parametros y realiza el calculo

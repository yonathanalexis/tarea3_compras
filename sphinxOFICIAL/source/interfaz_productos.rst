interfaz compras:
**************************


signals & metodos
=========================
		 * self.ui.editar_btn.clicked.connect(self.editar_dato)
		 * self.ui.agregar_btn.clicked.connect(self.agregar_dato)
		 * self.ui.eliminar_btn.clicked.connect(self.eliminar_dato)
		 * self.ui.btn_buscar.clicked.connect(self.cargar_buscar)
		 * self.ui.compra_btn.clicked.connect(self.compra)
 		 * self.ui.estadisticas_btn.clicked.connect(self.estadisticas)

Metodos propios de la clase
=============================

        * def estadisticas(self):
		responde a estadisticas_btn.clicked, muestra el formulario con el registro de las compras realizadas
	* def compra(self):
		responde a compra_btn, despliega el formulario de nueva compra
	* def agregar_dato(self):
		responde a agregar_btn , agrega nuevo dato
	* def cargar_buscar(self):
		responde btn_buscar, busca producto tomando la palabra desde el linetext	
	* def eliminar_dato(self):
		responde a eliminar_btn elimina elemento seleccionado desde la grilla, lanza advertencia si no se ha seleccionado elemento
	* def editar_dato(self):
		responde a editar_btn realiza la edicion de un dato desde la grilla, lanza advertencia si no se ha seleccionado elemento
	
		

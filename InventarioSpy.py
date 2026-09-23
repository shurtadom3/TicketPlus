class InventarioSpy:
    def __init__(self):
        self.veces_consultado = 0
    
    def consultar_disponibilidad(self):
        self.veces_consultado += 1
        return 50
    
#inventarioSpy = InventarioSpy()
#inventarioSpy.consultar_disponibilidad()
#inventarioSpy.consultar_disponibilidad()
#inventarioSpy.consultar_disponibilidad()
#print(inventarioSpy.veces_consultado)
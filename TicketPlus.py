from InventarioStub import InventarioStub
from RepositorioFake import RepositorioFake
from UsuarioDummy import UsuarioDummy
from unittest.mock import Mock
from EmailDummy import EmailDummy
from InventarioSpy import InventarioSpy
class TicketService:
   def __init__(self, inventario, repositorio, email_service):
      self.inventario = inventario
      self.repositorio = repositorio
      self.email_service = email_service
 
   def comprar(self, usuario, cantidad):
      disponibles = self.inventario.consultar_disponibilidad()
      if disponibles < cantidad:
          return False
      self.repositorio.guardar(usuario, cantidad)
      self.email_service.enviarConfirmacion(usuario)
      return True
inventarioSpy = InventarioSpy()
emailMock = Mock()
service = TicketService(inventarioSpy, RepositorioFake() , emailMock)
# resultado = service.comprar("Ana", 2)
resultado = service.comprar(UsuarioDummy(), 2)
emailMock.enviarConfirmacion.assert_called_once()
print(resultado) 

service.comprar(UsuarioDummy(), 1)
print(inventarioSpy.veces_consultado)

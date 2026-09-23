from unittest.mock import Mock

from TicketPlus import TicketService
from InventarioStub import InventarioStub
from RepositorioFake import RepositorioFake
from UsuarioDummy import UsuarioDummy


def test_compra_exitosa():

    emailMock = Mock()

    service = TicketService(
        InventarioStub(),
        RepositorioFake(),
        emailMock
    )

    resultado = service.comprar(
        UsuarioDummy(),
        2
    )

    assert resultado is True

    emailMock.enviarConfirmacion.assert_called_once()

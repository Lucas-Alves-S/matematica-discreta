from .calculadoras.bases import CalculadoraBases
from .calculadoras.euclides import EuclidesEstendido
from .calculadoras.crivo import CrivoEratostenes


class Api(CalculadoraBases, EuclidesEstendido, CrivoEratostenes):
    """Classe exposta ao JavaScript via window.pywebview.api.

    Herda os métodos públicos de cada calculadora como mixins,
    mantendo a lógica separada por responsabilidade.
    """

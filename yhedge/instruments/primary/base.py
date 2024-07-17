import torch
from torch import Tensor


from ..base import BaseInstrument

class BasePrimary(BaseInstrument):

    dt: float
    cost: float
    _buffers: dict

    def __init__(self) -> None:
        super().__init__()
        self._buffers = {}

    def register_buffer(self, name: str, tensor: Tensor) -> None:
        self._buffers[name] = tensor


    @property
    def spot(self):
        name = "spot"
        return self._buffers[name]

    

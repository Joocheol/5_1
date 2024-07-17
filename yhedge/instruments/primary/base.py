import torch
from torch import Tensor


from ..base import BaseInstrument

class BasePrimary(BaseInstrument):

    dt: float
    cost: float
    _buffers: dict

    def __init__(self) -> None:
        super().__init__()
        self._buffers = dict()

    def register_buffer(self, name: str, tensor: Tensor) -> None:
        self._buffers[name] = tensor

    

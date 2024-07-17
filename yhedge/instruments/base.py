from abc import ABC, abstractmethod

import torch
from torch import Tensor

class BaseInstrument(ABC):

    cost: float

    @property
    @abstractmethod
    def spot(self) -> Tensor:
        """"""

    @property
    @abstractmethod
    def simulate(self, n_paths: int, time_horizon: float, **kwargs) -> None:
        """"""

    
    

    
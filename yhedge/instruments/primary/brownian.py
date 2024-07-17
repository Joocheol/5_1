import torch
from torch import Tensor

from .base import BasePrimary

class BrownianStock(BasePrimary):

    def __init__(
        self, 
        sigma: float = 0.2,
        mu: float = 0.0,
        cost: float = 0.0,
        dt: float = 1 / 250,
    ) -> None:
        
        super().__init__()

        self.sigma = sigma
        self.mu = mu
        self.cost = cost
        self.dt = dt

    @property
    def default_init_state(self):
        return (1.0,)
    
    def simulate(
        self,
        n_paths: int = 1,
        time_horizon: float = 20 / 250,
        init_state = None,
    ):
        
        if init_state is None:
            init_state = self.default_init_state

        spot = torch.randn(1,1)

        self.register_buffer("spot", spot)

        
    



from typing import Optional
from jaxtyping import jaxtyped
from typeguard import typechecked as typechecker

import mlx.core as mx
import mlx.nn as nn

from ..modules.activation import relu


@jaxtyped(typechecker=typechecker)
class ReLU(nn.Module):
    def __init__(
            self,
            inplace: bool = False,
            device: Optional[mx.DeviceType] = None
    ):
        super().__init__()

        self.device = device
        self.inplace = inplace

    def __call__(
            self,
            x: mx.array,
    ) -> mx.array:
        """
        Like torch.nn.ReLU using functional relu
        """
        return relu(x, self.inplace, self.device)

    def _extra_repr(self):
        return super()._extra_repr()


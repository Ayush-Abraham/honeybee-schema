from enum import Enum


class LayerDirectionType(str, Enum):
    forward = "Forward"
    reverse = "Reverse"
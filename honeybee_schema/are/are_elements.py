from pydantic import (
    Field
)
from typing import List, Union, Annotated
from enum import Enum


from typing_extensions import Annotated


class ElementType(str, Enum):
    external_wall = "External Wall"
    internal_wall = "Internal Wall"
    floor_ceiling = "Floor Ceiling"
    roof = "Roof"
    window = "Window"
    door = "Door"
    opaque_louvre = "Opaque Louvre"
    skylight = "Skylight"
    roof_window = "Roof Window"
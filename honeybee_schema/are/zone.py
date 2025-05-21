from pydantic import (
    Field
)
from typing import List, Union, Annotated
from enum import Enum


from typing_extensions import Annotated


class ZoneType(str, Enum):
    outdoor_air = "Outdoor Air"
    neighbour = "Neighbour"
    ground = "Ground"
    living = "Living"
    bedroom = "Bedroom"
    living_kitchen = "Kitchen - Living"
    day_time = "Day Time"
    unconditioned = "Unconditioned"
    night_time = "Night Time"
    garage = "Garage"
    garage_conditioned = "Garage - conditioned"
    corridor = "Corridor"
    roof_space = "Roof Space"
    subfloor = "Subfloor"
    shared_basement_car_park = "Shared Basement Car Park"
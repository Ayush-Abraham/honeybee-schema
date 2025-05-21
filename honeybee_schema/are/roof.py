from pydantic import (
    Field
)
from typing import List, Union, Annotated
from enum import Enum


from typing_extensions import Annotated


class RoofExposureType(str, Enum):
    normal = "Normal"
    parasol = "Parasol"
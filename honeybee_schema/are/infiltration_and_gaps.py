from pydantic import (
    Field
)
from typing import List, Union, Annotated
from enum import Enum


from typing_extensions import Annotated

class GapSizeType(str, Enum):
    nogap = "None"
    small = "Small"
    medium = "Medium"
    large = "Large"

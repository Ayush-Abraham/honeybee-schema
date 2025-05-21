from pydantic import (
    Field
)
from typing import List, Union, Annotated
from enum import Enum


from typing_extensions import Annotated


class WindowType(str, Enum):
    awning = "Awning"
    casement = "Casement"
    double_or_single_hung = "Double or Single Hung"
    louvre = "Louvre"
    sliding = "Sliding"
    other = "Other"


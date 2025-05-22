from pydantic import (
    Field
)
from typing import List, Union, Annotated
from enum import Enum


from typing_extensions import Annotated

from .are_schema import Address
from .are_schema import DwellingExposureType1, DwellingType1


class Dwelling():
    """Information about the dwelling (site)"""
    climate_zone : int = Field(
        description = "NatHERS climate zone number",
        ge=1,
        le=69
    )
    ground_reflectance : float | None = Field(
        default = 0.2,
        description = "Ground reflectance - default to 0.2"
    )
    
    council_submitted_to : str | None = Field(
        default = None,
        description = "Council that plans are submitted to"
    )
    
    dwelling_exposure_type : DwellingExposureType1 = Field(
        description = "Exposure type of dwelling"
    )

    dwelling_type : DwellingType1 = Field(
        description = "Type of dwelling"
    )

    address : Address | None = Field(
        default = None,
        description = "Address of building"
    )



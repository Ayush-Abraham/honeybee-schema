from pydantic import (
    Field
)

from datetime import datetime

from .are_schema import HeatingCoolingLimit, Ventilation

class DesignVariation():
    name: str | None = Field(
        default = None,
        description = "Name of design variation"
    )

    description : str | None = Field(
        default = None,
        description = "Description of design variation"
    )

    submitted_date_time: datetime = Field(
        description = "Submitted date and time"
    )

    heating_cooling_limit: HeatingCoolingLimit | None = Field(
        default = None,
        description = "Heating and Cooling limit info for this design variation"
    )

    ventilation: Ventilation | None = Field(
        default = None,
        description = "Site ventilation information for this design variation"
    )





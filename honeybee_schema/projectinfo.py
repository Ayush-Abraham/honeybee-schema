"""Schema for project information."""

from pydantic import StringConstraints, BaseModel, Field, AnyUrl
from typing import List, Union

from .altnumber import Autocalculate
from .energy.simulation import EfficiencyStandards, ClimateZones, BuildingTypes
from typing_extensions import Annotated


class Location(BaseModel):
    """A Ladybug Location."""

    type: Annotated[str, StringConstraints(pattern="^Location$")] = "Location"

    city: str = Field("-", description="Name of the city as a string.")

    latitude: float = Field(
        0, description="Location latitude between -90 and 90 (Default: 0)."
    )

    longitude: float = Field(
        0,
        description="Location longitude between -180 (west) and 180 (east) (Default: 0).",
    )

    time_zone: Union[Autocalculate, Annotated[int, Field(ge=-12, le=14)]] = Field(
        Autocalculate(),
        description="Time zone between -12 hours (west) and +14 hours (east). "
        "If None, the time zone will be an estimated integer value derived from "
        "the longitude in accordance with solar time.",
    )

    elevation: float = Field(
        0, description="A number for elevation of the location in meters. (Default: 0)."
    )

    station_id: str | None = Field(
        None,
        description="ID of the location if the location is representing a weather "
        "station.",
    )

    source: str | None = Field(None, description="Source of data (e.g. TMY, TMY3).")


class ProjectInfo(BaseModel):
    """Project information."""

    type: Annotated[str, StringConstraints(pattern="^ProjectInfo$")] = "ProjectInfo"

    north: float = Field(
        0,
        description="A number between -360 to 360 where positive values rotate the "
        "compass counterclockwise (towards the West) and negative values rotate the "
        "compass clockwise (towards the East).",
        le=360,
        ge=-360,
    )

    weather_urls: List[AnyUrl] | None = Field(
        None,
        description="A list of URLs to zip files that includes EPW, DDY and STAT files. "
        "You can find these URLs from the EPWMAP. The first URL will be used as the "
        "primary weather file.",
    )

    location: Location | None = Field(
        None,
        description="Project location. This value is usually generated from the "
        "information in the weather files.",
    )

    ashrae_climate_zone: ClimateZones | None = Field(
        None, description="Project location climate zone."
    )

    building_type: List[BuildingTypes] | None = Field(
        None,
        description="A list of building types for the project. The first building "
        "type is considered the primary type for the project.",
    )

    vintage: List[EfficiencyStandards] | None = Field(
        None, description="A list of building vintages (e.g. ASHRAE_2019, ASHRAE_2016)."
    )

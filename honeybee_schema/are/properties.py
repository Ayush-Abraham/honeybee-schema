"""Model are properties."""

from pydantic import StringConstraints, Field
from typing import List, Union
from typing_extensions import Annotated

class DoorAREPropertiesAbridged():
    type: Annotated[
        str, StringConstraints(pattern="^DoorAREPropertiesAbridged$")
    ] = "DoorAREPropertiesAbridged"

    construction: str | None = Field(
        default=None,
        min_length=1,
        max_length=100,
        description="",
    )

    is_external_door: bool | None = Field(
        default=None,
        description="True if this door opens to the outdoors"
    )

    is_permanent_opening: bool | None = Field(
        default=False,
        description="True if this is a permanent opening such as an archway"
    )
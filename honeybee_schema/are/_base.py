"""Base class used by various schema objects."""

from pydantic import Field, BaseModel



class OptionalIDBase(BaseModel):
    """ Base class when identifier is optinal """
    identifier: str | None = Field(
        default = None,
        description = "unique identifier"
    )

    display_name: str | None = Field(
        default = None,
        description = "Name"
    )

class RequiredIDBase(BaseModel):
    """ Base class when identifier is required """
    identifier: str = Field(
        description = "unique identifier"
    )

    display_name: str | None = Field(
        default = None,
        description = "Name"
    )

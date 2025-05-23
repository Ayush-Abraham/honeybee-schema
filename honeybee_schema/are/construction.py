"""Construction Schema"""

from pydantic import StringConstraints, Field

from .are_schema import GlazedConstruction, ExternalConstruction, InternalConstruction

from typing_extensions import Annotated


class ExternalConstructionAbridged():
    """External construction"""

    type: Annotated[str, StringConstraints(pattern="^ExternalConstructionAbridged$")] = (
        "ExternalConstructionAbridged"
    )

    identifier: str = Field(
        description = "identifier for external construction to match it to full definition"
    )

class InternalConstructionAbridged():
    """Internal construction"""

    type: Annotated[str, StringConstraints(pattern="^InternalConstructionAbridged$")] = (
        "InternalConstructionAbridged"
    )

    identifier: str = Field(
        description = "identifier for internal construction to match it to full definition"
    )

class GlazedConstructionAbridged():
    """Glazed construction"""

    type: Annotated[str, StringConstraints(pattern="^GlazedConstructionAbridged$")] = (
        "GlazedConstructionAbridged"
    )

    identifier: str = Field(
        description = "identifier for glazed construction to match it to full definition"
    )

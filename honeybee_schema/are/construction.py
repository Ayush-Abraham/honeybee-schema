"""Construction Schema"""

from pydantic import StringConstraints, Field
from typing import List, Union
from enum import Enum

from .are_schema import GlazedConstruction, ExternalConstruction, InternalConstruction
from .schedule import ScheduleRuleset, ScheduleFixedInterval
from typing_extensions import Annotated


class ExternalConstructionAbridged():
    """External construction"""

    type: Annotated[str, StringConstraints(pattern="^ExternalConstructionAbridged$")] = (
        "ExternalConstructionAbridged"
    )
    
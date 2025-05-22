"""Global construction-set for Model."""

import pathlib
import json

from typing import List, Union
from pydantic import StringConstraints, Field

from honeybee_standards import energy_default

from .._base import NoExtraBaseModel
from .constructionset import (
    WallConstructionSetAbridged,
    FloorConstructionSetAbridged,
    RoofCeilingConstructionSetAbridged,
    ApertureConstructionSetAbridged,
    DoorConstructionSetAbridged,
)

from .construction import (
    OpaqueConstructionAbridged,
    WindowConstructionAbridged,
    ShadeConstruction,
    AirBoundaryConstructionAbridged,
)

from typing_extensions import Annotated
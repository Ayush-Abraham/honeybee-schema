"""Global modifier-set for Model."""

import pathlib
import json

from typing import List, Union
from pydantic import StringConstraints, Field

from honeybee_standards import radiance_default

from .._base import NoExtraBaseModel
from .modifierset import (
    WallModifierSetAbridged,
    FloorModifierSetAbridged,
    RoofCeilingModifierSetAbridged,
    ApertureModifierSetAbridged,
    DoorModifierSetAbridged,
    ShadeModifierSetAbridged,
)
from .modifier import Plastic, Glass, Trans
from typing_extensions import Annotated


# import modifierset default values from honeybee standards
_DEFAULTS = json.loads(pathlib.Path(radiance_default).read_text())
_MOD_SET = [
    ms
    for ms in _DEFAULTS["modifier_sets"]
    if ms["identifier"] == "Generic_Interior_Visible_Modifier_Set"
][0]
_MODIFIER_NAMES = [
    "generic_wall_0.50",
    "generic_floor_0.20",
    "generic_ceiling_0.80",
    "generic_interior_window_vis_0.88",
    "generic_exterior_window_vis_0.64",
    "generic_opaque_door_0.50",
    "generic_interior_shade_0.50",
    "generic_exterior_shade_0.35",
    "generic_context_0.20",
    "air_boundary",
]
_MODIFIERS = [
    Plastic.model_validate(m)
    if m["type"] == "Plastic"
    else Glass.model_validate(m)
    if m["type"] == "Glass"
    else Trans.model_validate(m)
    for m in _DEFAULTS["modifiers"]
    if m["identifier"] in _MODIFIER_NAMES
]


class GlobalModifierSet(NoExtraBaseModel):
    type: Annotated[str, StringConstraints(pattern="^GlobalModifierSet$")] = (
        "GlobalModifierSet"
    )

    modifiers: List[Union[Plastic, Glass, Trans]] = Field(
        default=_MODIFIERS,
        description="Global Honeybee Radiance modifiers.",
        frozen=True,
    )

    wall_set: WallModifierSetAbridged = Field(
        default=WallModifierSetAbridged.model_validate(_MOD_SET["wall_set"]),
        description="Global Honeybee WallModifierSet.",
        frozen=True,
    )

    floor_set: FloorModifierSetAbridged = Field(
        default=FloorModifierSetAbridged.model_validate(_MOD_SET["floor_set"]),
        description="Global Honeybee FloorModifierSet.",
        frozen=True,
    )

    roof_ceiling_set: RoofCeilingModifierSetAbridged = Field(
        default=RoofCeilingModifierSetAbridged.model_validate(
            _MOD_SET["roof_ceiling_set"]
        ),
        description="Global Honeybee RoofCeilingModifierSet.",
        frozen=True,
    )

    aperture_set: ApertureModifierSetAbridged = Field(
        default=ApertureModifierSetAbridged.model_validate(_MOD_SET["aperture_set"]),
        description="Global Honeybee ApertureModifierSet.",
        frozen=True,
    )

    door_set: DoorModifierSetAbridged = Field(
        default=DoorModifierSetAbridged.model_validate(_MOD_SET["door_set"]),
        description="Global Honeybee DoorModifierSet.",
        frozen=True,
    )

    shade_set: ShadeModifierSetAbridged = Field(
        default=ShadeModifierSetAbridged.model_validate(_MOD_SET["shade_set"]),
        description="Global Honeybee ShadeModifierSet.",
        frozen=True,
    )

    air_boundary_modifier: str = Field(
        default=_MOD_SET["air_boundary_modifier"],
        description="Global Honeybee Modifier for AirBoundary Faces.",
        frozen=True,
    )

    context_modifier: str = Field(
        default="generic_context_0.20",
        description="Global Honeybee Modifier for context Shades.",
        frozen=True,
    )

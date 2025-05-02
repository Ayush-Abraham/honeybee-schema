"""ModifierSet Schema"""

from pydantic import StringConstraints, Field
from .._base import NoExtraBaseModel
from ._base import IDdRadianceBaseModel
from .modifier import _REFERENCE_UNION_MODIFIERS
from typing_extensions import Annotated


class BaseModifierSetAbridged(NoExtraBaseModel):
    """Base class for the abridged modifier sets assigned to Faces."""

    exterior_modifier: str | None = Field(
        default=None,
        description="Identifier for a radiance modifier object for faces with an "
        " Outdoors boundary condition.",
    )

    interior_modifier: str | None = Field(
        default=None,
        description="Identifier for a radiance modifier object for faces with a "
        "boundary condition other than Outdoors.",
    )


class WallModifierSetAbridged(BaseModifierSetAbridged):
    """Abridged set containing radiance modifiers needed for a model's Walls."""

    type: Annotated[str, StringConstraints(pattern="^WallModifierSetAbridged$")] = (
        "WallModifierSetAbridged"
    )


class FloorModifierSetAbridged(BaseModifierSetAbridged):
    """Abridged set containing radiance modifiers needed for a model's Floors."""

    type: Annotated[str, StringConstraints(pattern="^FloorModifierSetAbridged$")] = (
        "FloorModifierSetAbridged"
    )


class RoofCeilingModifierSetAbridged(BaseModifierSetAbridged):
    """Abridged set containing radiance modifiers needed for a model's Roofs."""

    type: Annotated[
        str, StringConstraints(pattern="^RoofCeilingModifierSetAbridged$")
    ] = "RoofCeilingModifierSetAbridged"


class ShadeModifierSetAbridged(BaseModifierSetAbridged):
    """Abridged set containing radiance modifiers needed for a model's Shade."""

    type: Annotated[str, StringConstraints(pattern="^ShadeModifierSetAbridged$")] = (
        "ShadeModifierSetAbridged"
    )


class ApertureModifierSetAbridged(NoExtraBaseModel):
    """Abridged set containing radiance modifiers needed for a model's Apertures."""

    type: Annotated[str, StringConstraints(pattern="^ApertureModifierSetAbridged$")] = (
        "ApertureModifierSetAbridged"
    )

    window_modifier: str | None = Field(
        default=None,
        description="Identifier of modifier object for apertures with an Outdoors "
        "boundary condition, False is_operable property, "
        "and Wall parent Face.",
    )

    interior_modifier: str | None = Field(
        default=None,
        description="Identifier of modifier object for apertures with a Surface "
        "boundary condition.",
    )

    skylight_modifier: str | None = Field(
        default=None,
        description="Identifier of modifier object for apertures with an Outdoors "
        "boundary condition, False is_operable property, and a "
        "RoofCeiling or Floor face type for their parent face.",
    )

    operable_modifier: str | None = Field(
        default=None,
        description="Identifier of modifier object for apertures with an Outdoors "
        "boundary condition and a True is_operable property.",
    )


class DoorModifierSetAbridged(BaseModifierSetAbridged):
    """Abridged set containing radiance modifiers needed for a model's Doors."""

    type: Annotated[str, StringConstraints(pattern="^DoorModifierSetAbridged$")] = (
        "DoorModifierSetAbridged"
    )

    interior_glass_modifier: str | None = Field(
        default=None,
        description="Identifier of modifier object for glass with a Surface "
        "boundary condition.",
    )

    exterior_glass_modifier: str | None = Field(
        default=None,
        description="Identifier of modifier object for glass with an Outdoors "
        "boundary condition.",
    )

    overhead_modifier: str | None = Field(
        default=None,
        description="Identifier of a modifier object for doors with an "
        "Outdoors boundary condition and a RoofCeiling or Floor "
        "face type for their parent face.",
    )


class ModifierSetAbridged(IDdRadianceBaseModel):
    """Abridged set containing all modifiers needed to create a radiance model."""

    type: Annotated[str, StringConstraints(pattern="^ModifierSetAbridged$")] = (
        "ModifierSetAbridged"
    )

    wall_set: WallModifierSetAbridged | None = Field(
        default=None,
        description="Optional WallModifierSet object for this "
        "ModifierSet (default: None).",
    )

    floor_set: FloorModifierSetAbridged | None = Field(
        default=None,
        description="Optional FloorModifierSet object for "
        "this ModifierSet (default: None).",
    )

    roof_ceiling_set: RoofCeilingModifierSetAbridged | None = Field(
        default=None,
        description="Optional RoofCeilingModifierSet object for this "
        "ModifierSet (default: None).",
    )

    aperture_set: ApertureModifierSetAbridged | None = Field(
        default=None,
        description="Optional ApertureModifierSet object for this "
        "ModifierSet (default: None).",
    )

    door_set: DoorModifierSetAbridged | None = Field(
        default=None,
        description="Optional DoorModifierSet object for this "
        "ModifierSet (default: None).",
    )

    shade_set: ShadeModifierSetAbridged | None = Field(
        default=None,
        description="Optional ShadeModifierSet object for this "
        "ModifierSet (default: None).",
    )

    air_boundary_modifier: str | None = Field(
        default=None,
        description="Optional Modifier to be used for all Faces "
        "with an AirBoundary face type. If None, it will be the "
        "honeybee generic air wall modifier.",
    )


class BaseModifierSet(NoExtraBaseModel):
    """Base class for the modifier sets assigned to Faces."""

    exterior_modifier: _REFERENCE_UNION_MODIFIERS | None = Field(
        default=None,
        description="A radiance modifier object for faces with an Outdoors boundary "
        "condition.",
    )

    interior_modifier: _REFERENCE_UNION_MODIFIERS | None = Field(
        default=None,
        description="A radiance modifier object for faces with a boundary condition "
        "other than Outdoors.",
    )


class WallModifierSet(BaseModifierSet):
    """Set containing radiance modifiers needed for a model's Walls."""

    type: Annotated[str, StringConstraints(pattern="^WallModifierSet$")] = (
        "WallModifierSet"
    )


class FloorModifierSet(BaseModifierSet):
    """Set containing radiance modifiers needed for a model's Floors."""

    type: Annotated[str, StringConstraints(pattern="^FloorModifierSet$")] = (
        "FloorModifierSet"
    )


class RoofCeilingModifierSet(BaseModifierSet):
    """Set containing radiance modifiers needed for a model's roofs."""

    type: Annotated[str, StringConstraints(pattern="^RoofCeilingModifierSet$")] = (
        "RoofCeilingModifierSet"
    )


class ShadeModifierSet(BaseModifierSet):
    """Set containing radiance modifiers needed for a model's Shade."""

    type: Annotated[str, StringConstraints(pattern="^ShadeModifierSet$")] = (
        "ShadeModifierSet"
    )


class ApertureModifierSet(NoExtraBaseModel):
    """Set containing radiance modifiers needed for a model's Apertures."""

    type: Annotated[str, StringConstraints(pattern="^ApertureModifierSet$")] = (
        "ApertureModifierSet"
    )

    window_modifier: _REFERENCE_UNION_MODIFIERS | None = Field(
        default=None,
        description="A modifier object for apertures with an Outdoors "
        "boundary condition, False is_operable property, "
        "and Wall parent Face.",
    )

    interior_modifier: _REFERENCE_UNION_MODIFIERS | None = Field(
        default=None,
        description="A modifier object for apertures with a Surface "
        "boundary condition.",
    )

    skylight_modifier: _REFERENCE_UNION_MODIFIERS | None = Field(
        default=None,
        description="A modifier object for apertures with an Outdoors "
        "boundary condition, False is_operable property, and a "
        "RoofCeiling or Floor face type for their parent face.",
    )

    operable_modifier: _REFERENCE_UNION_MODIFIERS | None = Field(
        default=None,
        description="A modifier object for apertures with an Outdoors boundary "
        "condition and a True is_operable property.",
    )


class DoorModifierSet(BaseModifierSet):
    """Set containing radiance modifiers needed for a model's Doors."""

    type: Annotated[str, StringConstraints(pattern="^DoorModifierSet$")] = (
        "DoorModifierSet"
    )

    interior_glass_modifier: _REFERENCE_UNION_MODIFIERS | None = Field(
        default=None,
        description="A modifier object for glass with a Surface boundary condition.",
    )

    exterior_glass_modifier: _REFERENCE_UNION_MODIFIERS | None = Field(
        default=None,
        description="A modifier object for glass with an Outdoors boundary condition.",
    )

    overhead_modifier: _REFERENCE_UNION_MODIFIERS | None = Field(
        default=None,
        description="A window modifier object for doors with an Outdoors boundary "
        "condition and a RoofCeiling or Floor face type for their "
        "parent face.",
    )


class ModifierSet(IDdRadianceBaseModel):
    """Set containing all radiance modifiers needed to create a radiance model."""

    type: Annotated[str, StringConstraints(pattern="^ModifierSet$")] = "ModifierSet"

    wall_set: WallModifierSet | None = Field(
        default=None,
        description="An optional WallModifierSet object for this ModifierSet. "
        "(default: None).",
    )

    floor_set: FloorModifierSet | None = Field(
        default=None,
        description="An optional FloorModifierSet object for this ModifierSet. "
        "(default: None).",
    )

    roof_ceiling_set: RoofCeilingModifierSet | None = Field(
        default=None,
        description="An optional RoofCeilingModifierSet object for this ModifierSet. "
        "(default: None).",
    )

    aperture_set: ApertureModifierSet | None = Field(
        default=None,
        description="An optional ApertureModifierSet object for this ModifierSet. "
        "(default: None).",
    )

    door_set: DoorModifierSet | None = Field(
        default=None,
        description="An optional DoorModifierSet object for this ModifierSet. "
        "(default: None).",
    )

    shade_set: ShadeModifierSet | None = Field(
        default=None,
        description="An optional ShadeModifierSet object for this ModifierSet. "
        "(default: None).",
    )

    air_boundary_modifier: _REFERENCE_UNION_MODIFIERS | None = Field(
        default=None,
        description="An optional Modifier to be used for all Faces with an AirBoundary "
        "face type. If None, it will be the honeybee generic air wall "
        "modifier.",
    )

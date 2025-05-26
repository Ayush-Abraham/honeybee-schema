'''

wall set :   walls to air GF (air=special zone, external walls)
             walls to air upper levels (air=special zone, external walls)
             walls to ground (ground=special zone)
             walls to neighbour (neighbour=special zone)
             walls to other zones (adj zone, internal walls)
             

floor set :  floor to ground (ground=special zone)
             floor to subfloor (subfloor=special zone)
             floor to air (air=special zone)
             floorceiling to adjacent zone ie. midfloor (adj zone)
             floorceiling to neighbour (neighbour=special zone)

roof set:    combined ceiling-roof (raked ceilings)
             ceiling below roofspace (special zone)
             roof over roofspace (pitched roof)

Scratch files have:
41 90: External walls (wall sol-air temperatures) 
91 190: Roofs (roof sol-air temperatures) 
191 240: Floors to outdoors (air temperature) 
241 340: Floors to other zones 
341 440: Ceilings to other zones 
441 490: Walls to other zones 
491 520: Walls within zones 
521 550: Floors to neighbour 
551 580: Ceilings to neighbour 
581 610: Walls to neighbour

hb_energy has interior/exterior/ground subsets of Floor Face Aperture Roof

Can we include roofspace infiltration and subfloor infiltration as part of the templates?
'''
from pydantic import BaseModel, StringConstraints, Field
from construction import ExternalConstruction as ExternalAREConstruction, InternalConstruction as InternalAREConstruction, GlazedConstruction as GlazedAREConstruction

from typing_extensions import Annotated


class NameOptionalIDBase(BaseModel):
    """ Base class when identifier is optinal """
    identifier: str | None = Field(
        default = None,
        description = "unique identifier"
    )

    display_name: str | None = Field(
        default = None,
        description = "Name"
    )

class NameRequiredIDBase(BaseModel):
    """ Base class when identifier is required """
    identifier: str = Field(
        description = "unique identifier"
    )

    display_name: str | None = Field(
        default = None,
        description = "Name"
    )




class WallAREConstructionSet(NameOptionalIDBase):
    """A set of constructions for walls."""
    type: Annotated[str, StringConstraints(pattern="^WallAREConstructionSet$")] = (
        "WallAREConstructionSet"
    )

    wall_to_air_construction: ExternalAREConstruction | None = Field(
        default=None,
        description="An ExternalAREConstruction for walls with an Outdoors boundary condition.",
    )

    wall_to_ground_construction: InternalAREConstruction | None = Field(
        default=None,
        description="An InternalAREConstruction for walls with adjacency to Ground zone",
    )

    wall_to_adj_construction: InternalAREConstruction | None = Field(
        default=None,
        description="An InternalAREConstruction for walls with adjacency to another zone",
    )

    wall_to_neighbour_construction: InternalAREConstruction | None = Field(
        default=None,
        description="An InternalAREConstruction for walls with adjacency to Neighbour zone",
    )

    wall_to_roofspace_construction: InternalAREConstruction | None = Field(
        default=None,
        description="An InternalAREConstruction for walls with adjacency to Roofspace zone",
    )

    wall_to_subfloor_construction: InternalAREConstruction | None = Field(
        default=None,
        description="An InternalAREConstruction for walls with adjacency to Subfloor zone",
    )

class WallAREConstructionSetAbridged(NameOptionalIDBase):
    """A set of constructions for wall, floor, or roof assemblies."""
    type: Annotated[str, StringConstraints(pattern="^WallAREConstructionSetAbridged$")] = (
        "WallAREConstructionSetAbridged"
    )

    wall_to_air_construction: str | None = Field(
        default=None,
        min_length=1,
        max_length=100,
        description="Identifier for an ExternalAREConstruction for walls with an Outdoors boundary condition.",
    )

    wall_to_ground_construction: str | None = Field(
        default=None,
        min_length=1,
        max_length=100,
        description="Identifier for InternalAREConstruction for walls with adjacency to Ground zone",
    )

    wall_to_adj_construction: str | None = Field(
        default=None,
        min_length=1,
        max_length=100,
        description="Identifier for an InternalAREConstruction for walls with adjacency to another zone",
    )

    wall_to_neighbour_construction: str | None = Field(
        default=None,
        min_length=1,
        max_length=100,
        description="Identifier for an InternalAREConstruction for walls with adjacency to Neighbour zone",
    )

    wall_to_roofspace_construction: str | None = Field(
        default=None,
        min_length=1,
        max_length=100,
        description="Identifier for an InternalAREConstruction for walls with adjacency to Roofspace zone",
    )

    wall_to_subfloor_construction: str | None = Field(
        default=None,
        min_length=1,
        max_length=100,
        description="Identifier for an InternalAREConstruction for walls with adjacency to Subfloor zone",
    )


class FloorAREConstructionSet(NameOptionalIDBase):
    """A set of constructions for floors."""
    type: Annotated[str, StringConstraints(pattern="^FloorAREConstructionSet$")] = (
        "FloorAREConstructionSet"
    )

    floor_to_ground_construction: InternalAREConstruction | None = Field(
        default=None,
        description="An InternalAREConstruction for floors with adjacency to Ground zone",
    )

    floor_to_subfloor_construction: InternalAREConstruction | None = Field(
        default=None,
        description="An InternalAREConstruction for floors with adjacency to Subfloor zone",
    )

    floorceiling_to_adj_construction: InternalAREConstruction | None = Field(
        default=None,
        description="An InternalAREConstruction for floorceilings with adjacency to another zone",
    )

    floorceiling_to_neighbour_construction: InternalAREConstruction | None = Field(
        default=None,
        description="An InternalAREConstruction for floorceilings with adjacency to Neighbour zone",
    )

    floor_to_air_construction: ExternalAREConstruction | None = Field(
        default=None,
        description="An ExternalAREConstruction for floors with an Outdoors boundary condition.",
    )

class FloorAREConstructionSetAbridged(NameOptionalIDBase):
    """A set of constructions for floors"""
    type: Annotated[str, StringConstraints(pattern="^FloorAREConstructionSetAbridged$")] = (
        "FloorAREConstructionSetAbridged"
    )
    floor_to_ground_construction: str | None = Field(
        default=None,
        min_length=1,
        max_length=100,
        description="Identifer for an InternalAREConstruction for floors with adjacency to Ground zone",
    )

    floor_to_subfloor_construction: str | None = Field(
        default=None,
        min_length=1,
        max_length=100,
        description="Identifer for an  InternalAREConstruction for floors with adjacency to Subfloor zone",
    )

    floorceiling_to_adj_construction: str | None = Field(
        default=None,
        min_length=1,
        max_length=100,
        description="Identifer for an  InternalAREConstruction for floorceilings with adjacency to another zone",
    )

    floorceiling_to_neighbour_construction: str | None = Field(
        default=None,
        min_length=1,
        max_length=100,
        description="Identifer for an  InternalAREConstruction for floorceilings with adjacency to Neighbour zone",
    )

    floor_to_air_construction: str | None = Field(
        default=None,
        min_length=1,
        max_length=100,
        description="Identifer for an An ExternalAREConstruction for floors with an Outdoors boundary condition.",
    )
    

class RoofCeilingAREConstructionSet(NameOptionalIDBase):
    """A set of constructions for roofs."""
    type: Annotated[str, StringConstraints(pattern="^RoofCeilingAREConstructionSet$")] = (
        "RoofCeilingAREConstructionSet"
    )

    roof_to_roofspace_construction: InternalAREConstruction | None = Field(
        default=None,
        description="An ExternalAREConstruction for roofs with adjacency to Roofspace zone",
    )

    roofceiling_to_zone_construction: InternalAREConstruction | None = Field(
        default=None,
        description="An ExternalAREConstruction for a roof-ceiling with adjacency to an internal zone",
    )

    roofceiling_to_garage_construction: InternalAREConstruction | None = Field(
        default=None,
        description="An ExternalAREConstruction for roof-ceiling with adjacency to a garage zone",
    )

    roofceiling_to_ground_construction: InternalAREConstruction | None = Field(
        default=None,
        description="An ExternalAREConstruction for a roof-ceiling with adjacency to a Ground zone for lower levels cut into slopes",
    )

class RoofCeilingAREConstructionSetAbridged(NameOptionalIDBase):
    """A set of constructions for roofs."""
    type: Annotated[str, StringConstraints(pattern="^RoofCeilingAREConstructionSetAbridged$")] = (
        "RoofCeilingAREConstructionSetAbridged"
    )

    roof_to_roofspace_construction: str | None = Field(
        default=None,
        min_length=1,
        max_length=100,
        description="Identifier for ExternalAREConstruction for roofs with adjacency to Roofspace zone",
    )

    roofceiling_to_zone_construction: str | None = Field(
        default=None,
        min_length=1,
        max_length=100,
        description="Identifier for an ExternalAREConstruction for a roof-ceiling with adjacency to an internal zone",
    )

    #TODO: should there be a roofceiling to garage here for flat/raked garage roofs?
    roofceiling_to_garage_construction: str | None = Field(
        default=None,
        min_length=1,
        max_length=100,
        description="Identifier for an ExternalAREConstruction for roof-ceiling with adjacency to a garage zone",
    )

    roofceiling_to_ground_construction: str | None = Field(
        default=None,
        min_length=1,
        max_length=100,
        description="Identifier for an ExternalAREConstruction for roof-ceiling with adjacency to ground - for lower levels cut into slopes",
    )

    




class DoorAREConstructionSet(NameOptionalIDBase):
    """A set of constructions for external doors."""
    type: Annotated[str, StringConstraints(pattern="^DoorAREConstructionSet$")] = (
        "DoorAREConstructionSet"
    )

    external_solid_door_construction: ExternalAREConstruction | None = Field(
        default=None,
        description="An ExternalAREConstruction for solid external doors",
    )
    
    external_glazed_door_construction: GlazedAREConstruction | None = Field(
        default=None,
        description="A GlazedAREConstruction for glazed external doors",
    )


class DoorAREConstructionSetAbridged(NameOptionalIDBase):
    """A set of constructions for external doors"""
    type: Annotated[str, StringConstraints(pattern="^DoorAREConstructionSetAbridged$")] = (
        "DoorAREConstructionSetAbridged"
    )
    
    external_solid_door_construction: str | None = Field(
        default=None,
        min_length=1,
        max_length=100,
        description="Identifier for an ExternalAREConstruction for a solid external door",
    )

    external_glazed_door_construction: str | None = Field(
        default=None,
        min_length=1,
        max_length=100,
        description="Identifier for an ExternalAREConstruction for a solid external door",
    )

class ApertureAREConstructionSet(NameOptionalIDBase):
    """ A set of constructions for glazed apertures """
    type: Annotated[str, StringConstraints(pattern="^ApertureAREConstructionSet$")] = (
        "ApertureAREConstructionSet"
    )
    window_construction : GlazedAREConstruction | None = Field(
        default=None,
        description="A GlazedAREConstruction for windows",
    )  #TODO: review all categories with Aysh

    sliding_door_construction : GlazedAREConstruction | None = Field(
        default=None,
        description="A GlazedAREConstruction for glazed sliding doors",
    )

class ApertureAREConstructionSetAbridged(NameOptionalIDBase):
    """ A set of constructions for glazed apertures"""
    type: Annotated[str, StringConstraints(pattern="^ApertureAREConstructionSetAbridged$")] = (
        "ApertureAREConstructionSetAbridged"
    )
    window_construction :  str | None = Field(
        default=None,
        min_length=1,
        max_length=100,
        description="Identifier for a GlazedAREConstruction for a window",
    )
    sliding_door_construction :  str | None = Field(
        default=None,
        min_length=1,
        max_length=100,
        description="Identifier for a GlazedAREConstruction for a glazed sliding door",
    )
    












class AREConstructionSetAbridged(NameRequiredIDBase):
    """A set of constructions for different surface types and boundary conditions."""

    type: Annotated[str, StringConstraints(pattern="^AREConstructionSetAbridged$")] = (
        "AREConstructionSetAbridged"
    )

    
    wall_set: WallAREConstructionSetAbridged | None = Field(
        default=None,
        description="A WallAREConstructionSetAbridged object for this ConstructionSet.",
    )

    floor_set: FloorAREConstructionSetAbridged | None = Field(
        default=None,
        description="A FloorAREConstructionSetAbridged object for this ConstructionSet.",
    )

    roof_ceiling_set: RoofCeilingAREConstructionSetAbridged | None = Field(
        default=None,
        description="A RoofCeilingAREConstructionSetAbridged object for this "
        "ConstructionSet.",
    )

    aperture_set: ApertureAREConstructionSetAbridged | None = Field(
        default=None,
        description="A ApertureAREConstructionSetAbridged object for this ConstructionSet.",
    )

    door_set: DoorAREConstructionSetAbridged | None = Field(
        default=None,
        description="A DoorAREConstructionSetAbridged object for this ConstructionSet.",
    )

    


class AREConstructionSet(NameRequiredIDBase):
    """A set of constructions for different surface types and boundary conditions."""

    type: Annotated[str, StringConstraints(pattern="^AREConstructionSet$")] = (
        "AREConstructionSet"
    )

    wall_set: WallAREConstructionSet | None = Field(
        default=None,
        description="A WallAREConstructionSet object for this ConstructionSet.",
    )

    floor_set: FloorAREConstructionSet | None = Field(
        default=None,
        description="A FloorAREConstructionSet object for this ConstructionSet.",
    )

    roof_ceiling_set: RoofCeilingAREConstructionSet | None = Field(
        default=None,
        description="A RoofCeilingAREConstructionSet object for this ConstructionSet.",
    )

    aperture_set: ApertureAREConstructionSet | None = Field(
        default=None,
        description="A ApertureAREConstructionSet object for this ConstructionSet.",
    )

    door_set: DoorAREConstructionSet | None = Field(
        default=None,
        description="A DoorAREConstructionSet object for this ConstructionSet.",
    )

    

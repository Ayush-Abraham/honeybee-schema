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
from pydantic import StringConstraints, Field
from .construction import ExternalConstruction, InternalConstruction, GlazedConstruction

from typing_extensions import Annotated

class WallConstructionSet():
    """A set of constructions for walls."""

    wall_to_air_construction: ExternalConstruction | None = Field(
        default=None,
        description="An ExternalConstruction for walls with an Outdoors boundary condition.",
    )

    wall_to_ground_construction: InternalConstruction | None = Field(
        default=None,
        description="An InternalConstruction for walls with adjacency to Ground zone",
    )

    wall_to_adj_construction: InternalConstruction | None = Field(
        default=None,
        description="An InternalConstruction for walls with adjacency to another zone",
    )

    wall_to_neighbour_construction: InternalConstruction | None = Field(
        default=None,
        description="An InternalConstruction for walls with adjacency to Neighbour zone",
    )

    wall_to_roofspace_construction: InternalConstruction | None = Field(
        default=None,
        description="An InternalConstruction for walls with adjacency to Roofspace zone",
    )

    wall_to_subfloor_construction: InternalConstruction | None = Field(
        default=None,
        description="An InternalConstruction for walls with adjacency to Subfloor zone",
    )

class WallConstructionSetAbridged():
    """A set of constructions for wall, floor, or roof assemblies."""

    wall_to_air_construction: str | None = Field(
        default=None,
        min_length=1,
        max_length=100,
        description="Identifier for an ExternalConstruction for walls with an Outdoors boundary condition.",
    )

    wall_to_ground_construction: str | None = Field(
        default=None,
        min_length=1,
        max_length=100,
        description="Identifier for InternalConstruction for walls with adjacency to Ground zone",
    )

    wall_to_adj_construction: str | None = Field(
        default=None,
        min_length=1,
        max_length=100,
        description="Identifier for an InternalConstruction for walls with adjacency to another zone",
    )

    wall_to_neighbour_construction: str | None = Field(
        default=None,
        min_length=1,
        max_length=100,
        description="Identifier for an InternalConstruction for walls with adjacency to Neighbour zone",
    )

    wall_to_roofspace_construction: str | None = Field(
        default=None,
        min_length=1,
        max_length=100,
        description="Identifier for an InternalConstruction for walls with adjacency to Roofspace zone",
    )

    wall_to_subfloor_construction: str | None = Field(
        default=None,
        min_length=1,
        max_length=100,
        description="Identifier for an InternalConstruction for walls with adjacency to Subfloor zone",
    )


class FloorConstructionSet():
    """A set of constructions for floors."""

    floor_to_ground_construction: InternalConstruction | None = Field(
        default=None,
        description="An InternalConstruction for floors with adjacency to Ground zone",
    )

    floor_to_subfloor_construction: InternalConstruction | None = Field(
        default=None,
        description="An InternalConstruction for floors with adjacency to Subfloor zone",
    )

    floorceiling_to_adj_construction: InternalConstruction | None = Field(
        default=None,
        description="An InternalConstruction for floorceilings with adjacency to another zone",
    )

    floorceiling_to_neighbour_construction: InternalConstruction | None = Field(
        default=None,
        description="An InternalConstruction for floorceilings with adjacency to Neighbour zone",
    )

    floor_to_air_construction: ExternalConstruction | None = Field(
        default=None,
        description="An ExternalConstruction for floors with an Outdoors boundary condition.",
    )

class FloorConstructionSetAbridged():
    """A set of constructions for floors"""
    floor_to_ground_construction: str | None = Field(
        default=None,
        min_length=1,
        max_length=100,
        description="Identifer for an InternalConstruction for floors with adjacency to Ground zone",
    )

    floor_to_subfloor_construction: str | None = Field(
        default=None,
        min_length=1,
        max_length=100,
        description="Identifer for an  InternalConstruction for floors with adjacency to Subfloor zone",
    )

    floorceiling_to_adj_construction: str | None = Field(
        default=None,
        min_length=1,
        max_length=100,
        description="Identifer for an  InternalConstruction for floorceilings with adjacency to another zone",
    )

    floorceiling_to_neighbour_construction: str | None = Field(
        default=None,
        min_length=1,
        max_length=100,
        description="Identifer for an  InternalConstruction for floorceilings with adjacency to Neighbour zone",
    )

    floor_to_air_construction: str | None = Field(
        default=None,
        min_length=1,
        max_length=100,
        description="Identifer for an An ExternalConstruction for floors with an Outdoors boundary condition.",
    )
    

class RoofCeilingConstructionSet():
    """A set of constructions for roofs."""

    roof_to_roofspace_construction: InternalConstruction | None = Field(
        default=None,
        description="An ExternalConstruction for roofs with adjacency to Roofspace zone",
    )

    roofceiling_to_zone_construction: InternalConstruction | None = Field(
        default=None,
        description="An ExternalConstruction for a roof-ceiling with adjacency to an internal zone",
    )

    roofceiling_to_garage_construction: InternalConstruction | None = Field(
        default=None,
        description="An ExternalConstruction for roof-ceiling with adjacency to a garage zone",
    )

    roofceiling_to_ground_construction: InternalConstruction | None = Field(
        default=None,
        description="An ExternalConstruction for a roof-ceiling with adjacency to a Ground zone for lower levels cut into slopes",
    )

class RoofCeilingConstructionSetAbridged():
    """A set of constructions for roofs."""

    roof_to_roofspace_construction: str | None = Field(
        default=None,
        min_length=1,
        max_length=100,
        description="Identifier for ExternalConstruction for roofs with adjacency to Roofspace zone",
    )

    roofceiling_to_zone_construction: str | None = Field(
        default=None,
        min_length=1,
        max_length=100,
        description="Identifier for an ExternalConstruction for a roof-ceiling with adjacency to an internal zone",
    )

    #TODO: should there be a roofceiling to garage here for flat/raked garage roofs?
    roofceiling_to_garage_construction: str | None = Field(
        default=None,
        min_length=1,
        max_length=100,
        description="Identifier for an ExternalConstruction for roof-ceiling with adjacency to a garage zone",
    )

    roofceiling_to_ground_construction: str | None = Field(
        default=None,
        min_length=1,
        max_length=100,
        description="Identifier for an ExternalConstruction for roof-ceiling with adjacency to ground - for lower levels cut into slopes",
    )

    




class DoorConstructionSet():
    """A set of constructions for external doors."""

    external_solid_door_construction: ExternalConstruction | None = Field(
        default=None,
        description="An ExternalConstruction for solid external doors",
    )
    
    external_glazed_door_construction: GlazedConstruction | None = Field(
        default=None,
        description="A GlazedConstruction for glazed external doors",
    )


class DoorConstructionSetAbridged():
    """A set of constructions for external doors"""
    
    external_solid_door_construction: str | None = Field(
        default=None,
        min_length=1,
        max_length=100,
        description="Identifier for an ExternalConstruction for a solid external door",
    )

    external_glazed_door_construction: str | None = Field(
        default=None,
        min_length=1,
        max_length=100,
        description="Identifier for an ExternalConstruction for a solid external door",
    )

class ApertureConstructionSet():
    window_construction : GlazedConstruction | None = Field(
        default=None,
        description="A GlazedConstruction for windows",
    )  #TODO: review all categories with Aysh

    sliding_door_construction : GlazedConstruction | None = Field(
        default=None,
        description="A GlazedConstruction for glazed sliding doors",
    )

class ApertureConstructionSetAbridged():
    window_construction :  str | None = Field(
        default=None,
        min_length=1,
        max_length=100,
        description="Identifier for a GlazedConstruction for a window",
    )
    sliding_door_construction :  str | None = Field(
        default=None,
        min_length=1,
        max_length=100,
        description="Identifier for a GlazedConstruction for a glazed sliding door",
    )
    












class ConstructionSetAbridged():
    """A set of constructions for different surface types and boundary conditions."""

    type: Annotated[str, StringConstraints(pattern="^ConstructionSetAbridged$")] = (
        "ConstructionSetAbridged"
    )

    wall_set: WallConstructionSetAbridged | None = Field(
        default=None,
        description="A WallConstructionSetAbridged object for this ConstructionSet.",
    )

    floor_set: FloorConstructionSetAbridged | None = Field(
        default=None,
        description="A FloorConstructionSetAbridged object for this ConstructionSet.",
    )

    roof_ceiling_set: RoofCeilingConstructionSetAbridged | None = Field(
        default=None,
        description="A RoofCeilingConstructionSetAbridged object for this "
        "ConstructionSet.",
    )

    aperture_set: ApertureConstructionSetAbridged | None = Field(
        default=None,
        description="A ApertureConstructionSetAbridged object for this ConstructionSet.",
    )

    door_set: DoorConstructionSetAbridged | None = Field(
        default=None,
        description="A DoorConstructionSetAbridged object for this ConstructionSet.",
    )

    


class ConstructionSet(ConstructionSetAbridged):
    """A set of constructions for different surface types and boundary conditions."""

    type: Annotated[str, StringConstraints(pattern="^ConstructionSet$")] = (
        "ConstructionSet"
    )

    wall_set: WallConstructionSet | None = Field(
        default=None,
        description="A WallConstructionSet object for this ConstructionSet.",
    )

    floor_set: FloorConstructionSet | None = Field(
        default=None,
        description="A FloorConstructionSet object for this ConstructionSet.",
    )

    roof_ceiling_set: RoofCeilingConstructionSet | None = Field(
        default=None,
        description="A RoofCeilingConstructionSet object for this ConstructionSet.",
    )

    aperture_set: ApertureConstructionSet | None = Field(
        default=None,
        description="A ApertureConstructionSet object for this ConstructionSet.",
    )

    door_set: DoorConstructionSet | None = Field(
        default=None,
        description="A DoorConstructionSet object for this ConstructionSet.",
    )

    

"""Model are properties."""

from pydantic import StringConstraints, Field
from typing import List, Union
from typing_extensions import Annotated

#from .are_elements import ElementType

from .are_project import Project
from .designvariation import DesignVariation
from .global_constructionset import  GlobalConstructionSet
from .constructionset import ConstructionSetAbridged, ConstructionSet
from .are_schema import Dwelling, InternalConstruction, ExternalConstruction, GlazedConstruction,\
                                   InfiltrationPenetration,\
                                   RoofspaceZoneInfiltration, SubfloorZoneInfiltration, \
                                   RoofWindow


from .are_schema import WindowType1, IndoorCoveringType1, OutdoorCoveringType1, \
                       GapSizeType1, RoofExposureType1, LayerDirectionType1, \
                       ZoneType1

#TODO: should we add and track are ids in the model?
#TODO: add base class with id for extension classes
#TODO: add code to match abridged and non abridged classes - see energy extension


class ModelAREProperties():
    type: Annotated[
        str, StringConstraints(pattern="^ModelAREProperties")
    ] = "ModelAREProperties"

    are_project : Project
    are_dwelling : Dwelling

    

    construction_sets: List[Union[ConstructionSetAbridged, ConstructionSet]] | None = (
        Field(
            default=None,
            description="List of all unique ConstructionSets in the Model.",
        )
    )

    are_constructions: (
        List[
            Union[
                InternalConstruction,
                ExternalConstruction,
                GlazedConstruction
            ]
        ]
        | None
    ) = Field(
        default=None,
        description="A list of all unique constructions in the model. This includes "
        "constructions used across all Faces, Apertures, Doors, Shades, Room "
        "ConstructionSets, and the global_construction_set.",
    )

    global_construction_set :  GlobalConstructionSet = Field(
        default = GlobalConstructionSet(),
        description="Global Energy construction set.",
        frozen=True,
    )  # default construction set to use if none is specified explicitly in the model
    
    are_designvariation : DesignVariation


class RoomAREPropertiesAbridged():
    type: Annotated[
        str, StringConstraints(pattern="^RoomAREPropertiesAbridged")
    ] = "RoomAREPropertiesAbridged"

    construction_set: str | None = Field(
        default=None,
        min_length=1,
        max_length=100,
        description="Identifier of a ConstructionSet to specify all default "
        "constructions for the Faces, Apertures, and Doors of the Room. If "
        "None, the Room will use the Model global_construction_set.",
    )  #TODO:  constructions will need to be altered for are for now keep energy extension code

    zonetype: ZoneType1 = Field(
        description = "Zone type of this room"
    )

    is_heated : bool = Field(
        description = "True if room/zone is heated"
    )

    is_cooled : bool = Field(
        description = "True if room/zone is cooled"
    )

    is_reflective : bool | None = Field(
        default = None,
        description = "confirm use of this field I think it is only for roofspaces"
    )  #TODO: confirm use of this field

    roofspace_zoneinfiltration : RoofspaceZoneInfiltration | None = Field(
        default = None,
        description = "If this room/zone is a roofspace, infiltration properties"
    )
    
    subfloor_zoneinfiltration : SubfloorZoneInfiltration | None = Field(
        default = None,
        description = "If this room/zone is a subfloor, infiltration properties"
    )



class FaceAREPropertiesAbridged():
    type: Annotated[
        str, StringConstraints(pattern="^FaceAREPropertiesAbridged")
    ] = "FaceAREPropertiesAbridged"

    construction: str | None = Field(
        default=None,
        min_length=1,
        max_length=100,
        description="identifier for an InternalConstruction or ExternalConstruction representing a wall, roof, floor or ceiling construction",
    )   # TODO:  constructions will need to be altered for are for now keep energy extension code

    opening_area: float = Field(
        ge = 0.0,
        description = "Effective open area of the window when fully open - may not be the same as window area"
    )

    has_insect_screens : bool | None = Field(
        default = True,
        description = "True if openings in the Face have insect screens. None for internal faces"
    )

    infiltration_penetrations : list[InfiltrationPenetration] | None = Field(
        default = None,
        description = "Infiltration (air leakage) penetrations for this face such as lights and fans"
    )

    gross_area : float | None = Field(
        default = None,
        description = "confirm use of this field"
    )  #TODO: confirm use of this field

    opening_area: float = Field(
        ge = 0.0,
        description = "Effective open area of the window when fully open - may not be the same as window area"
    )

    is_opening_controlled : bool = Field(
        description = "True if openings in this face are controlled ie. opened and closed for ventilation"
    )

    are_shadedby_shades : list[str] | None = Field(
        default = None,
        description = "List of ids of detached/orphaned Shades that shade this face - for building are shading relationships"
    )

    are_shadedby_walls : list[str] | None = Field(
        default = None,
        description = "List of ids of External Wall type Faces that shade this face - for building are shading relationships"
    )

    roof_exposure_type : RoofExposureType1 | None = Field(
        default = None,
        description = "Exposure type if this face is a Roof"
    )

    roof_azimuth : float | None = Field(
        default = None, 
        description = "Azimuth of roof normal if this face is a Roof"
    )

    roof_roof_windows : list[RoofWindow] | None = Field(
        default = None,
        description = "List of roof window objects if this face is a Roof"
    )

    externalwall_is_wall_in_courtyard : bool | None = Field(
        default = None,
        description = "confirm use of this field "
    ) #TODO: confirm use of this field

    externalwall_floor_height : float | None = Field(
        default = None,
        description = "Floor height of this wall if the face is an External Wall"
    )  # TODO: confirm use of this field - is it required as an extension property?

    floorceiling_ceiling_floor_height : float | None = Field(
        default = None,
        description = "Height of this fl0or or ceiling if the face is an FloorCeiling"
    )  # TODO: confirm use of this field - is it required as an extension property?

    floorceiling_insulation_r_value : float | None = Field(
        default = None, 
        description = "confirm use of this field"
    )

    floorceiling_level : int | None = Field(
        default = None,
        description = "Level number of this floorceiling"
    )  # TODO: confirm number convention GF = ?? FF = ??

    internalwall_layer_direction_type : LayerDirectionType1 | None = Field(
        default = None,
        description = "For internal walls, which order should the layers in the consstruction be read - forward or backward"
    )


    


class ApertureAREPropertiesAbridged():
    type: Annotated[
        str, StringConstraints(pattern="^ApertureAREPropertiesAbridged")
    ] = "ApertureAREPropertiesAbridged"

    construction: str | None = Field(
        default=None,
        min_length=1,
        max_length=100,
        description="Identifier for a GlazedConstruction representing a window or glazed door construction",
    )   # TODO:  constructions will need to be altered for are for now keep energy extension code

    opening_area: float = Field(
        ge = 0.0,
        description = "Effective open area of the window when fully open - may not be the same as window area"
    )

    openable_percent: int = Field(
        ge = 0,
        description = "When fully open accounting for restrictions due to operator type or safety devices "
                      "what percent of window area is open"
    )

    window_type : WindowType1 = Field(
        description = "Type (operator type) of window in the aperture. "
    )

    has_insect_screens : bool | None = Field(
        default = True,
        description = "True if the window has insect screens"
    )

    is_weather_stripped : bool | None = Field(
        default = True,
        description = "True if the window has weather stripping"
    )

    gap_size_type : GapSizeType1 | None = Field(
        default = GapSizeType1.MEDIUM,
        description = "Gap size type around window frame (construction detail)"
    )

    indoor_covering_type : IndoorCoveringType1 = Field(
        default = IndoorCoveringType1.HOLLAND_BLINDS,
        description = "Indoor covering type over window"
    )
    
    outdoor_covering_type : OutdoorCoveringType1 = Field(
        default = OutdoorCoveringType1.NONE,
        description = "Outdoor covering type over window"
    )




class DoorAREPropertiesAbridged():
    type: Annotated[
        str, StringConstraints(pattern="^DoorAREPropertiesAbridged$")
    ] = "DoorAREPropertiesAbridged"

    construction: str | None = Field(
        default=None,
        min_length=1,
        max_length=100,
        description="Identifier for an ExternalConstruction representing a door construction",
    )   # TODO:  constructions will need to be altered for are for now keep energy extension code

    is_external_door: bool = Field(
        description="True if this door opens to the outdoors"
    )

    is_permanent_opening: bool | None = Field(
        default=False,
        description="True if this is a permanent opening such as an archway"
    )
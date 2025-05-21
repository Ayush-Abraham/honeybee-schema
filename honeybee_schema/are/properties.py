"""Model are properties."""

from pydantic import StringConstraints, Field
from typing_extensions import Annotated

from .are_elements import ElementType
from .window import WindowType, IndoorCoveringType, OutdoorCoveringType
from .infiltration_and_gaps import InfiltrationPenetration, GapSizeType
from .roof import RoofExposureType
from .roofwindow import RoofWindow
from .internal_wall import LayerDirectionType

class FaceAREPropertiesAbridged():
    type: Annotated[
        str, StringConstraints(pattern="^FaceAREPropertiesAbridged")
    ] = "FaceAREPropertiesAbridged"

    construction: str | None = Field(
        default=None,
        min_length=1,
        max_length=100,
        description="",
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
        description = "List of ids of Shades that shade this face - for building are shading relationships"
    )

    are_shadedby_walls : list[str] | None = Field(
        default = None,
        description = "List of ids of External Wall type Faces that shade this face - for building are shading relationships"
    )

    roof_exposure_type : RoofExposureType | None = Field(
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

    internalwall_layer_direction_type : LayerDirectionType | None = Field(
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
        description="",
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

    window_type : WindowType = Field(
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

    gap_size_type : GapSizeType | None = Field(
        default = GapSizeType.medium,
        description = "Gap size type around window frame (construction detail)"
    )

    indoor_covering_type : IndoorCoveringType = Field(
        default = IndoorCoveringType.holland_blinds,
        description = "Indoor covering type over window"
    )
    
    outdoor_covering_type : OutdoorCoveringType = Field(
        default = OutdoorCoveringType.no_outdoorcovering,
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
        description="",
    )   # TODO:  constructions will need to be altered for are for now keep energy extension code

    is_external_door: bool | None = Field(
        default=None,
        description="True if this door opens to the outdoors"
    )

    is_permanent_opening: bool | None = Field(
        default=False,
        description="True if this is a permanent opening such as an archway"
    )
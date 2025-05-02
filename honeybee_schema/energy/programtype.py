"""Programtype Schema"""

from pydantic import StringConstraints, Field

from ._base import IDdEnergyBaseModel
from .load import (
    PeopleAbridged,
    LightingAbridged,
    ElectricEquipmentAbridged,
    GasEquipmentAbridged,
    ServiceHotWaterAbridged,
    InfiltrationAbridged,
    VentilationAbridged,
    SetpointAbridged,
    People,
    Lighting,
    ElectricEquipment,
    GasEquipment,
    ServiceHotWater,
    Infiltration,
    Ventilation,
    Setpoint,
)
from typing_extensions import Annotated


class ProgramTypeAbridged(IDdEnergyBaseModel):
    type: Annotated[str, StringConstraints(pattern="^ProgramTypeAbridged$")] = (
        "ProgramTypeAbridged"
    )

    people: PeopleAbridged | None = Field(
        default=None,
        description="People to describe the occupancy of the program. If None, "
        "no occupancy will be assumed for the program.",
    )

    lighting: LightingAbridged | None = Field(
        default=None,
        description="Lighting to describe the lighting usage of the program. "
        "If None, no lighting will be assumed for the program.",
    )

    electric_equipment: ElectricEquipmentAbridged | None = Field(
        default=None,
        description="ElectricEquipment to describe the usage of electric equipment "
        "within the program. If None, no electric equipment will be assumed.",
    )

    gas_equipment: GasEquipmentAbridged | None = Field(
        default=None,
        description="GasEquipment to describe the usage of gas equipment "
        "within the program. If None, no gas equipment will be assumed.",
    )

    service_hot_water: ServiceHotWaterAbridged | None = Field(
        default=None,
        description="ServiceHotWater object to describe the usage of hot water "
        "within the program. If None, no hot water will be assumed.",
    )

    infiltration: InfiltrationAbridged | None = Field(
        default=None,
        description="Infiltration to describe the outdoor air leakage of "
        "the program. If None, no infiltration will be assumed for the program.",
    )

    ventilation: VentilationAbridged | None = Field(
        default=None,
        description="Ventilation to describe the minimum outdoor air requirement "
        "of the program. If None, no ventilation requirement will be assumed.",
    )

    setpoint: SetpointAbridged | None = Field(
        default=None,
        description="Setpoint object to describe the temperature and humidity setpoints "
        "of the program.  If None, the ProgramType cannot be assigned to a Room "
        "that is conditioned.",
    )


class ProgramType(ProgramTypeAbridged):
    type: Annotated[str, StringConstraints(pattern="^ProgramType$")] = "ProgramType"

    people: People | None = Field(
        default=None,
        description="People to describe the occupancy of the program. If None, "
        "no occupancy will be assumed for the program.",
    )

    lighting: Lighting | None = Field(
        default=None,
        description="Lighting to describe the lighting usage of the program. "
        "If None, no lighting will be assumed for the program.",
    )

    electric_equipment: ElectricEquipment | None = Field(
        default=None,
        description="ElectricEquipment to describe the usage of electric equipment "
        "within the program. If None, no electric equipment will be assumed.",
    )

    gas_equipment: GasEquipment | None = Field(
        default=None,
        description="GasEquipment to describe the usage of gas equipment "
        "within the program. If None, no gas equipment will be assumed.",
    )

    service_hot_water: ServiceHotWater | None = Field(
        default=None,
        description="ServiceHotWater object to describe the usage of hot water "
        "within the program. If None, no hot water will be assumed.",
    )

    infiltration: Infiltration | None = Field(
        default=None,
        description="Infiltration to describe the outdoor air leakage of "
        "the program. If None, no infiltration will be assumed for the program.",
    )

    ventilation: Ventilation | None = Field(
        default=None,
        description="Ventilation to describe the minimum outdoor air requirement "
        "of the program. If None, no ventilation requirement will be assumed.",
    )

    setpoint: Setpoint | None = Field(
        default=None,
        description="Setpoint object to describe the temperature and humidity setpoints "
        "of the program.  If None, the ProgramType cannot be assigned to a Room "
        "that is conditioned.",
    )

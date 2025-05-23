"""Ventilative cooling Schema"""
from pydantic import StringConstraints, Field

from .._base import NoExtraBaseModel
from ._base import EnergyBaseModel
from enum import Enum
from typing_extensions import Annotated


class VentilationControlAbridged(NoExtraBaseModel):

    type: Annotated[str, StringConstraints(pattern='^VentilationControlAbridged$')] = 'VentilationControlAbridged'

    min_indoor_temperature: float = Field(
        -100,
        ge=-100,
        le=100,
        description='A number for the minimum indoor temperature at which to '
        'ventilate in Celsius. Typically, this variable is used to initiate ventilation.'
    )

    max_indoor_temperature: float = Field(
        100,
        ge=-100,
        le=100,
        description='A number for the maximum indoor temperature at which to '
        'ventilate in Celsius. This can be used to set a maximum temperature at '
        'which point ventilation is stopped and a cooling system is turned on.'
    )

    min_outdoor_temperature: float = Field(
        -100,
        ge=-100,
        le=100,
        description='A number for the minimum outdoor temperature at which to ventilate '
        'in Celsius. This can be used to ensure ventilative cooling does not happen '
        'during the winter even if the Room is above the min_indoor_temperature.'
    )

    max_outdoor_temperature: float = Field(
        100,
        ge=-100,
        le=100,
        description='A number for the maximum indoor temperature at which to ventilate '
        'in Celsius. This can be used to set a limit for when it is considered too hot '
        'outside for ventilative cooling.'
    )

    delta_temperature: float = Field(
        -100,
        ge=-100,
        le=100,
        description='A number for the temperature differential in Celsius between '
        'indoor and outdoor below which ventilation is shut off.  This should usually '
        'be a positive number so that ventilation only occurs when the outdoors is '
        'cooler than the indoors. Negative numbers indicate how much hotter the '
        'outdoors can be than the indoors before ventilation is stopped.'
    )

    schedule: str = Field(
        default=None,
        min_length=1,
        max_length=100,
        description='Identifier of the schedule for the ventilation over the course of '
        'the year. Note that this is applied on top of any setpoints. The type of this '
        'schedule should be On/Off and values should be either 0 (no possibility of '
        'ventilation) or 1 (ventilation possible).'
    )


class VentilationType(str, Enum):
    exhaust = 'Exhaust'
    intake = 'Intake'
    balanced = 'Balanced'


class VentilationFan(EnergyBaseModel):

    type: Annotated[str, StringConstraints(pattern='^VentilationFan$')] = 'VentilationFan'

    flow_rate: float = Field(
        ...,
        gt=0,
        description='A number for the flow rate of the fan in m3/s.'
    )

    ventilation_type: VentilationType = Field(
        default=VentilationType.balanced,
        description='Text to indicate the type of type of ventilation. Choose '
        'from the options below. For either Exhaust or Intake, values for '
        'fan pressure and efficiency define the fan electric consumption. For Exhaust '
        'ventilation, the conditions of the air entering the space are assumed '
        'to be equivalent to outside air conditions. For Intake and Balanced '
        'ventilation, an appropriate amount of fan heat is added to the '
        'entering air stream. For Balanced ventilation, both an intake fan '
        'and an exhaust fan are assumed to co-exist, both having the same '
        'flow rate and power consumption (using the entered values for fan '
        'pressure rise and fan total efficiency). Thus, the fan electric '
        'consumption for Balanced ventilation is twice that for the Exhaust or '
        'Intake ventilation types which employ only a single fan.'
    )

    pressure_rise: float = Field(
        ...,
        gt=0,
        description='A number for the the pressure rise across the fan in Pascals '
        '(N/m2). This is often a function of the fan speed and the conditions in '
        'which the fan is operating since having the fan blow air through filters '
        'or narrow ducts will increase the pressure rise that is needed to '
        'deliver the input flow rate. The pressure rise plays an important role in '
        'determining the amount of energy consumed by the fan. Smaller fans like '
        'a 0.05 m3/s desk fan tend to have lower pressure rises around 60 Pa. '
        'Larger fans, such as a 6 m3/s fan used for ventilating a large room tend '
        'to have higher pressure rises around 400 Pa. The highest pressure rises '
        'are typically for large fans blowing air through ducts and filters, which '
        'can have pressure rises as high as 1000 Pa.'
    )

    efficiency: float = Field(
        ...,
        ge=0,
        le=1,
        description='A number between 0 and 1 for the overall efficiency of the fan. '
        'Specifically, this is the ratio of the power delivered to the fluid '
        'to the electrical input power. It is the product of the fan motor '
        'efficiency and the fan impeller efficiency. Fans that have a higher blade '
        'diameter and operate at lower speeds with smaller pressure rises for '
        'their size tend to have higher efficiencies. Because motor efficiencies '
        'are typically between 0.8 and 0.9, the best overall fan efficiencies '
        'tend to be around 0.7 with most typical fan efficiencies between 0.5 and '
        '0.7. The lowest efficiencies often happen for small fans in situations '
        'with high pressure rises for their size, which can result in efficiencies '
        'as low as 0.15.'
    )

    control: VentilationControlAbridged = Field(
        default=None,
        description='A VentilationControl object that dictates the conditions under '
        'which the fan is turned on. If None, a default VentilationControl will '
        'be generated, which will keep the fan on all of the time.'
    )


class VentilationOpening(NoExtraBaseModel):

    type: Annotated[str, StringConstraints(pattern='^VentilationOpening$')] = 'VentilationOpening'

    fraction_area_operable: float = Field(
        0.5,
        ge=0,
        le=1,
        description='A number for the fraction of the window area that is operable.'
    )

    fraction_height_operable: float = Field(
        1.0,
        ge=0,
        le=1,
        description='A number for the fraction of the distance from the bottom of the '
        'window to the top that is operable'
    )

    discharge_coefficient: float = Field(
        0.45,
        ge=0,
        le=1,
        description='A number that will be multiplied by the area of the window in the '
        'stack (buoyancy-driven) part of the equation to account for additional '
        'friction from window geometry, insect screens, etc. Typical values include '
        '0.45, for unobstructed windows WITH insect screens and 0.65 for unobstructed '
        'windows WITHOUT insect screens. This value should be lowered if windows are '
        'of an awning or casement type and are not allowed to fully open.'
    )

    wind_cross_vent: bool = Field(
        False,
        description='Boolean to indicate if there is an opening of roughly equal area '
        'on the opposite side of the Room such that wind-driven cross ventilation will '
        'be induced. If False, the assumption is that the operable area is primarily on '
        'one side of the Room and there is no wind-driven ventilation.'
    )

    flow_coefficient_closed: float = Field(
        default=0,
        ge=0,
        description='An optional number in kg/s-m, at 1 Pa per meter of crack length, '
        'used to calculate the mass flow rate when the opening is closed; required to '
        'run an AirflowNetwork simulation. The DesignBuilder Cracks template defines '
        'the flow coefficient for a tight, low-leakage closed external window to be '
        '0.00001, and the flow coefficient for a very poor, high-leakage closed '
        'external window to be 0.003.'
    )

    flow_exponent_closed: float = Field(
        default=0.65,
        ge=0.5,
        le=1,
        description='An optional dimensionless number between 0.5 and 1 used to '
        'calculate the mass flow rate when the opening is closed; required to run an '
        'AirflowNetwork simulation. This value represents the leak geometry impact '
        'on airflow, with 0.5 generally corresponding to turbulent orifice flow and 1 '
        'generally corresponding to laminar flow. The default of 0.65 is '
        'representative of many cases of wall and window leakage, used when the '
        'exponent cannot be measured.'
    )

    two_way_threshold: float = Field(
        default=0.0001,
        gt=0,
        description='A number in kg/m3 indicating the minimum density difference above '
        'which two-way flow may occur due to stack effect, required to run an '
        'AirflowNetwork simulation. This value is required because the air density '
        'difference between two zones (which drives two-way air flow) will tend '
        'towards division by zero errors as the air density difference approaches '
        'zero. The default of 0.0001 is a typical default value used for AirflowNetwork '
        'openings.'
    )


class AFNCrack(NoExtraBaseModel):
    """Properties for airflow through a crack."""

    type: Annotated[str, StringConstraints(pattern='^AFNCrack$')] = 'AFNCrack'

    flow_coefficient: float = Field(
        ...,
        gt=0,
        description='A number in kg/s-m at 1 Pa per meter of crack length at the '
        'conditions defined in the ReferenceCrack condition; required to run an '
        'AirflowNetwork simulation. The DesignBuilder Cracks template defines the flow '
        'coefficient for a tight, low-leakage wall to be 0.00001 and 0.001 for external '
        'and internal constructions, respectively. Flow coefficients for a very poor, '
        'high-leakage wall are defined to be 0.0004 and 0.019 for external and internal '
        'constructions, respectively.'
    )

    flow_exponent: float = Field(
        default=0.65,
        ge=0.5,
        le=1,
        description='An optional dimensionless number between 0.5 and 1 used to '
        'calculate the crack mass flow rate; required to run an '
        'AirflowNetwork simulation. This value represents the leak geometry impact '
        'on airflow, with 0.5 generally corresponding to turbulent orifice flow and 1 '
        'generally corresponding to laminar flow. The default of 0.65 is '
        'representative of many cases of wall and window leakage, used when the '
        'exponent cannot be measured.'
    )


class VentilationControlType(str, Enum):
    single_zone = 'SingleZone'
    multi_zone_with_distribution = 'MultiZoneWithDistribution'
    multi_zone_without_distribution = 'MultiZoneWithoutDistribution'


class BuildingType(str, Enum):
    lowrise = 'LowRise'
    highrise = 'HighRise'


class VentilationSimulationControl(NoExtraBaseModel):
    """The global parameters used in the ventilation simulation."""

    type: Annotated[str, StringConstraints(pattern='^VentilationSimulationControl$')] = 'VentilationSimulationControl'

    vent_control_type: VentilationControlType = Field(
        default=VentilationControlType.single_zone,
        description='Text indicating type of ventilation control. Choices are: '
        'SingleZone, MultiZoneWithDistribution, MultiZoneWithoutDistribution. The '
        'MultiZone options will model air flow with the AirflowNetwork model, which '
        'is generally more accurate then the SingleZone option, but will take '
        'considerably longer to simulate, and requires defining more ventilation '
        'parameters to explicitly account for weather and building-induced pressure '
        'differences, and the leakage geometry corresponding to specific windows, '
        'doors, and surface cracks.'
    )

    reference_temperature: float = Field(
        default=20,
        ge=-273.15,
        description='Reference temperature measurement in Celsius under which the '
        'surface crack data were obtained.'
    )

    reference_pressure: float = Field(
        default=101325,
        ge=31000,
        le=120000,
        description='Reference barometric pressure measurement in Pascals under which '
        'the surface crack data were obtained.'
    )

    reference_humidity_ratio: float = Field(
        default=0,
        ge=0,
        description='Reference humidity ratio measurement in kgWater/kgDryAir under '
        'which the surface crack data were obtained.'
    )

    building_type: BuildingType = Field(
        default=BuildingType.lowrise,
        description='Text indicating relationship between building footprint and '
        'height used to calculate the wind pressure coefficients for exterior surfaces.'
        'Choices are: LowRise and HighRise. LowRise corresponds to rectangular building '
        'whose height is less then three times the width and length of the footprint. '
        'HighRise corresponds to a rectangular building whose height is more than three '
        'times the width and length of the footprint. This parameter is required to '
        'automatically calculate wind pressure coefficients for the AirflowNetwork '
        'simulation. If used for complex building geometries that cannot be described '
        'as a highrise or lowrise rectangular mass, the resulting air flow and pressure '
        'simulated on the building surfaces may be inaccurate.'
    )

    long_axis_angle: float = Field(
        default=0,
        ge=0,
        le=180,
        description='The clockwise rotation in degrees from true North of the long axis '
        'of the building. This parameter is required to automatically calculate wind '
        'pressure coefficients for the AirflowNetwork simulation. If used for complex '
        'building geometries that cannot be described as a highrise or lowrise '
        'rectangular mass, the resulting air flow and pressure simulated on the '
        'building surfaces may be inaccurate.'
    )

    aspect_ratio: float = Field(
        default=1,
        gt=0,
        le=1,
        description='Aspect ratio of a rectangular footprint, defined as the ratio of '
        'length of the short axis divided by the length of the long axis. This '
        'parameter is required to automatically calculate wind '
        'pressure coefficients for the AirflowNetwork simulation. If used for complex '
        'building geometries that cannot be described as a highrise or lowrise '
        'rectangular mass, the resulting air flow and pressure simulated on the '
        'building surfaces may be inaccurate.'
    )

from pydantic import (
    Field
)

from .are_schema import PlanDocument, Assessor, Client, Acknowledgement, \
                        SimulationConfiguration
from .are_schema import BuildingClassType1, AccuRateEngineVersion1, \
                        ChenathEngineVersion1, DeclarationOfInterestType1

class Project():
    name : str | None = Field(
        default = None,
        description = "Project name"
    )
    code : str | None = Field(
        default = None,
        description = "Project description"
    )
    additional_information : str | None = Field(
        default = None,
        description = "Additional project information"
    )
    default_design_variation_id : str | None = Field(
        default = None,
        description = "Default design variation id"
    )
    building_class_type : BuildingClassType1 = Field(
        description = "Building class"
    )
    accurate_engine_version : AccuRateEngineVersion1 = Field(
        description = "AccuRate engine version"
    )
    chenath_engine_version : ChenathEngineVersion1 = Field(
        description = "Chenath engine version"
    )
    declaration_of_interest_type : DeclarationOfInterestType1 = Field(
        description = "Declaration of interest type"
    )
    plan_document : PlanDocument | None = Field(
        default = None,
        description = "Plan document"
    )
    assessor : Assessor | None = Field(
        default = None,
        description = "Assessor details"
    )
    client : Client | None = Field(
        default = None,
        description = "Client details"
    )
    acknowledgement : Acknowledgement | None = Field(
        default = None,
        description = "Acknowledgement"
    )
    simulation_configuration : SimulationConfiguration | None = Field(
        default = None,
        description = "Simulation configuration info"
    )

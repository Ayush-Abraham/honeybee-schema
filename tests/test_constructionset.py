from honeybee_schema.energy.constructionset import (
    ConstructionSetAbridged,
    WallConstructionSetAbridged,
    RoofCeilingConstructionSetAbridged,
    FloorConstructionSetAbridged,
    ApertureConstructionSetAbridged,
    DoorConstructionSetAbridged,
    ConstructionSet,
)
import os

# target folder where all of the samples live
root = os.path.dirname(os.path.dirname(__file__))
target_folder = os.path.join(root, "samples", "construction_set")


def test_constructionset_complete_0():
    file_path = os.path.join(target_folder, "constructionset_abridged_complete.json")
    # ConstructionSetAbridged.parse_file(file_path)
    with open(file_path) as file:
        json_data = file.read()
    ConstructionSetAbridged.model_validate_json(json_data)


def test_constructionset_partial_exterior_0():
    file_path = os.path.join(
        target_folder, "constructionset_abridged_partial_exterior.json"
    )
    # ConstructionSetAbridged.parse_file(file_path)
    with open(file_path) as file:
        json_data = file.read()
    ConstructionSetAbridged.model_validate_json(json_data)


def test_constructionset_complete_1():
    file_path = os.path.join(target_folder, "constructionset_complete.json")
    # ConstructionSet.parse_file(file_path)
    with open(file_path) as file:
        json_data = file.read()
    ConstructionSet.model_validate_json(json_data)


def test_constructionset_partial_exterior_1():
    file_path = os.path.join(target_folder, "constructionset_partial_exterior.json")
    # ConstructionSet.parse_file(file_path)
    with open(file_path) as file:
        json_data = file.read()
    ConstructionSet.model_validate_json(json_data)

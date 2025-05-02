from honeybee_schema.energy.programtype import ProgramTypeAbridged, ProgramType
import os

# target folder where all of the samples live
root = os.path.dirname(os.path.dirname(__file__))
target_folder = os.path.join(root, "samples", "program_type")


def test_program_type_abridged_plenum():
    file_path = os.path.join(target_folder, "program_type_abridged_plenum.json")
    # ProgramTypeAbridged.parse_file(file_path)
    with open(file_path) as file:
        json_data = file.read()
    ProgramTypeAbridged.model_validate_json(json_data)


def test_program_type_abridged_office():
    file_path = os.path.join(target_folder, "program_type_abridged_office.json")
    # ProgramTypeAbridged.parse_file(file_path)
    with open(file_path) as file:
        json_data = file.read()
    ProgramTypeAbridged.model_validate_json(json_data)


def test_program_type_abridged_kitchen():
    file_path = os.path.join(target_folder, "program_type_abridged_kitchen.json")
    # ProgramTypeAbridged.parse_file(file_path)
    with open(file_path) as file:
        json_data = file.read()
    ProgramTypeAbridged.model_validate_json(json_data)


def test_program_type_abridged_patient_room():
    file_path = os.path.join(target_folder, "program_type_abridged_patient_room.json")
    # ProgramTypeAbridged.parse_file(file_path)
    with open(file_path) as file:
        json_data = file.read()
    ProgramTypeAbridged.model_validate_json(json_data)


def test_program_type_plenum():
    file_path = os.path.join(target_folder, "program_type_plenum.json")
    # ProgramType.parse_file(file_path)
    with open(file_path) as file:
        json_data = file.read()
    ProgramType.model_validate_json(json_data)


def test_program_type_office():
    file_path = os.path.join(target_folder, "program_type_office.json")
    # ProgramType.parse_file(file_path)
    with open(file_path) as file:
        json_data = file.read()
    ProgramType.model_validate_json(json_data)

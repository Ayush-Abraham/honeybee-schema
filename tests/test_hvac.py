from honeybee_schema.energy.hvac.idealair import IdealAirSystemAbridged
from honeybee_schema.energy.hvac.allair import VAV
from honeybee_schema.energy.hvac.doas import FCUwithDOASAbridged
from honeybee_schema.energy.hvac.heatcool import WindowAC
import os

# target folder where all of the samples live
root = os.path.dirname(os.path.dirname(__file__))
target_folder = os.path.join(root, "samples", "hvac")


def test_ideal_air_default():
    file_path = os.path.join(target_folder, "ideal_air_default.json")
    # IdealAirSystemAbridged.parse_file(file_path)
    with open(file_path) as file:
        json_data = file.read()
    IdealAirSystemAbridged.model_validate_json(json_data)


def test_ideal_air_detailed():
    file_path = os.path.join(target_folder, "ideal_air_detailed.json")
    # IdealAirSystemAbridged.parse_file(file_path)
    with open(file_path) as file:
        json_data = file.read()
    IdealAirSystemAbridged.model_validate_json(json_data)


def test_vav_template():
    file_path = os.path.join(target_folder, "vav_template.json")
    # VAV.parse_file(file_path)
    with open(file_path) as file:
        json_data = file.read()
    VAV.model_validate_json(json_data)


def test_fcu_with_doas_template():
    file_path = os.path.join(target_folder, "fcu_with_doas_template.json")
    # FCUwithDOASAbridged.parse_file(file_path)
    with open(file_path) as file:
        json_data = file.read()
    FCUwithDOASAbridged.model_validate_json(json_data)


def test_window_ac_with_baseboard_template():
    file_path = os.path.join(target_folder, "window_ac_with_baseboard_template.json")
    # WindowAC.parse_file(file_path)
    with open(file_path) as file:
        json_data = file.read()
    WindowAC.model_validate_json(json_data)

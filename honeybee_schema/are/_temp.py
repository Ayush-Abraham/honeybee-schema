# TODO: remove this file - it is temporary to save reinstalling the library to the test environment while testing

from constructionset import    ExternalConstruction, InternalConstruction, GlazedConstruction,\
                                ConstructionSet, ConstructionSetAbridged, \
                                WallConstructionSet, FloorConstructionSet, RoofCeilingConstructionSet, ApertureConstructionSet, DoorConstructionSet,\
                                WallConstructionSetAbridged, FloorConstructionSetAbridged, RoofCeilingConstructionSetAbridged, ApertureConstructionSetAbridged,  DoorConstructionSetAbridged


def create_sample_construction_sets(samples_folder):
    # minimal set of constructions
    sample_external_wall_construction = ExternalConstruction()
    sample_internal_wall_construction = InternalConstruction()
    sample_external_floor_construction = ExternalConstruction()
    sample_internal_floor_construction = InternalConstruction()
    sample_external_roof_construction = ExternalConstruction()
    sample_glazed_construction = GlazedConstruction()
    sample_external_door_construction = ExternalConstruction()
    sample_glazed_door_construction = GlazedConstruction()



    wall_set = WallConstructionSet()
    wall_set.wall_to_air_construction = sample_external_wall_construction
    wall_set.wall_to_adj_construction = sample_internal_wall_construction
    wall_set.wall_to_ground_construction = sample_internal_wall_construction
    wall_set.wall_to_neighbour_construction = sample_internal_wall_construction
    wall_set.wall_to_roofspace_construction = sample_internal_wall_construction
    wall_set.wall_to_subfloor_construction = sample_internal_wall_construction

    floor_set = FloorConstructionSet()
    floor_set.floor_to_air_construction = sample_external_floor_construction
    floor_set.floor_to_ground_construction = sample_external_floor_construction
    floor_set.floor_to_subfloor_construction = sample_internal_floor_construction
    floor_set.floorceiling_to_adj_construction = sample_internal_floor_construction
    floor_set.floorceiling_to_neighbour_construction = sample_internal_floor_construction

    roof_ceiling_set = RoofCeilingConstructionSet()
    roof_ceiling_set.roof_to_roofspace_construction = sample_external_roof_construction
    roof_ceiling_set.roofceiling_to_garage_construction = sample_external_roof_construction
    roof_ceiling_set.roofceiling_to_ground_construction = sample_external_roof_construction
    roof_ceiling_set.roofceiling_to_zone_construction = sample_external_roof_construction

    aperture_set = ApertureConstructionSet()
    aperture_set.window_construction = sample_glazed_construction
    aperture_set.sliding_door_construction = sample_glazed_construction

    door_set = DoorConstructionSet()
    door_set.external_solid_door_construction = sample_external_door_construction
    door_set.external_glazed_door_construction = sample_glazed_door_construction


    sample_construction_set = ConstructionSet()
    sample_construction_set.type = "ConstructionSet"
    sample_construction_set.wall_set = wall_set
    sample_construction_set.floor_set = floor_set
    sample_construction_set.roof_ceiling_set = roof_ceiling_set
    sample_construction_set.aperture_set = aperture_set
    sample_construction_set.door_set = door_set
    
    return sample_construction_set

def create_sample_abridged_construction_sets(samples_folder):

    wall_set = WallConstructionSetAbridged()
    wall_set.wall_to_air_construction = "sample_external_wall_construction"
    wall_set.wall_to_adj_construction = "sample_internal_wall_construction"
    wall_set.wall_to_ground_construction = "sample_internal_wall_construction"
    wall_set.wall_to_neighbour_construction = "sample_internal_wall_construction"
    wall_set.wall_to_roofspace_construction = "sample_internal_wall_construction"
    wall_set.wall_to_subfloor_construction = "sample_internal_wall_construction"

    floor_set = FloorConstructionSetAbridged()
    floor_set.floor_to_air_construction = "sample_external_floor_construction"
    floor_set.floor_to_ground_construction = "sample_external_floor_construction"
    floor_set.floor_to_subfloor_construction = "sample_internal_floor_construction"
    floor_set.floorceiling_to_adj_construction = "sample_internal_floor_construction"
    floor_set.floorceiling_to_neighbour_construction = "sample_internal_floor_construction"

    roof_ceiling_set = RoofCeilingConstructionSetAbridged()
    roof_ceiling_set.roof_to_roofspace_construction = "sample_external_roof_construction"
    roof_ceiling_set.roofceiling_to_garage_construction = "sample_external_roof_construction"
    roof_ceiling_set.roofceiling_to_ground_construction = "sample_external_roof_construction"
    roof_ceiling_set.roofceiling_to_zone_construction = "sample_external_roof_construction"

    aperture_set = ApertureConstructionSetAbridged()
    aperture_set.window_construction = "sample_glazed_construction"
    aperture_set.sliding_door_construction = "sample_glazed_construction"

    door_set = DoorConstructionSetAbridged()
    door_set.external_solid_door_construction = "sample_external_door_construction"
    door_set.external_glazed_door_construction = "sample_glazed_door_construction"

    sample_abridged_construction_set = ConstructionSetAbridged()
    sample_abridged_construction_set.type = "ConstructionSetAbridged"

    return sample_abridged_construction_set



if __name__ == '__main__':
    this_cs = create_sample_abridged_construction_sets()
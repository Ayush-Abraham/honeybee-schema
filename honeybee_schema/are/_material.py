from enum import Enum

''' In ARE materials are referenced by their integer id and come from a 
    pre-defined list - this can be retrieved from the API

    NOTE: the LibraryMaterial class here is not part of the ARE schema - it is for reading the material library retrieved from the API
          to refer to a material, use its index value (int)
    
    TODO: move this file from the schema to another location

'''



    
class LibraryMaterial():
    index : int
    name : str
    level1_name : str
    level2_name : str
    capacitance : int
    res_u : float
    res_d : float
    thick_req : bool
    thick_fix : bool
    thickness : int
    density : float
    cp : float
    comment : str
    insulation_conductivity : float
    airgap_e : float


    def from_dict(self, mat_dict):
        self.index =                    mat_dict["Index"]
        self.name =                     mat_dict["Name"]
        self.level1_name =              mat_dict["Level_1_Name"]
        self.level2_name =              mat_dict["Level_2_Name"]
        self.capacitance =              mat_dict["Capacitance"]
        self.res_u =                    mat_dict["ResU"]
        self.res_d =                    mat_dict["ResD"]
        self.thick_req =                mat_dict["ThickReq"]
        self.thick_fix =                mat_dict["ThickFix"]
        self.thickness =                mat_dict["Thickness"]
        self.density =                  mat_dict["Density"]
        self.cp =                       mat_dict["Cp"]
        self.comment =                  mat_dict["Comment"]
        self.insulation_conductivity =  mat_dict["InsulationConductivity"]
        self.airgap_e =                 mat_dict["AirGapE"]

     
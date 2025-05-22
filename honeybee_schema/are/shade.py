from enum import Enum


'''
Shading in ARE is different to honeybee - label each shade with a shade object type to assist in processing and 
collect references to shades that apply to each element under each element either as child objects of Face, Window
or in extended properties of Face: ARE_ShadedBy_Shades
'''

class ShadeType(str, Enum):
    eave = "Eave"
    overhang_balcony = "Overhang or Balcony"
    pergola = "Pergola"
    roof_over_outdoor_area = "Roof Over Outdoor Area"
    fence = "Fence"
    neighbouring_structure = "Neighbouring Structure"
    fixed_awning = "Fixed Awning"
    other_shade = "Other shade"
from pydantic import (
    Field
)
from typing import List, Union, Annotated
from enum import Enum


from typing_extensions import Annotated


class WindowType(str, Enum):
    awning = "Awning"
    casement = "Casement"
    double_or_single_hung = "Double or Single Hung"
    louvre = "Louvre"
    sliding = "Sliding"
    other = "Other"

class IndoorCoveringType(str, Enum):
    no_indoorcovering = "No Indoor Covering"
    open_weave = "Open Weave"
    closed_weave = "Closed Weave"
    heavy_drapes = "Heavy Drapes"
    curtains_and_pelmets = "Curtains and Pelmets"
    heavy_drapes_and_pelments = "Heavy Drapes and Pelmets"
    holland_blinds = "Holland Blinds"
    venetian_blinds = "Venetian Blinds"

class OutdoorCoveringType(str, Enum):
    no_outdoorcovering = "No Outdoor Covering"
    roller_shutters = "Roller Shutters"
    canvas_awning_closed = "Canvas Awning Closed"
    canvas_awning_vented = "Canvas Awning Vented"
    miniature_louvres = "Miniature Louvres"
    outdoor_venetians = "Outdoor Venetians"
    forty_percent_shade_cloth = "40pc Shade Cloth"
    sixty_percent_shade_cloth = "60pc Shade Cloth"
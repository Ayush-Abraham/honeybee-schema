"""Objects used as alternatives to numerical properties."""

from typing import Annotated

from pydantic import constr, StringConstraints
from ._base import NoExtraBaseModel


class NoLimit(NoExtraBaseModel):
    type: Annotated[str, StringConstraints(pattern="^NoLimit$")] = "NoLimit"


class Autocalculate(NoExtraBaseModel):
    type: Annotated[str, StringConstraints(pattern="^Autocalculate$")] = "Autocalculate"


class Autosize(NoExtraBaseModel):
    type: Annotated[str, StringConstraints(pattern="^Autosize$")] = "Autosize"

"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from pypazy.models.components import patchedorganism as components_patchedorganism
from pypazy.types import BaseModel
from pypazy.utils import FieldMetadata, PathParamMetadata, RequestMetadata
from typing import Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class PartialUpdateOrganismRequestTypedDict(TypedDict):
    id: str
    patched_organism: NotRequired[components_patchedorganism.PatchedOrganismTypedDict]
    

class PartialUpdateOrganismRequest(BaseModel):
    id: Annotated[str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))]
    patched_organism: Annotated[Optional[components_patchedorganism.PatchedOrganism], FieldMetadata(request=RequestMetadata(media_type="application/json"))] = None
    
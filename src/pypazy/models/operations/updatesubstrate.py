"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from pypazy.models.components import substrate_input as components_substrate_input
from pypazy.types import BaseModel
from pypazy.utils import FieldMetadata, PathParamMetadata, RequestMetadata
from typing import TypedDict
from typing_extensions import Annotated


class UpdateSubstrateRequestTypedDict(TypedDict):
    id: str
    substrate: components_substrate_input.SubstrateInputTypedDict
    

class UpdateSubstrateRequest(BaseModel):
    id: Annotated[str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))]
    substrate: Annotated[components_substrate_input.SubstrateInput, FieldMetadata(request=RequestMetadata(media_type="application/json"))]
    

"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from pypazy.models.components import dataset_input as components_dataset_input
from pypazy.types import BaseModel
from pypazy.utils import FieldMetadata, PathParamMetadata, RequestMetadata
from typing import TypedDict
from typing_extensions import Annotated


class UpdateDatasetRequestTypedDict(TypedDict):
    id: str
    dataset: components_dataset_input.DatasetInputTypedDict
    

class UpdateDatasetRequest(BaseModel):
    id: Annotated[str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))]
    dataset: Annotated[components_dataset_input.DatasetInput, FieldMetadata(request=RequestMetadata(media_type="application/json"))]
    

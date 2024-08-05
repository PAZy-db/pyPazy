"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .proteinsequence_input import ProteinSequenceInput, ProteinSequenceInputTypedDict
from pypazy.types import BaseModel
from pypazy.utils import FieldMetadata, FormMetadata, MultipartFormMetadata
from typing import List, TypedDict
from typing_extensions import Annotated


class DatasetInputTypedDict(TypedDict):
    protein: List[ProteinSequenceInputTypedDict]
    accession: str
    database: str
    

class DatasetInput(BaseModel):
    protein: Annotated[List[ProteinSequenceInput], FieldMetadata(form=FormMetadata(json=True), multipart=MultipartFormMetadata(json=True))]
    accession: Annotated[str, FieldMetadata(form=True, multipart=True)]
    database: Annotated[str, FieldMetadata(form=True, multipart=True)]
    
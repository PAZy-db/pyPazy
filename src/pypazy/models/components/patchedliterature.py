"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from pypazy.types import BaseModel
from pypazy.utils import FieldMetadata
from typing import Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class PatchedLiteratureTypedDict(TypedDict):
    doi: NotRequired[str]
    title: NotRequired[str]
    authors: NotRequired[str]
    journal: NotRequired[str]
    year: NotRequired[int]
    

class PatchedLiterature(BaseModel):
    doi: Annotated[Optional[str], FieldMetadata(form=True, multipart=True)] = None
    title: Annotated[Optional[str], FieldMetadata(form=True, multipart=True)] = None
    authors: Annotated[Optional[str], FieldMetadata(form=True, multipart=True)] = None
    journal: Annotated[Optional[str], FieldMetadata(form=True, multipart=True)] = None
    year: Annotated[Optional[int], FieldMetadata(form=True, multipart=True)] = None
    
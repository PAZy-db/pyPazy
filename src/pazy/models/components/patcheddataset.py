"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .proteinsequence_input import ProteinSequenceInput
from dataclasses_json import Undefined, dataclass_json
from pazy import utils
from typing import List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PatchedDataset:
    protein: Optional[List[ProteinSequenceInput]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('protein'), 'exclude': lambda f: f is None }, 'form': { 'field_name': 'protein', 'json': True }, 'multipart_form': { 'field_name': 'protein', 'json': True }})
    accession: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('accession'), 'exclude': lambda f: f is None }, 'form': { 'field_name': 'accession' }, 'multipart_form': { 'field_name': 'accession' }})
    database: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('database'), 'exclude': lambda f: f is None }, 'form': { 'field_name': 'database' }, 'multipart_form': { 'field_name': 'database' }})
    


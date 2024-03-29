"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .proteinsequence_input import ProteinSequenceInput
from dataclasses_json import Undefined, dataclass_json
from pazy import utils
from typing import List


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DatasetInput:
    protein: List[ProteinSequenceInput] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('protein') }, 'form': { 'field_name': 'protein', 'json': True }, 'multipart_form': { 'field_name': 'protein', 'json': True }})
    accession: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('accession') }, 'form': { 'field_name': 'accession' }, 'multipart_form': { 'field_name': 'accession' }})
    database: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('database') }, 'form': { 'field_name': 'database' }, 'multipart_form': { 'field_name': 'database' }})
    


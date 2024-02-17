"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .literature_input import LiteratureInput
from .organism_input import OrganismInput
from .substrate_input import SubstrateInput
from dataclasses_json import Undefined, dataclass_json
from pazy import utils
from typing import List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ProteinSequenceInput:
    organisms: List[OrganismInput] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('organisms') }, 'form': { 'field_name': 'organisms', 'json': True }, 'multipart_form': { 'field_name': 'organisms', 'json': True }})
    substrates: List[SubstrateInput] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('substrates') }, 'form': { 'field_name': 'substrates', 'json': True }, 'multipart_form': { 'field_name': 'substrates', 'json': True }})
    literature: List[LiteratureInput] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('literature') }, 'form': { 'field_name': 'literature', 'json': True }, 'multipart_form': { 'field_name': 'literature', 'json': True }})
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }, 'form': { 'field_name': 'name' }, 'multipart_form': { 'field_name': 'name' }})
    amino_acid_sequence: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('amino_acid_sequence'), 'exclude': lambda f: f is None }, 'form': { 'field_name': 'amino_acid_sequence' }, 'multipart_form': { 'field_name': 'amino_acid_sequence' }})
    verified_activity: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('verified_activity'), 'exclude': lambda f: f is None }, 'form': { 'field_name': 'verified_activity' }, 'multipart_form': { 'field_name': 'verified_activity' }})
    

"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from pazy import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class LiteratureInput:
    doi: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('doi') }, 'form': { 'field_name': 'doi' }, 'multipart_form': { 'field_name': 'doi' }})
    title: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('title') }, 'form': { 'field_name': 'title' }, 'multipart_form': { 'field_name': 'title' }})
    authors: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('authors') }, 'form': { 'field_name': 'authors' }, 'multipart_form': { 'field_name': 'authors' }})
    journal: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('journal') }, 'form': { 'field_name': 'journal' }, 'multipart_form': { 'field_name': 'journal' }})
    year: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('year') }, 'form': { 'field_name': 'year' }, 'multipart_form': { 'field_name': 'year' }})
    


# Proteins
(*proteins*)

### Available Operations

* [get_protein_sequences](#get_protein_sequences) - Returns all ProteinSequences
* [add_protein_sequence](#add_protein_sequence) - Adds a new ProteinSequence to the database.
* [get_protein_sequence_by_id](#get_protein_sequence_by_id) - Returns a ProteinSequence for a given ProteinSequence ID.
* [update_protein_sequence](#update_protein_sequence) - Updates a ProteinSequence for a given ProteinSequence ID.
* [partial_update_protein_sequence](#partial_update_protein_sequence) - Partially updates a ProteinSequence for a given ProteinSequence ID.
* [delete_protein_sequence](#delete_protein_sequence) - Deletes a ProteinSequence from the database.

## get_protein_sequences

Returns all ProteinSequences

### Example Usage

```python
import pazy
from pazy.models import components

s = pazy.Pazy(
    security=components.Security(
        username="<YOUR_USERNAME_HERE>",
    ),
)


res = s.proteins.get_protein_sequences()

if res.protein_sequences is not None:
    # handle response
    pass

```


### Response

**[operations.GetProteinSequencesResponse](../../models/operations/getproteinsequencesresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## add_protein_sequence

Adds a new ProteinSequence to the database.

### Example Usage

```python
import pazy
from pazy.models import components

s = pazy.Pazy(
    security=components.Security(
        username="<YOUR_USERNAME_HERE>",
    ),
)

req = components.ProteinSequenceInput(
    organisms=[
        components.OrganismInput(
            scientific_name='<value>',
        ),
    ],
    substrates=[
        components.SubstrateInput(
            name='<value>',
            abbreviation='<value>',
        ),
    ],
    literature=[
        components.LiteratureInput(
            doi='<value>',
            title='<value>',
            authors='<value>',
            journal='<value>',
            year=78070,
        ),
    ],
    name='<value>',
)

res = s.proteins.add_protein_sequence(req)

if res.protein_sequence is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [components.ProteinSequenceInput](../../models/components/proteinsequenceinput.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |


### Response

**[operations.AddProteinSequenceResponse](../../models/operations/addproteinsequenceresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_protein_sequence_by_id

Returns a ProteinSequence for a given ProteinSequence ID.

### Example Usage

```python
import pazy
from pazy.models import components

s = pazy.Pazy(
    security=components.Security(
        username="<YOUR_USERNAME_HERE>",
    ),
)


res = s.proteins.get_protein_sequence_by_id(id='<value>')

if res.protein_sequence is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.GetProteinSequenceByIDResponse](../../models/operations/getproteinsequencebyidresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## update_protein_sequence

Updates a ProteinSequence for a given ProteinSequence ID.

### Example Usage

```python
import pazy
from pazy.models import components

s = pazy.Pazy(
    security=components.Security(
        username="<YOUR_USERNAME_HERE>",
    ),
)


res = s.proteins.update_protein_sequence(id='<value>', protein_sequence=components.ProteinSequenceInput(
    organisms=[
        components.OrganismInput(
            scientific_name='<value>',
        ),
    ],
    substrates=[
        components.SubstrateInput(
            name='<value>',
            abbreviation='<value>',
        ),
    ],
    literature=[
        components.LiteratureInput(
            doi='<value>',
            title='<value>',
            authors='<value>',
            journal='<value>',
            year=956230,
        ),
    ],
    name='<value>',
))

if res.protein_sequence is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `id`                                                                               | *str*                                                                              | :heavy_check_mark:                                                                 | N/A                                                                                |
| `protein_sequence`                                                                 | [components.ProteinSequenceInput](../../models/components/proteinsequenceinput.md) | :heavy_check_mark:                                                                 | N/A                                                                                |


### Response

**[operations.UpdateProteinSequenceResponse](../../models/operations/updateproteinsequenceresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## partial_update_protein_sequence

Partially updates a ProteinSequence for a given ProteinSequence ID.

### Example Usage

```python
import pazy
from pazy.models import components

s = pazy.Pazy(
    security=components.Security(
        username="<YOUR_USERNAME_HERE>",
    ),
)


res = s.proteins.partial_update_protein_sequence(id='<value>', patched_protein_sequence=components.PatchedProteinSequence())

if res.protein_sequence is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `id`                                                                                             | *str*                                                                                            | :heavy_check_mark:                                                                               | N/A                                                                                              |
| `patched_protein_sequence`                                                                       | [Optional[components.PatchedProteinSequence]](../../models/components/patchedproteinsequence.md) | :heavy_minus_sign:                                                                               | N/A                                                                                              |


### Response

**[operations.PartialUpdateProteinSequenceResponse](../../models/operations/partialupdateproteinsequenceresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## delete_protein_sequence

Deletes a ProteinSequence from the database.

### Example Usage

```python
import pazy
from pazy.models import components

s = pazy.Pazy(
    security=components.Security(
        username="<YOUR_USERNAME_HERE>",
    ),
)


res = s.proteins.delete_protein_sequence(id='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.DeleteProteinSequenceResponse](../../models/operations/deleteproteinsequenceresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

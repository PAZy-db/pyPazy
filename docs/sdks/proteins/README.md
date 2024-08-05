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
from pypazy import Pazy
from pypazy.models import components

s = Pazy(
    security=components.Security(
        username="",
        password="",
    ),
)


res = s.proteins.get_protein_sequences()

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `limit`                                                             | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | Number of results to return per page.                               |
| `offset`                                                            | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | The initial index from which to return the results.                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |


### Response

**[components.PaginatedProteinSequenceList](../../models/components/paginatedproteinsequencelist.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## add_protein_sequence

Adds a new ProteinSequence to the database.

### Example Usage

```python
from pypazy import Pazy
from pypazy.models import components

s = Pazy(
    security=components.Security(
        username="",
        password="",
    ),
)


res = s.proteins.add_protein_sequence(request={
    "organisms": [
        {
            "scientific_name": "<value>",
        },
    ],
    "substrates": [
        {
            "name": "<value>",
            "abbreviation": "<value>",
        },
    ],
    "literature": [
        {
            "doi": "<value>",
            "title": "<value>",
            "authors": "<value>",
            "journal": "<value>",
            "year": 78070,
        },
    ],
    "name": "<value>",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [components.ProteinSequenceInput](../../models/components/proteinsequenceinput.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |
| `retries`                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                   | :heavy_minus_sign:                                                                 | Configuration to override the default retry behavior of the client.                |


### Response

**[components.ProteinSequence](../../models/components/proteinsequence.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_protein_sequence_by_id

Returns a ProteinSequence for a given ProteinSequence ID.

### Example Usage

```python
from pypazy import Pazy
from pypazy.models import components

s = Pazy(
    security=components.Security(
        username="",
        password="",
    ),
)


res = s.proteins.get_protein_sequence_by_id(id="<value>")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |


### Response

**[components.ProteinSequence](../../models/components/proteinsequence.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## update_protein_sequence

Updates a ProteinSequence for a given ProteinSequence ID.

### Example Usage

```python
from pypazy import Pazy
from pypazy.models import components

s = Pazy(
    security=components.Security(
        username="",
        password="",
    ),
)


res = s.proteins.update_protein_sequence(id="<value>", protein_sequence={
    "organisms": [
        {
            "scientific_name": "<value>",
        },
    ],
    "substrates": [
        {
            "name": "<value>",
            "abbreviation": "<value>",
        },
    ],
    "literature": [
        {
            "doi": "<value>",
            "title": "<value>",
            "authors": "<value>",
            "journal": "<value>",
            "year": 956230,
        },
    ],
    "name": "<value>",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `id`                                                                               | *str*                                                                              | :heavy_check_mark:                                                                 | N/A                                                                                |
| `protein_sequence`                                                                 | [components.ProteinSequenceInput](../../models/components/proteinsequenceinput.md) | :heavy_check_mark:                                                                 | N/A                                                                                |
| `retries`                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                   | :heavy_minus_sign:                                                                 | Configuration to override the default retry behavior of the client.                |


### Response

**[components.ProteinSequence](../../models/components/proteinsequence.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## partial_update_protein_sequence

Partially updates a ProteinSequence for a given ProteinSequence ID.

### Example Usage

```python
from pypazy import Pazy
from pypazy.models import components

s = Pazy(
    security=components.Security(
        username="",
        password="",
    ),
)


res = s.proteins.partial_update_protein_sequence(id="<value>")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `id`                                                                                             | *str*                                                                                            | :heavy_check_mark:                                                                               | N/A                                                                                              |
| `patched_protein_sequence`                                                                       | [Optional[components.PatchedProteinSequence]](../../models/components/patchedproteinsequence.md) | :heavy_minus_sign:                                                                               | N/A                                                                                              |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |


### Response

**[components.ProteinSequence](../../models/components/proteinsequence.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## delete_protein_sequence

Deletes a ProteinSequence from the database.

### Example Usage

```python
from pypazy import Pazy
from pypazy.models import components

s = Pazy(
    security=components.Security(
        username="",
        password="",
    ),
)


s.proteins.delete_protein_sequence(id="<value>")

# Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

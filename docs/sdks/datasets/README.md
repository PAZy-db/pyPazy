# Datasets
(*datasets*)

### Available Operations

* [get_datasets](#get_datasets) - Returns all Datasets
* [add_dataset](#add_dataset) - Adds a new Dataset to the database.
* [get_dataset_by_id](#get_dataset_by_id) - Returns a Dataset for a given Dataset ID.
* [update_dataset](#update_dataset) - Updates a Dataset for a given Dataset ID.
* [partial_update_dataset](#partial_update_dataset) - Partially updates a Dataset for a given Dataset ID.
* [delete_dataset](#delete_dataset) - Deletes a Dataset from the database.

## get_datasets

Returns all Datasets

### Example Usage

```python
import pazy
from pazy.models import components

s = pazy.Pazy(
    security=components.Security(
        username="<YOUR_USERNAME_HERE>",
    ),
)


res = s.datasets.get_datasets()

if res.datasets is not None:
    # handle response
    pass
```


### Response

**[operations.GetDatasetsResponse](../../models/operations/getdatasetsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## add_dataset

Adds a new Dataset to the database.

### Example Usage

```python
import pazy
from pazy.models import components

s = pazy.Pazy(
    security=components.Security(
        username="<YOUR_USERNAME_HERE>",
    ),
)

req = components.DatasetInput(
    protein=[
        components.ProteinSequenceInput(
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
                    year=924105,
                ),
            ],
            name='<value>',
        ),
    ],
    accession='<value>',
    database='<value>',
)

res = s.datasets.add_dataset(req)

if res.dataset is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                          | Type                                                               | Required                                                           | Description                                                        |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `request`                                                          | [components.DatasetInput](../../models/components/datasetinput.md) | :heavy_check_mark:                                                 | The request object to use for the request.                         |


### Response

**[operations.AddDatasetResponse](../../models/operations/adddatasetresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_dataset_by_id

Returns a Dataset for a given Dataset ID.

### Example Usage

```python
import pazy
from pazy.models import components

s = pazy.Pazy(
    security=components.Security(
        username="<YOUR_USERNAME_HERE>",
    ),
)


res = s.datasets.get_dataset_by_id(id='<value>')

if res.dataset is not None:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.GetDatasetByIDResponse](../../models/operations/getdatasetbyidresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## update_dataset

Updates a Dataset for a given Dataset ID.

### Example Usage

```python
import pazy
from pazy.models import components

s = pazy.Pazy(
    security=components.Security(
        username="<YOUR_USERNAME_HERE>",
    ),
)


res = s.datasets.update_dataset(id='<value>', dataset=components.DatasetInput(
    protein=[
        components.ProteinSequenceInput(
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
                    year=897277,
                ),
            ],
            name='<value>',
        ),
    ],
    accession='<value>',
    database='<value>',
))

if res.dataset is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                          | Type                                                               | Required                                                           | Description                                                        |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `id`                                                               | *str*                                                              | :heavy_check_mark:                                                 | N/A                                                                |
| `dataset`                                                          | [components.DatasetInput](../../models/components/datasetinput.md) | :heavy_check_mark:                                                 | N/A                                                                |


### Response

**[operations.UpdateDatasetResponse](../../models/operations/updatedatasetresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## partial_update_dataset

Partially updates a Dataset for a given Dataset ID.

### Example Usage

```python
import pazy
from pazy.models import components

s = pazy.Pazy(
    security=components.Security(
        username="<YOUR_USERNAME_HERE>",
    ),
)


res = s.datasets.partial_update_dataset(id='<value>', patched_dataset=components.PatchedDataset())

if res.dataset is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `id`                                                                             | *str*                                                                            | :heavy_check_mark:                                                               | N/A                                                                              |
| `patched_dataset`                                                                | [Optional[components.PatchedDataset]](../../models/components/patcheddataset.md) | :heavy_minus_sign:                                                               | N/A                                                                              |


### Response

**[operations.PartialUpdateDatasetResponse](../../models/operations/partialupdatedatasetresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## delete_dataset

Deletes a Dataset from the database.

### Example Usage

```python
import pazy
from pazy.models import components

s = pazy.Pazy(
    security=components.Security(
        username="<YOUR_USERNAME_HERE>",
    ),
)


res = s.datasets.delete_dataset(id='<value>')

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.DeleteDatasetResponse](../../models/operations/deletedatasetresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

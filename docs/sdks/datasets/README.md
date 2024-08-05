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
from pypazy import Pazy
from pypazy.models import components

s = Pazy(
    security=components.Security(
        username="",
        password="",
    ),
)


res = s.datasets.get_datasets()

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

**[components.PaginatedDatasetList](../../models/components/paginateddatasetlist.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## add_dataset

Adds a new Dataset to the database.

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


res = s.datasets.add_dataset(request={
    "protein": [
        {
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
                    "year": 924105,
                },
            ],
            "name": "<value>",
        },
    ],
    "accession": "<value>",
    "database": "<value>",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [components.DatasetInput](../../models/components/datasetinput.md)  | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |


### Response

**[components.Dataset](../../models/components/dataset.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_dataset_by_id

Returns a Dataset for a given Dataset ID.

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


res = s.datasets.get_dataset_by_id(id="<value>")

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

**[components.Dataset](../../models/components/dataset.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## update_dataset

Updates a Dataset for a given Dataset ID.

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


res = s.datasets.update_dataset(id="<value>", dataset={
    "protein": [
        {
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
                    "year": 897277,
                },
            ],
            "name": "<value>",
        },
    ],
    "accession": "<value>",
    "database": "<value>",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `dataset`                                                           | [components.DatasetInput](../../models/components/datasetinput.md)  | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |


### Response

**[components.Dataset](../../models/components/dataset.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## partial_update_dataset

Partially updates a Dataset for a given Dataset ID.

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


res = s.datasets.partial_update_dataset(id="<value>")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `id`                                                                             | *str*                                                                            | :heavy_check_mark:                                                               | N/A                                                                              |
| `patched_dataset`                                                                | [Optional[components.PatchedDataset]](../../models/components/patcheddataset.md) | :heavy_minus_sign:                                                               | N/A                                                                              |
| `retries`                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                 | :heavy_minus_sign:                                                               | Configuration to override the default retry behavior of the client.              |


### Response

**[components.Dataset](../../models/components/dataset.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## delete_dataset

Deletes a Dataset from the database.

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


s.datasets.delete_dataset(id="<value>")

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

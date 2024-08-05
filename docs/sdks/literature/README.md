# Literature
(*literature*)

### Available Operations

* [get_literatures](#get_literatures) - Returns all Literatures
* [add_literature](#add_literature) - Adds a new Literature to the database.
* [get_literature_by_id](#get_literature_by_id) - Returns a Literature for a given Literature ID.
* [update_literature](#update_literature) - Updates a Literature for a given Literature ID.
* [partial_update_literature](#partial_update_literature) - Partially updates a Literature for a given Literature ID.
* [delete_literature](#delete_literature) - Deletes a Literature from the database.

## get_literatures

Returns all Literatures

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


res = s.literature.get_literatures()

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

**[components.PaginatedLiteratureList](../../models/components/paginatedliteraturelist.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## add_literature

Adds a new Literature to the database.

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


res = s.literature.add_literature(request={
    "doi": "<value>",
    "title": "<value>",
    "authors": "<value>",
    "journal": "<value>",
    "year": 531038,
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `request`                                                                | [components.LiteratureInput](../../models/components/literatureinput.md) | :heavy_check_mark:                                                       | The request object to use for the request.                               |
| `retries`                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)         | :heavy_minus_sign:                                                       | Configuration to override the default retry behavior of the client.      |


### Response

**[components.Literature](../../models/components/literature.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_literature_by_id

Returns a Literature for a given Literature ID.

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


res = s.literature.get_literature_by_id(id="<value>")

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

**[components.Literature](../../models/components/literature.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## update_literature

Updates a Literature for a given Literature ID.

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


res = s.literature.update_literature(id="<value>", literature={
    "doi": "<value>",
    "title": "<value>",
    "authors": "<value>",
    "journal": "<value>",
    "year": 696699,
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `id`                                                                     | *str*                                                                    | :heavy_check_mark:                                                       | N/A                                                                      |
| `literature`                                                             | [components.LiteratureInput](../../models/components/literatureinput.md) | :heavy_check_mark:                                                       | N/A                                                                      |
| `retries`                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)         | :heavy_minus_sign:                                                       | Configuration to override the default retry behavior of the client.      |


### Response

**[components.Literature](../../models/components/literature.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## partial_update_literature

Partially updates a Literature for a given Literature ID.

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


res = s.literature.partial_update_literature(id="<value>")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `id`                                                                                   | *str*                                                                                  | :heavy_check_mark:                                                                     | N/A                                                                                    |
| `patched_literature`                                                                   | [Optional[components.PatchedLiterature]](../../models/components/patchedliterature.md) | :heavy_minus_sign:                                                                     | N/A                                                                                    |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |


### Response

**[components.Literature](../../models/components/literature.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## delete_literature

Deletes a Literature from the database.

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


s.literature.delete_literature(id="<value>")

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

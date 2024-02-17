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
import pazy
from pazy.models import components

s = pazy.Pazy(
    security=components.Security(
        username="<YOUR_USERNAME_HERE>",
    ),
)


res = s.literature.get_literatures()

if res.literature is not None:
    # handle response
    pass
```


### Response

**[operations.GetLiteraturesResponse](../../models/operations/getliteraturesresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## add_literature

Adds a new Literature to the database.

### Example Usage

```python
import pazy
from pazy.models import components

s = pazy.Pazy(
    security=components.Security(
        username="<YOUR_USERNAME_HERE>",
    ),
)

req = components.LiteratureInput(
    doi='<value>',
    title='<value>',
    authors='<value>',
    journal='<value>',
    year=531038,
)

res = s.literature.add_literature(req)

if res.literature is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `request`                                                                | [components.LiteratureInput](../../models/components/literatureinput.md) | :heavy_check_mark:                                                       | The request object to use for the request.                               |


### Response

**[operations.AddLiteratureResponse](../../models/operations/addliteratureresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_literature_by_id

Returns a Literature for a given Literature ID.

### Example Usage

```python
import pazy
from pazy.models import components

s = pazy.Pazy(
    security=components.Security(
        username="<YOUR_USERNAME_HERE>",
    ),
)


res = s.literature.get_literature_by_id(id='<value>')

if res.literature is not None:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.GetLiteratureByIDResponse](../../models/operations/getliteraturebyidresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## update_literature

Updates a Literature for a given Literature ID.

### Example Usage

```python
import pazy
from pazy.models import components

s = pazy.Pazy(
    security=components.Security(
        username="<YOUR_USERNAME_HERE>",
    ),
)


res = s.literature.update_literature(id='<value>', literature=components.LiteratureInput(
    doi='<value>',
    title='<value>',
    authors='<value>',
    journal='<value>',
    year=696699,
))

if res.literature is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `id`                                                                     | *str*                                                                    | :heavy_check_mark:                                                       | N/A                                                                      |
| `literature`                                                             | [components.LiteratureInput](../../models/components/literatureinput.md) | :heavy_check_mark:                                                       | N/A                                                                      |


### Response

**[operations.UpdateLiteratureResponse](../../models/operations/updateliteratureresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## partial_update_literature

Partially updates a Literature for a given Literature ID.

### Example Usage

```python
import pazy
from pazy.models import components

s = pazy.Pazy(
    security=components.Security(
        username="<YOUR_USERNAME_HERE>",
    ),
)


res = s.literature.partial_update_literature(id='<value>', patched_literature=components.PatchedLiterature())

if res.literature is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `id`                                                                                   | *str*                                                                                  | :heavy_check_mark:                                                                     | N/A                                                                                    |
| `patched_literature`                                                                   | [Optional[components.PatchedLiterature]](../../models/components/patchedliterature.md) | :heavy_minus_sign:                                                                     | N/A                                                                                    |


### Response

**[operations.PartialUpdateLiteratureResponse](../../models/operations/partialupdateliteratureresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## delete_literature

Deletes a Literature from the database.

### Example Usage

```python
import pazy
from pazy.models import components

s = pazy.Pazy(
    security=components.Security(
        username="<YOUR_USERNAME_HERE>",
    ),
)


res = s.literature.delete_literature(id='<value>')

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.DeleteLiteratureResponse](../../models/operations/deleteliteratureresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

# Substrates
(*substrates*)

### Available Operations

* [get_substrates](#get_substrates) - Returns all Substrates
* [add_substrate](#add_substrate) - Adds a new Substrate to the database.
* [get_substrate_by_id](#get_substrate_by_id) - Returns a Substrate for a given Substrate ID.
* [update_substrate](#update_substrate) - Updates a Substrate for a given Substrate ID.
* [partial_update_substrate](#partial_update_substrate) - Partially updates a Substrate for a given Substrate ID.
* [delete_substrate](#delete_substrate) - Deletes a Substrate from the database.

## get_substrates

Returns all Substrates

### Example Usage

```python
import pazy
from pazy.models import components

s = pazy.Pazy(
    security=components.Security(
        username="<YOUR_USERNAME_HERE>",
    ),
)


res = s.substrates.get_substrates()

if res.substrates is not None:
    # handle response
    pass
```


### Response

**[operations.GetSubstratesResponse](../../models/operations/getsubstratesresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## add_substrate

Adds a new Substrate to the database.

### Example Usage

```python
import pazy
from pazy.models import components

s = pazy.Pazy(
    security=components.Security(
        username="<YOUR_USERNAME_HERE>",
    ),
)

req = components.SubstrateInput(
    name='<value>',
    abbreviation='<value>',
)

res = s.substrates.add_substrate(req)

if res.substrate is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                              | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `request`                                                              | [components.SubstrateInput](../../models/components/substrateinput.md) | :heavy_check_mark:                                                     | The request object to use for the request.                             |


### Response

**[operations.AddSubstrateResponse](../../models/operations/addsubstrateresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_substrate_by_id

Returns a Substrate for a given Substrate ID.

### Example Usage

```python
import pazy
from pazy.models import components

s = pazy.Pazy(
    security=components.Security(
        username="<YOUR_USERNAME_HERE>",
    ),
)


res = s.substrates.get_substrate_by_id(id='<value>')

if res.substrate is not None:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.GetSubstrateByIDResponse](../../models/operations/getsubstratebyidresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## update_substrate

Updates a Substrate for a given Substrate ID.

### Example Usage

```python
import pazy
from pazy.models import components

s = pazy.Pazy(
    security=components.Security(
        username="<YOUR_USERNAME_HERE>",
    ),
)


res = s.substrates.update_substrate(id='<value>', substrate=components.SubstrateInput(
    name='<value>',
    abbreviation='<value>',
))

if res.substrate is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                              | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `id`                                                                   | *str*                                                                  | :heavy_check_mark:                                                     | N/A                                                                    |
| `substrate`                                                            | [components.SubstrateInput](../../models/components/substrateinput.md) | :heavy_check_mark:                                                     | N/A                                                                    |


### Response

**[operations.UpdateSubstrateResponse](../../models/operations/updatesubstrateresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## partial_update_substrate

Partially updates a Substrate for a given Substrate ID.

### Example Usage

```python
import pazy
from pazy.models import components

s = pazy.Pazy(
    security=components.Security(
        username="<YOUR_USERNAME_HERE>",
    ),
)


res = s.substrates.partial_update_substrate(id='<value>', patched_substrate=components.PatchedSubstrate())

if res.substrate is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `id`                                                                                 | *str*                                                                                | :heavy_check_mark:                                                                   | N/A                                                                                  |
| `patched_substrate`                                                                  | [Optional[components.PatchedSubstrate]](../../models/components/patchedsubstrate.md) | :heavy_minus_sign:                                                                   | N/A                                                                                  |


### Response

**[operations.PartialUpdateSubstrateResponse](../../models/operations/partialupdatesubstrateresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## delete_substrate

Deletes a Substrate from the database.

### Example Usage

```python
import pazy
from pazy.models import components

s = pazy.Pazy(
    security=components.Security(
        username="<YOUR_USERNAME_HERE>",
    ),
)


res = s.substrates.delete_substrate(id='<value>')

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.DeleteSubstrateResponse](../../models/operations/deletesubstrateresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

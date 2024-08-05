# Organisms
(*organisms*)

### Available Operations

* [get_organisms](#get_organisms) - Returns all Organisms
* [add_organism](#add_organism) - Adds a new Organism to the database.
* [get_organism_by_id](#get_organism_by_id) - Returns a Organism for a given Organism ID.
* [update_organism](#update_organism) - Updates a Organism for a given Organism ID.
* [partial_update_organism](#partial_update_organism) - Partially updates a Organism for a given Organism ID.
* [delete_organism](#delete_organism) - Deletes a Organism from the database.

## get_organisms

Returns all Organisms

### Example Usage

```python
import pazy
from pazy.models import components

s = pazy.Pazy(
    security=components.Security(
        username="<YOUR_USERNAME_HERE>",
    ),
)


res = s.organisms.get_organisms()

if res.organisms is not None:
    # handle response
    pass

```


### Response

**[operations.GetOrganismsResponse](../../models/operations/getorganismsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## add_organism

Adds a new Organism to the database.

### Example Usage

```python
import pazy
from pazy.models import components

s = pazy.Pazy(
    security=components.Security(
        username="<YOUR_USERNAME_HERE>",
    ),
)

req = components.OrganismInput(
    scientific_name='<value>',
)

res = s.organisms.add_organism(req)

if res.organism is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                            | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `request`                                                            | [components.OrganismInput](../../models/components/organisminput.md) | :heavy_check_mark:                                                   | The request object to use for the request.                           |


### Response

**[operations.AddOrganismResponse](../../models/operations/addorganismresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_organism_by_id

Returns a Organism for a given Organism ID.

### Example Usage

```python
import pazy
from pazy.models import components

s = pazy.Pazy(
    security=components.Security(
        username="<YOUR_USERNAME_HERE>",
    ),
)


res = s.organisms.get_organism_by_id(id='<value>')

if res.organism is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.GetOrganismByIDResponse](../../models/operations/getorganismbyidresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## update_organism

Updates a Organism for a given Organism ID.

### Example Usage

```python
import pazy
from pazy.models import components

s = pazy.Pazy(
    security=components.Security(
        username="<YOUR_USERNAME_HERE>",
    ),
)


res = s.organisms.update_organism(id='<value>', organism=components.OrganismInput(
    scientific_name='<value>',
))

if res.organism is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                            | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `id`                                                                 | *str*                                                                | :heavy_check_mark:                                                   | N/A                                                                  |
| `organism`                                                           | [components.OrganismInput](../../models/components/organisminput.md) | :heavy_check_mark:                                                   | N/A                                                                  |


### Response

**[operations.UpdateOrganismResponse](../../models/operations/updateorganismresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## partial_update_organism

Partially updates a Organism for a given Organism ID.

### Example Usage

```python
import pazy
from pazy.models import components

s = pazy.Pazy(
    security=components.Security(
        username="<YOUR_USERNAME_HERE>",
    ),
)


res = s.organisms.partial_update_organism(id='<value>', patched_organism=components.PatchedOrganism())

if res.organism is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `id`                                                                               | *str*                                                                              | :heavy_check_mark:                                                                 | N/A                                                                                |
| `patched_organism`                                                                 | [Optional[components.PatchedOrganism]](../../models/components/patchedorganism.md) | :heavy_minus_sign:                                                                 | N/A                                                                                |


### Response

**[operations.PartialUpdateOrganismResponse](../../models/operations/partialupdateorganismresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## delete_organism

Deletes a Organism from the database.

### Example Usage

```python
import pazy
from pazy.models import components

s = pazy.Pazy(
    security=components.Security(
        username="<YOUR_USERNAME_HERE>",
    ),
)


res = s.organisms.delete_organism(id='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.DeleteOrganismResponse](../../models/operations/deleteorganismresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

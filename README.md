# pypazy

<div align="left">
    <a href="https://speakeasyapi.dev/"><img src="https://custom-icon-badges.demolab.com/badge/-Built%20By%20Speakeasy-212015?style=for-the-badge&logoColor=FBE331&logo=speakeasy&labelColor=545454" /></a>
    <a href="https://opensource.org/licenses/MIT">
        <img src="https://img.shields.io/badge/License-MIT-blue.svg" style="width: 100px; height: 28px;" />
    </a>
</div>


## 🏗 **Welcome to your new SDK!** 🏗

It has been generated successfully based on your OpenAPI spec. However, it is not yet ready for production use. Here are some next steps:
- [ ] 🛠 Make your SDK feel handcrafted by [customizing it](https://www.speakeasyapi.dev/docs/customize-sdks)
- [ ] ♻️ Refine your SDK quickly by iterating locally with the [Speakeasy CLI](https://github.com/speakeasy-api/speakeasy)
- [ ] 🎁 Publish your SDK to package managers by [configuring automatic publishing](https://www.speakeasyapi.dev/docs/productionize-sdks/publish-sdks)
- [ ] ✨ When ready to productionize, delete this section from the README

<!-- Start SDK Installation [installation] -->
## SDK Installation

```bash
pip install git+<UNSET>.git
```
<!-- End SDK Installation [installation] -->

<!-- Start SDK Example Usage [usage] -->
## SDK Example Usage

### Example

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
<!-- End SDK Example Usage [usage] -->

<!-- Start Available Resources and Operations [operations] -->
## Available Resources and Operations

### [datasets](docs/sdks/datasets/README.md)

* [get_datasets](docs/sdks/datasets/README.md#get_datasets) - Returns all Datasets
* [add_dataset](docs/sdks/datasets/README.md#add_dataset) - Adds a new Dataset to the database.
* [get_dataset_by_id](docs/sdks/datasets/README.md#get_dataset_by_id) - Returns a Dataset for a given Dataset ID.
* [update_dataset](docs/sdks/datasets/README.md#update_dataset) - Updates a Dataset for a given Dataset ID.
* [partial_update_dataset](docs/sdks/datasets/README.md#partial_update_dataset) - Partially updates a Dataset for a given Dataset ID.
* [delete_dataset](docs/sdks/datasets/README.md#delete_dataset) - Deletes a Dataset from the database.

### [literature](docs/sdks/literature/README.md)

* [get_literatures](docs/sdks/literature/README.md#get_literatures) - Returns all Literatures
* [add_literature](docs/sdks/literature/README.md#add_literature) - Adds a new Literature to the database.
* [get_literature_by_id](docs/sdks/literature/README.md#get_literature_by_id) - Returns a Literature for a given Literature ID.
* [update_literature](docs/sdks/literature/README.md#update_literature) - Updates a Literature for a given Literature ID.
* [partial_update_literature](docs/sdks/literature/README.md#partial_update_literature) - Partially updates a Literature for a given Literature ID.
* [delete_literature](docs/sdks/literature/README.md#delete_literature) - Deletes a Literature from the database.

### [organisms](docs/sdks/organisms/README.md)

* [get_organisms](docs/sdks/organisms/README.md#get_organisms) - Returns all Organisms
* [add_organism](docs/sdks/organisms/README.md#add_organism) - Adds a new Organism to the database.
* [get_organism_by_id](docs/sdks/organisms/README.md#get_organism_by_id) - Returns a Organism for a given Organism ID.
* [update_organism](docs/sdks/organisms/README.md#update_organism) - Updates a Organism for a given Organism ID.
* [partial_update_organism](docs/sdks/organisms/README.md#partial_update_organism) - Partially updates a Organism for a given Organism ID.
* [delete_organism](docs/sdks/organisms/README.md#delete_organism) - Deletes a Organism from the database.

### [proteins](docs/sdks/proteins/README.md)

* [get_protein_sequences](docs/sdks/proteins/README.md#get_protein_sequences) - Returns all ProteinSequences
* [add_protein_sequence](docs/sdks/proteins/README.md#add_protein_sequence) - Adds a new ProteinSequence to the database.
* [get_protein_sequence_by_id](docs/sdks/proteins/README.md#get_protein_sequence_by_id) - Returns a ProteinSequence for a given ProteinSequence ID.
* [update_protein_sequence](docs/sdks/proteins/README.md#update_protein_sequence) - Updates a ProteinSequence for a given ProteinSequence ID.
* [partial_update_protein_sequence](docs/sdks/proteins/README.md#partial_update_protein_sequence) - Partially updates a ProteinSequence for a given ProteinSequence ID.
* [delete_protein_sequence](docs/sdks/proteins/README.md#delete_protein_sequence) - Deletes a ProteinSequence from the database.

### [substrates](docs/sdks/substrates/README.md)

* [get_substrates](docs/sdks/substrates/README.md#get_substrates) - Returns all Substrates
* [add_substrate](docs/sdks/substrates/README.md#add_substrate) - Adds a new Substrate to the database.
* [get_substrate_by_id](docs/sdks/substrates/README.md#get_substrate_by_id) - Returns a Substrate for a given Substrate ID.
* [update_substrate](docs/sdks/substrates/README.md#update_substrate) - Updates a Substrate for a given Substrate ID.
* [partial_update_substrate](docs/sdks/substrates/README.md#partial_update_substrate) - Partially updates a Substrate for a given Substrate ID.
* [delete_substrate](docs/sdks/substrates/README.md#delete_substrate) - Deletes a Substrate from the database.
<!-- End Available Resources and Operations [operations] -->

<!-- Start Error Handling [errors] -->
## Error Handling

Handling errors in this SDK should largely match your expectations.  All operations return a response object or raise an error.  If Error objects are specified in your OpenAPI Spec, the SDK will raise the appropriate Error type.

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

### Example

```python
import pazy
from pazy.models import components, errors

s = pazy.Pazy(
    security=components.Security(
        username="<YOUR_USERNAME_HERE>",
    ),
)


res = None
try:
    res = s.datasets.get_datasets()
except errors.SDKError as e:
    # handle exception
    raise(e)

if res.datasets is not None:
    # handle response
    pass
```
<!-- End Error Handling [errors] -->

<!-- Start Server Selection [server] -->
## Server Selection

### Select Server by Index

You can override the default server globally by passing a server index to the `server_idx: int` optional parameter when initializing the SDK client instance. The selected server will then be used as the default on the operations that use it. This table lists the indexes associated with the available servers:

| # | Server | Variables |
| - | ------ | --------- |
| 0 | `https://pazy-backend.3.us-1.fl0.io` | None |

#### Example

```python
import pazy
from pazy.models import components

s = pazy.Pazy(
    server_idx=0,
    security=components.Security(
        username="<YOUR_USERNAME_HERE>",
    ),
)


res = s.datasets.get_datasets()

if res.datasets is not None:
    # handle response
    pass
```


### Override Server URL Per-Client

The default server can also be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:
```python
import pazy
from pazy.models import components

s = pazy.Pazy(
    server_url="https://pazy-backend.3.us-1.fl0.io",
    security=components.Security(
        username="<YOUR_USERNAME_HERE>",
    ),
)


res = s.datasets.get_datasets()

if res.datasets is not None:
    # handle response
    pass
```
<!-- End Server Selection [server] -->

<!-- Start Custom HTTP Client [http-client] -->
## Custom HTTP Client

The Python SDK makes API calls using the [requests](https://pypi.org/project/requests/) HTTP library.  In order to provide a convenient way to configure timeouts, cookies, proxies, custom headers, and other low-level configuration, you can initialize the SDK client with a custom `requests.Session` object.

For example, you could specify a header for every request that this sdk makes as follows:
```python
import pazy
import requests

http_client = requests.Session()
http_client.headers.update({'x-custom-header': 'someValue'})
s = pazy.Pazy(client: http_client)
```
<!-- End Custom HTTP Client [http-client] -->

<!-- Start Authentication [security] -->
## Authentication

### Per-Client Security Schemes

This SDK supports the following security scheme globally:

| Name       | Type       | Scheme     |
| ---------- | ---------- | ---------- |
| `password` | http       | HTTP Basic |

You can set the security parameters through the `security` optional parameter when initializing the SDK client instance. For example:
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
<!-- End Authentication [security] -->

<!-- Placeholder for Future Speakeasy SDK Sections -->

# Development

## Maturity

This SDK is in beta, and there may be breaking changes between versions without a major version update. Therefore, we recommend pinning usage
to a specific package version. This way, you can install the same version each time without breaking changes unless you are intentionally
looking for the latest version.

## Contributions

While we value open-source contributions to this SDK, this library is generated programmatically.
Feel free to open a PR or a Github issue as a proof of concept and we'll do our best to include it in a future release!

### SDK Created by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)

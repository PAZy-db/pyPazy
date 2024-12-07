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

PIP
```bash
pip install git+https://github.com/PAZy-db/pyPazy.git
```

Poetry
```bash
poetry add git+https://github.com/PAZy-db/pyPazy.git
```
<!-- End SDK Installation [installation] -->

<!-- Start SDK Example Usage [usage] -->
## SDK Example Usage

### Example

```python
# Synchronous Example
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

</br>

The same SDK client can also be used to make asychronous requests by importing asyncio.
```python
# Asynchronous Example
import asyncio
from pypazy import Pazy
from pypazy.models import components

async def main():
    s = Pazy(
        security=components.Security(
            username="",
            password="",
        ),
    )
    res = await s.datasets.get_datasets_async()
    if res is not None:
        # handle response
        pass

asyncio.run(main())
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
| errors.SDKError | 4xx-5xx         | */*             |

### Example

```python
from pypazy import Pazy
from pypazy.models import components, errors

s = Pazy(
    security=components.Security(
        username="",
        password="",
    ),
)

res = None
try:
    res = s.datasets.get_datasets()

except errors.SDKError as e:
    # handle exception
    raise(e)

if res is not None:
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
| 0 | `http://localhost:8000` | None |

#### Example

```python
from pypazy import Pazy
from pypazy.models import components

s = Pazy(
    server_idx=0,
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


### Override Server URL Per-Client

The default server can also be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:
```python
from pypazy import Pazy
from pypazy.models import components

s = Pazy(
    server_url="http://localhost:8000",
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
<!-- End Server Selection [server] -->

<!-- Start Custom HTTP Client [http-client] -->
## Custom HTTP Client

The Python SDK makes API calls using the [httpx](https://www.python-httpx.org/) HTTP library.  In order to provide a convenient way to configure timeouts, cookies, proxies, custom headers, and other low-level configuration, you can initialize the SDK client with your own HTTP client instance.
Depending on whether you are using the sync or async version of the SDK, you can pass an instance of `HttpClient` or `AsyncHttpClient` respectively, which are Protocol's ensuring that the client has the necessary methods to make API calls.
This allows you to wrap the client with your own custom logic, such as adding custom headers, logging, or error handling, or you can just pass an instance of `httpx.Client` or `httpx.AsyncClient` directly.

For example, you could specify a header for every request that this sdk makes as follows:
```python
from pypazy import Pazy
import httpx

http_client = httpx.Client(headers={"x-custom-header": "someValue"})
s = Pazy(client=http_client)
```

or you could wrap the client with your own custom logic:
```python
from pypazy import Pazy
from pypazy.httpclient import AsyncHttpClient
import httpx

class CustomClient(AsyncHttpClient):
    client: AsyncHttpClient

    def __init__(self, client: AsyncHttpClient):
        self.client = client

    async def send(
        self,
        request: httpx.Request,
        *,
        stream: bool = False,
        auth: Union[
            httpx._types.AuthTypes, httpx._client.UseClientDefault, None
        ] = httpx.USE_CLIENT_DEFAULT,
        follow_redirects: Union[
            bool, httpx._client.UseClientDefault
        ] = httpx.USE_CLIENT_DEFAULT,
    ) -> httpx.Response:
        request.headers["Client-Level-Header"] = "added by client"

        return await self.client.send(
            request, stream=stream, auth=auth, follow_redirects=follow_redirects
        )

    def build_request(
        self,
        method: str,
        url: httpx._types.URLTypes,
        *,
        content: Optional[httpx._types.RequestContent] = None,
        data: Optional[httpx._types.RequestData] = None,
        files: Optional[httpx._types.RequestFiles] = None,
        json: Optional[Any] = None,
        params: Optional[httpx._types.QueryParamTypes] = None,
        headers: Optional[httpx._types.HeaderTypes] = None,
        cookies: Optional[httpx._types.CookieTypes] = None,
        timeout: Union[
            httpx._types.TimeoutTypes, httpx._client.UseClientDefault
        ] = httpx.USE_CLIENT_DEFAULT,
        extensions: Optional[httpx._types.RequestExtensions] = None,
    ) -> httpx.Request:
        return self.client.build_request(
            method,
            url,
            content=content,
            data=data,
            files=files,
            json=json,
            params=params,
            headers=headers,
            cookies=cookies,
            timeout=timeout,
            extensions=extensions,
        )

s = Pazy(async_client=CustomClient(httpx.AsyncClient()))
```
<!-- End Custom HTTP Client [http-client] -->

<!-- Start Authentication [security] -->
## Authentication

### Per-Client Security Schemes

This SDK supports the following security scheme globally:

| Name                  | Type                  | Scheme                |
| --------------------- | --------------------- | --------------------- |
| `username` `password` | http                  | HTTP Basic            |

You can set the security parameters through the `security` optional parameter when initializing the SDK client instance. For example:
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
<!-- End Authentication [security] -->

<!-- Start Retries [retries] -->
## Retries

Some of the endpoints in this SDK support retries. If you use the SDK without any configuration, it will fall back to the default retry strategy provided by the API. However, the default retry strategy can be overridden on a per-operation basis, or across the entire SDK.

To change the default retry strategy for a single API call, simply provide a `RetryConfig` object to the call:
```python
from pazy.utils import BackoffStrategy, RetryConfig
from pypazy import Pazy
from pypazy.models import components

s = Pazy(
    security=components.Security(
        username="",
        password="",
    ),
)


res = s.datasets.get_datasets(,
    RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False))

if res is not None:
    # handle response
    pass

```

If you'd like to override the default retry strategy for all operations that support retries, you can use the `retry_config` optional parameter when initializing the SDK:
```python
from pazy.utils import BackoffStrategy, RetryConfig
from pypazy import Pazy
from pypazy.models import components

s = Pazy(
    retry_config=RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False),
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
<!-- End Retries [retries] -->

<!-- Start Debugging [debug] -->
## Debugging

To emit debug logs for SDK requests and responses you can pass a logger object directly into your SDK object.

```python
from pypazy import Pazy
import logging

logging.basicConfig(level=logging.DEBUG)
s = Pazy(debug_logger=logging.getLogger("pypazy"))
```
<!-- End Debugging [debug] -->

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

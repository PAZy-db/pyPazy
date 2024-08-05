<!-- Start SDK Example Usage [usage] -->
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
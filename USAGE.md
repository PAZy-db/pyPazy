<!-- Start SDK Example Usage [usage] -->
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
# PaginatedLiteratureList


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          | Example                                                              |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `count`                                                              | *Optional[int]*                                                      | :heavy_minus_sign:                                                   | N/A                                                                  | 123                                                                  |
| `next`                                                               | *OptionalNullable[str]*                                              | :heavy_minus_sign:                                                   | N/A                                                                  | http://api.example.org/accounts/?offset=400&limit=100                |
| `previous`                                                           | *OptionalNullable[str]*                                              | :heavy_minus_sign:                                                   | N/A                                                                  | http://api.example.org/accounts/?offset=200&limit=100                |
| `results`                                                            | List[[components.Literature](../../models/components/literature.md)] | :heavy_minus_sign:                                                   | N/A                                                                  |                                                                      |
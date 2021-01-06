PUT /customer?pretty

GET /_cat/indices?v

PUT /customer

PUT /customer/external/1?pretty
{
    "name": "John Doe"
}

GET /customer/external/1?pretty

DELETE /customer?pretty

GET /_cat/indices?v

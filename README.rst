Consul Service Discovery API
----------------------------
This module provides a simple way to work with the 
`Consul Service Discovery API <https://www.consul.io/docs/agent/http.html>`_
from python.


Examples
--------
Usage examples::

    import consul
    service = consul.Client()
    service.register(id='flexlm1', name='flexlm',
                address='10.112.0.211', port=28518,
                tags=('flexlm1', light', 'v1'),
                check={'id': 'flexlm', 'name': 'flexlm on port 28518',
                       'tcp': '10.112.0.211:28518',
                       'Interval': '30s', 'timeout': '2s'})
    service.deregister(id='flexlm1')
    service.list()
    service.info(name='flexlm')

The registration/deregistration is done using the consul agent API::

    http://localhost:8500
    PUT /v1/agent/service/register
    DELETE /v1/agent/service/deregister/<serviceId>

To query the information the catalog API is used::

    http://localhost:8500
    GET /v1/catalog/services
    GET /v1/catalog/service/bigdata
    GET /v1/catalog/nodes
    GET /v1/catalog/node/c13-9

The payload for the registration request has the following format::

    {
      "ID": "flexlm1",
      "Name": "flexlm",
      "Tags": ["flexlm1", light", "v1"],
      "Address": "10.112.0.211",
      "Port": 28518,
      "Check": {
        "id": "flexlm",
        "name": "flexlm on port 28518",
        "tcp": "10.112.0.211:28518",
        "Interval": "30s",
        "timeout": "2s"
      }
    }

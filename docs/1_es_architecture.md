# ES architecture

## Node

Q: a node == a machine? or n nodes can run on the same machine?
A: __A node refers to an instance of Elasticsearch__, not a machine. Therefore, __any number of nodes can run on the same machine__.

__Each node in a cluster handles the HTTP request__ for a client who wants to send the request to the cluster.

Each __node contains multiple shards__. And the linit of shards per node in ES is 1000 shards per node.

-  you should have a number that is evenly divisible by the number of data nodes. For instance, if you have 3 data nodes, you should have 3, 6 or 9 shards.

The _master nodes_ handles additional tasks, like __setting status of the cluster__, managing indexes and nodes.


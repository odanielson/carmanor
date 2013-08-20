Carmanor
========

Carmanor is a simple logaggregation tool.
It currently consists of harvestor tool which scans logs
in directories and posts log entries to elasticsearch.
The purpose is a simple to use on-the-fly tool to have
ready at hand when needed rather than a constantly running log
aggreagator for server installations. For that purpose, [logstash](http://logstash.net) comes to mind.

Install
-------

Install this package and configure elastic host in config.py

    # git clone git@github.com:odanielson/carmanor.git
    # python setup.py install

Install dependencies
--------------------

Download (not described) and start elasticsearch

    ~elasticsearch# ./bin/elasticsearch -f

Usage
-----

Collect logs recursivly in a dir with

    # harvester elasticsearch_host path1 path2 path3 ....

Watch out for errors on failed to parse timestamps and repair.
Log entries are should now be posted as entries in elasticsearch.

Take a look at the logs
-----------------------
You could try using [Kibana](http://kibana.org) to take a look at the logs.
Configure it with those options to find the data from Carmanor.

Smart_index = false

Default_index = 'carmanor'


Carmanor
========

Install
-------

Install this package and configure elastic host in config.py

    # git clone git@github.com:odanielson/carmanor.git
    # python setup.py install

Start
-----

Collect logs recursivly in a dir with

    # harvester elasticsearch_host path1 path2 path3 ....

Watch out for errors on failed to parse timestamps and repair


Install dependencies
--------------------

On your analyze machine

* Install elastic search
* Install Kibana and configure

Smart_index = false
Default_index = 'carmanor'

Start elasticsearch

    ~elasticsearch# ./bin/elasticsearch -f

Start Kibana

    ~kibana# ruby kibana.rb

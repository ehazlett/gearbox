Gearbox
=========
Gearbox is a tool for bootstrapping [OpenShift](http://openshift.redhat.com) pre-built applications.  With gearbox you can view a list of template applications such as Django, Drupal, and many more (run `gb -l` for a complete list).

Installation
=============
Gearbox is written in Python.  Run `pip install https://github.com/ehazlett/gearbox/archive/master.zip`.

Usage
======

List Templates
---------------
To list available application templates run:

`gb -l`

```
Name                      Author               Type            Description
-----------------------------------------------------------------------------
django                    openshift            python-2.6      Default latest stable version of Django
flask                     openshift            python-2.6      Default install of Flask
reviewboard               openshift            python-2.6      Example install of Reviewboard
sinatra                   openshift            ruby-1.8        Example install of Sinatra
nodejs                    openshift            nodejs-0.6      Example install of Node.js
etherpad                  openshift            nodejs-0.6      Example install of Etherpad
drupal                    openshift            php-5.3         Example install of Drupal
...

```

Create Application
-------------------
To create an application:

`gb -n <your_app_name> -t <template_name>`

For example:

`gb -n mydjango -t django`

This will create a new OpenShift application named `mydjango`, create any OpenShift cartridges needed by the app, set the upstream repo to the sample, pull in the changes, and finally push and deploy the app to OpenShift.


Thanks
=======
Many thanks to the OpenShift team for all of the great work on the product -- and especially for open sourcing it :)

Help & contributing
====================
If you need help, you can find me on IRC (`ehazlett` on freenode) or shoot me a message here.  Pull-requests also welcome :)


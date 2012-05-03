Gearbox
=========
Gearbox is a tool for bootstrapping [OpenShift](http://openshift.redhat.com) pre-built applications.  With gearbox you can view a list of template applications such as Django, Drupal, and many more (run `gb -l` for a complete list).

Installation
=============
Gearbox is written in Python.  Run `pip install gearbox`.

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
drupal                    openshift            php-5.3         Example install of Drupal
sugarcrm                  openshift            php-5.3         Example install of SugarCRM
.......

```

Create Application
-------------------
To create an application:

`gb -n mydjango -t django`

This will create a new OpenShift application named `mydjango`, create any OpenShift cartridges needed by the app, clone set the upstream repo to the sample, pull in the changes, and finally push and deploy the app to OpenShift.


Thanks
=======
Many thanks to the OpenShift team for all of the great work on the product -- and especially for open sourcing it :)

Help & contributing
====================
If you need help, you can find me on IRC (`ehazlett` on freenode) or shoot me a message here.  Pull-requests also welcome :)


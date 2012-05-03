#!/usr/bin/env python
#    Copyright 2012 Gearbox Project
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.
import requests
from subprocess import Popen, PIPE
import logging
try:
    import simplejson as json
except ImportError:
    import json

class Gearbox(object):
    """docstring for Gearbox"""
    def __init__(self, base_url='https://raw.github.com/vitasso/gearbox/master', \
        template_file=None, debug=False):
        self._base_url = base_url
        self._template_file = template_file
        if not template_file:
            self._template_file = '{0}/templates.json'.format(self._base_url)
        self._debug = debug
        self._log = logging.getLogger(__name__)

    def list_templates(self):
        """
        Gets a list of Gearbox templates

        :rtype: List of templates

        """
        if self._debug:
            templates = json.loads(open(self._template_file, 'r').read())
        else:
            r = requests.get(self._template_file)
            templates = json.loads(r.text)
        return templates

    def create_app(self, name=None, template=None):
        templates = self.list_templates()
        tmpls = [x for x in templates if x.get('name') == template]
        if tmpls:
            template = tmpls[0]
        else:
            raise NameError('{0} is not a valid template'.format(template))
        self._log.debug('Creating application')
        # create app
        cmd = 'rhc-create-app -a {0} -t {1}'.format(name, template.get('type'))
        p = Popen([cmd], shell=True)
        p.wait()
        # check for cartridges
        for c in template.get('cartridges'):
            self._log.debug('Adding cartridge {0}'.format(c))
            cmd = 'rhc app cartridge add -a {0} -c {1}'.format(name, c)
            p = Popen([cmd], shell=True)
            p.wait()
        # get and push app
        self._log.debug('Adding upstream')
        cmd = 'cd {0} ; git remote add upstream -m master {1}'.format(name, template.get('repo'))
        p = Popen([cmd], shell=True)
        p.wait()
        self._log.debug('Pulling from upstream and pushing to OpenShift')
        cmd = 'cd {0} ; git pull -s recursive -X theirs upstream master ; git push'.format(name)
        p = Popen([cmd], shell=True)
        p.wait()
        return True
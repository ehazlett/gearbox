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
from optparse import OptionParser
import sys
import os
import commands
from core import Gearbox
import logging

logging.getLogger('requests').setLevel(logging.WARN)

def show_templates(templates):
    print('\n{0:25s} {1:20s} {2:15s} {3}'.format('Name', 'Author', 'Type', 'Description'))
    print('-----------------------------------------------------------------------------')
    for t in templates:
        print('{0:25s} {1:20s} {2:15s} {3}'.format(t.get('name'), t.get('author'), t.get('type'), t.get('description')))
    print('')

def main():
    base_url = 'https://raw.github.com/ehazlett/gearbox/master'
    log_level = logging.INFO
    log_format = "%(levelname)-10s %(name)s %(message)s"
    
    op = OptionParser()
    op.add_option('-n', '--name', dest='name', help='Name of application')
    op.add_option('-t', '--template', dest='template', help='Name of application template')
    op.add_option('-l', '--list-templates', dest='list_templates', action='store_true', default=False, help='List available app templates')
    op.add_option('-d', '--debug', dest='debug', action='store_true', default=False, help='Run debug mode')

    opts, args = op.parse_args()
    # check for rhc client
    if not commands.getoutput('which rhc'):
        print('Unable to find OpenShift rhc client.  Please install before using Gearbox.')
        sys.exit(1)
    template_file = None
    if opts.debug:
        tmpl_file = os.path.join(os.getcwd(), 'templates.json')
        if os.path.exists(tmpl_file):
            template_file = tmpl_file
        log_level = logging.DEBUG
    gb = Gearbox(base_url, debug=opts.debug, template_file=template_file)
    # configure logging
    logging.basicConfig(format=log_format, level=log_level)
    if opts.list_templates:
        show_templates(gb.list_templates())
        sys.exit(0)
    if opts.name and opts.template:
        if gb.create_app(name=opts.name, template=opts.template):
            print('Your application should be available at {0}-<domain>.rhcloud.com'.format(opts.name))
        sys.exit(0)
    op.print_help()
    
if __name__=='__main__':
    main()
    
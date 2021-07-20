#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Ansible module to manage CheckPoint Firewall (c) 2019
#
# Ansible is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Ansible is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Ansible.  If not, see <http://www.gnu.org/licenses/>.
#

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.check_point.gaia.plugins.module_utils.checkpoint import api_call

DOCUMENTATION = """
author: Thomas Marko (@arw-thomasm)
description:
- Running the first time wizard to create a Smartcenter/MDM server
module: cp_run_ftw
options:

short_description: Run the First Time Wizard for Management
version_added: '2.9'
"""

EXAMPLES = """
- name: Setup a primary Smartcenter Server
  cp_run_ftw:
    password: vpn123
    security_management:
      multi_domain: False
      type: primary
      gui_clients:
        network:
          ip_network_address: 192.168.0.0
          IPv4_masklen: 24
"""

RETURN = """
task_id:
  description: The task-id of the asynchronous task
  returned: always
  type: str
"""



def main():
    argument_spec = dict(
        task_id=dict(type='list')
    )
    argument_spec.update(checkpoint_argument_spec_for_commands)

    module = AnsibleModule(argument_spec=argument_spec)

    command = "show-task"

    result = api_command(module, command)
    module.exit_json(**result)


if __name__ == '__main__':
    main()
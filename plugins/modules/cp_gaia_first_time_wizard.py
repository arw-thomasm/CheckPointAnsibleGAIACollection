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
from ansible_collections.check_point.gaia.plugins.module_utils.checkpoint import idempotent_api_call

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
    # arguments for the module:
    fields = dict(
      security_management=dict(type='dict', options=dict(
        password=dict(type='str', required=True),
        multi_domain=dict(type='bool', required=True),
        type=dict(type='str', required=True, choices=['primary', 'secondary', 'log-server']),
        activation_key=dict(type='str', required=False),
        gui_clients=dict(type='dict', options=dict(
          range=dict(type='dict', options=dict(
            first_IPv4_range=dict(type='str'),
            last_IPv4_range=dict(type='str')
          )),
          network=dict(type=dict, options=dict(
            ip_network_address=dict(type='str'),
            IPv4_masklen=dict(type='int')
          )),
          single_ip=dict(type='str')
        )),
        leading_interface=dict(type='str')
      )),
      security_gateway=dict(type='dict', options=dict(
        dynamically_assigned_ip=dict(type='bool'),
        activation_key=dict(type='str', required=True),
        cluster_member=dict(type='bool')
      ))
    )
    module = AnsibleModule(argument_spec=fields, supports_check_mode=True)
    api_call_object = 'set-initial-setup'
    ignore = []
    keys = []

    res = idempotent_api_call(module, api_call_object, ignore, keys)
    module.exit_json(**res)


if __name__ == "__main__":
    main()
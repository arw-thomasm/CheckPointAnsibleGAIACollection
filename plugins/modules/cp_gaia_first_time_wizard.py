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
from ansible_collections.check_point.gaia.plugins.module_utils.checkpoint import checkpoint_argument_spec_for_commands, api_command

DOCUMENTATION = """
author: Thomas Marko (@arw-thomasm)
description:
- Run the first time wizard to create a Smartcenter/MDM server, gateway or cluster node
module: cp_gaia_first_time_wizard
options:
  password:
    description: password for user admin
    type: str
    required: True
    
  security_management:
    description: Install Security Management or Multi domain server
    type: dict
    options:
      multi_domain:
        description: Install Security Multi domain server, it can be primary or secondary or log-server according to type parameter
        type: bool
        required: True
      type:
        description: type of security management or multi domain server
        type: str
        required: True
        choices: 'primary'|'secondary'|'log-server'
      activation_key:
        description: Secure Internal Communication key, relevant in case of secondary or log-server
        type: str
      gui_clients:
        description: choose which GUI clients can log into the Security Management. fill one of the parameters (range/network/single-ip), for multi-domain it can be only single-ip or can keep the default value (any)
        type: dict
        options: 
          range:
            description: range of IPs allowed to connect to management
            type: dict
            options:
              first_IPv4_range:
                description: first ipv4-address
                type: str
              last_IPv4_range:
                description: last ipv4-address
                type: str
          network:
            description: IPs from specific network allowed to connect to management
            type: dict
            options:
              ip_network_address:
                description: ipv4 network address
                type: str
              IPv4_masklen:
                description: masklength (valid values are 1-32)
                type: int
          single_ip:
            description: In case of a single IP which allowed to connect to management
            type: str
        leading_interface:
          description: leading multi domain server interface, relevant in case of multi-domain enabled
          type: str
  security_gateway:
    description: Install Security Gateway
    type: dict
    options:
      dynamically_assigned_ip:
        description: Enable DAIP (dynamic ip) gateway. Should be false if cluster-member or security-management enabled
        type: bool
      activation_key:
        description: Secure Internal Communication key
        type: str
        required: True
      cluster_member:
        description: Enable/Disable ClusterXL
        type: bool

short_description: Run the First Time Wizard for Management
version_added: '2.9'
"""

EXAMPLES = """
- name: create a primary smartcenter server
      cp_gaia_first_time_wizard:
        password: vpn123
        security_management:
          multi_domain: False
          type: primary
          gui_clients:
            network:
              ip_network_address: 192.168.0.0
              IPv4_masklen: 24
      register: result
"""

RETURN = """
task_id:
  description: The task-id of the asynchronous task of the FTW
  returned: always
  type: string
"""


def main():
    # arguments for the module:
    argument_spec = dict(
      password=dict(type='str', no_log=True),
      security_management=dict(type='dict', options=dict(
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

    argument_spec.update(checkpoint_argument_spec_for_commands)

    module = AnsibleModule(argument_spec=argument_spec, supports_check_mode=True)
    api_call_object = 'set-initial-setup'

    res = api_command(module, api_call_object)
    module.exit_json(**res)


if __name__ == "__main__":
    main()
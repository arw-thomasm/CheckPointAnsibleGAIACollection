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
from ansible_collections.check_point.gaia.plugins.module_utils.checkpoint import checkpoint_argument_spec_for_objects, idempotent_api_call

DOCUMENTATION = """
author: Thomas Marko (@arw-thomasm)
description:
- Add, edit and remove static routes
module: cp_gaia_static_route
options:
    comment:
        description: Comment
        type: bool
    rank:
        description: Selects a route when there are many routes to a destination that use different routing protocols. 
            The route with the lowest rank value is selected. Possible values: default or integer 0-255
        type: int
    ping:
        description: Configures ping monitoring of the given IPv4 static route. Possible values: true, false
        type: bool
    mask_length:
        description: Mask-Length
        required: true
        type: bool
    scope-local:
        description: Configure the local-interface scope option, When the this option is enabled, the route treated as 
            directly connected to local machine. Possible values: true, false
        type: bool
    address:
        description: Destination IPv4 Address
        required: true
        type: str
    next_hop:
        description: Static next-hop. Contains a list of next-hop gateways.
        type: list|dict
    type:
        description: Type of next hop. Possible values: blackhole, gateway, reject
        required: true
        type: str       
        
short_description: Add or modify static IPv4 routes
version_added: '2.9'

"""

EXAMPLES = """
- name: 
  cp_gaia_static_route:
    mask_length: 24
    address: 192.168.0.0
    type: reject

"""

RETURN = """
route:
  description: The updated route object
  returned: always.
  type: dict
"""


def main():
    # arguments for the module:
    fields = dict(
        comment=dict(type='str'),
        mask_length=dict(type='int'),
        ping=dict(type='bool'),
        rank=dict(type='int'),
        scope_local=dict(type='bool'),
        address=dict(type='str'),
        next_hop=dict(type='dict', options=dict(
            add=dict(type=dict(
                priority=dict(type='int'),
                gateway=dict(type='str'),
            )),
            remove=dict(type=dict(
                priority=dict(type='int'),
                gateway=dict(type='str'),
            )),
            priority=dict(type='int'),
            gateway=dict(type='str'),
        )),
        type=dict(type='str', choices=['blackhole', 'gateway', 'reject'])
    )

    fields.update(checkpoint_argument_spec_for_objects)

    module = AnsibleModule(argument_spec=fields, supports_check_mode=True)
    api_call_object = 'static-route'
    ignore = []
    keys = ['address', 'mask_length']

    res = idempotent_api_call(module, api_call_object, ignore, keys)
    module.exit_json(**res)


if __name__ == "__main__":
    main()

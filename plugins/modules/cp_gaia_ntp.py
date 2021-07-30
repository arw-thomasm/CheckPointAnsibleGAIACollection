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
- Configure NTP settings
module: cp_gaia_ntp
options:
    enabled:
        description: NTP Active Status
        required: false
        type: bool
    servers:
        description: List of NTP Servers
        required: false
        type: list|dict

short_description: Configure NTP settings
version_added: '2.9'
"""

EXAMPLES = """
- name: 
  cp_gaia_ntp:
    enabled: true
    servers:
        - version: 4
          type: primary
          address: 1.2.3.4
        - version: 4
          type: secondary
          address: 1.2.3.5
"""

RETURN = """
ntp:
  description: The updated ntp configuration
  returned: always.
  type: dict
"""


def main():
    # arguments for the module:
    fields = dict(
        enabled=dict(type='bool'),
        servers=dict(type='list', options=dict(
            version=dict(type='int'),
            type=dict(type='str', choices=['primary', 'secondary']),
            address=dict(type='str')
        ))
    )
    module = AnsibleModule(argument_spec=fields, supports_check_mode=True)
    api_call_object = 'ntp'
    ignore = []
    keys = []

    res = idempotent_api_call(module, api_call_object, ignore, keys)
    module.exit_json(**res)


if __name__ == "__main__":
    main()

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
- Configure DNS settings
module: cp_gaia_dns
options:
    suffix:
        description: DNS Suffix
        required: false
        type: str
    primary:
        description: Primary DNS server's ip address
        required: false
        type: str
    secondary:
        description: Secondary DNS server's ip address
        required: false
        type: str
    tertiary:
        description: Tertiary DNS server's ip address
        required: false
        type: str

short_description: Configure DNS settings
version_added: '2.9'

"""

EXAMPLES = """
- name: 
  cp_gaia_dns:
    suffix: checkpoint.com
    primary: 1.1.1.1
    secondary: 8.8.8.8
"""

RETURN = """
dns:
  description: The updated dns configuration
  returned: always.
  type: dict
"""


def main():
    # arguments for the module:
    fields = dict(
        suffix=dict(type='str'),
        primary=dict(type='str'),
        secondary=dict(type='str'),
        tertiary=dict(type='str')
    )
    module = AnsibleModule(argument_spec=fields, supports_check_mode=True)
    api_call_object = 'static-route'
    ignore = []
    keys = []

    res = idempotent_api_call(module, api_call_object, ignore, keys)
    module.exit_json(**res)


if __name__ == "__main__":
    main()

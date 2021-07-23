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
- Setup users
module: cp_gaia_user
options:
  name:
    description: The username to operate on
    required: true
    type: str
short_description: Add or modify user's settings
version_added: '2.9'

"""

EXAMPLES = """
- name: Changing a user's shell
  cp_gaia_user:
    name: admin
    shell: bash

"""

RETURN = """
user:
  description: The updated user object
  returned: always.
  type: dict
"""


def main():
    # arguments for the module:
    fields = dict(
        name=dict(type='str', required=True),
        shell=dict(type='str', choices=['scp-only', 'tcsh', 'csh', 'sh', 'no-login', 'bash', 'cli']),
        homedir=dict(type='str'),
        secondary_system_groups=dict(type='dict', options=dict(
          add=dict(type='list'),
          remove=dict(type='list'),
        )),
        password_hash=dict(type='str'),
        must_change_password=dict(type='bool'),
        real_name=dict(type='str'),
        unlock=dict(type='bool'),
        allow_access_using=dict(type='dict', options=dict(
          add=dict(type='list'),
          remove=dict(type='list'),
        )),
        roles=dict(type='dict', options=dict(
          add=dict(type='list'),
          remove=dict(type='list'),
        )),
        primary_system_group_id=dict(type='int'),
        password=dict(type='str'),
        uid=dict(type='int')
    )
    module = AnsibleModule(argument_spec=fields, supports_check_mode=True)
    api_call_object = 'user'
    ignore = []
    keys = []

    res = idempotent_api_call(module, api_call_object, ignore, keys)
    module.exit_json(**res)


if __name__ == "__main__":
    main()

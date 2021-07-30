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
- Sets time, date, and timezone. Note: time and date cannot be changed while NTP is active.
module: cp_gaia_time_and_date
options:
    date:
        description: Date to set, in YYYY-MM-DD format
        type: str
    timezone:
        description: Timezone in Area / Region format. 
        type: str
    time:
        description: Time to set, in HH:MM[:SS] format
        type: str
        
short_description: Modify time and date settings.
version_added: '2.9'

"""

EXAMPLES = """
- name: 
  cp_gaia_time_and_date:
    date: 2021-07-30
    timezone: Europe / Vienna
    time: 12:00
"""

RETURN = """
task-id:
  description: Asynchronous task unique identifier
  returned: always.
  type: str
"""


def main():
    # arguments for the module:
    fields = dict(
        date=dict(type='str'),
        timezone=dict(type='str'),
        time=dict(type='str'),
    )
    module = AnsibleModule(argument_spec=fields, supports_check_mode=True)
    api_call_object = 'time_and_date'
    ignore = []
    keys = []

    res = idempotent_api_call(module, api_call_object, ignore, keys)
    module.exit_json(**res)


if __name__ == "__main__":
    main()

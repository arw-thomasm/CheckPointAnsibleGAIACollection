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
- Show the status of one or more asynchronous tasks.  
module: cp_gaia_show_task
options:
  task_id:
    description: a task-id or a list of task-ids
    required: true
    type: list|str

short_description: Show the status of asynchronous tasks
version_added: '2.9'
"""

EXAMPLES = """
- name: Show the status of a specific asynchronous task
  cp_gaia_show_task:
    task_id: ccc88f8f-ee65-44d2-bdc6-797f8347f6e1

- name: Show the status for a list of asynchronous tasks
  cp_gaia_show_task:
    task_id:
    - ccc88f8f-ee65-44d2-bdc6-797f8347f6e1
      360e2231-232d-4006-8d1d-903cdc902434
"""

RETURN = """
tasks:
  description: A list of running tasks
  returned: always
  type: list: dict
"""


def main():
  # arguments for the module:
  argument_spec = dict(
      task_id=dict(type='list')
  )

  module = AnsibleModule(argument_spec=argument_spec)

  command = "show-task"

  result = api_call(module, command)
  module.exit_json(**result)


if __name__ == '__main__':
    main()

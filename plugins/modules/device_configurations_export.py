#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: device_configurations_export
short_description: Resource module for Device Configurations Export
description:
- Manage operation create of the resource Device Configurations Export.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  deviceId:
    description: Device Id.
    elements: str
    type: list
  password:
    description: Password.
    type: str
requirements:
- dnacentersdk
seealso:
# Reference by Internet resource
- name: Device Configurations Export reference
  description: Complete reference of the Device Configurations Export object model.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Create
  cisco.dnac.device_configurations_export:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    deviceId:
    - string
    password: string

"""

RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": {
        "taskId": "string",
        "url": "string"
      },
      "version": "string"
    }
"""
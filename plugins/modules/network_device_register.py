#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2020, first last <email>
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

ANSIBLE_METADATA = {
    'metadata_version': '0.0.1',
    'status': ['preview'],
    'supported_by': 'community'
}

DOCUMENTATION = r'''
---
module: network_device_register
short_description: Manage NetworkDeviceRegister objects of Devices
description:
- Registers a device for WSA notification.
version_added: '1.0'
author: first last (@GitHubID)
options:
    macaddress:
        description:
        - Mac addres of the device.
        type: str
    serial_number:
        description:
        - Serial number of the device.
        type: str

requirements:
- dnacentersdk
seealso:
# Reference by module name
- module: cisco.dnac.plugins.module_utils.definitions.network_device_register
# Reference by Internet resource
- name: NetworkDeviceRegister reference
  description: Complete reference of the NetworkDeviceRegister object model.
  link: https://developer.cisco.com/docs/dna-center/api/1-3-3-x
# Reference by Internet resource
- name: NetworkDeviceRegister reference
  description: SDK reference.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v2-1-1-summary
'''

EXAMPLES = r'''
'''

RETURN = r'''
data_0:
    description: Registers a device for WSA notification.
    returned: success,changed,always
    type: dict
    contains:
        response:
            description: Response, property of the response body.
            returned: success,changed,always
            type: dict
            contains:
                macAddress:
                    description: It is the network device register's macAddress.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                modelNumber:
                    description: It is the network device register's modelNumber.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                name:
                    description: It is the network device register's name.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                serialNumber:
                    description: It is the network device register's serialNumber.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                tenantId:
                    description: It is the network device register's tenantId.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'

        version:
            description: Version, property of the response body.
            returned: success,changed,always
            type: str
            sample: 'sample_string'

'''

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.cisco.dnac.plugins.module_utils.dnac import ModuleDefinition, DNACModule, dnac_argument_spec
from ansible_collections.cisco.dnac.plugins.module_utils.definitions.network_device_register import module_definition


def main():

    moddef = ModuleDefinition(module_definition)

    argument_spec = dnac_argument_spec()
    argument_spec.update(moddef.get_argument_spec_dict())

    required_if = moddef.get_required_if_list()
    
    module = AnsibleModule(
        argument_spec=argument_spec,
        supports_check_mode=False,
        required_if=required_if
    )

    dnac = DNACModule(module, moddef)

    state = module.params.get("state")

    if state == "query":
        dnac.exec("get")

    dnac.exit_json()


if __name__ == "__main__":
    main()
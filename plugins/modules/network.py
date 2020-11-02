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
module: network
short_description: Manage Network objects of NetworkSettings
description:
- API to get DHCP and DNS center server details.
- API to create a Network for DHCP and DNS center server settings.
- API to update Network for DHCP and DNS center server settings.
version_added: '1.0'
author: first last (@GitHubID)
options:
    site_id:
        description:
        - Site id to get the Network settings associated with the site.
        type: str
    site_id:
        description:
        - Site id to which site details to associate with the Network settings.
        type: str
        required: True
    settings:
        description:
        - Settings, property of the request body.
        type: dict
        required: True
        suboptions:
            dhcpServer:
                description:
                - It is the Network's dhcpServer.
                type: list
            dnsServer:
                description:
                - It is the Network's dnsServer.
                type: dict
                suboptions:
                    domainName:
                        description:
                        - It is the Network's domainName.
                        type: str
                    primaryIpAddress:
                        description:
                        - It is the Network's primaryIpAddress.
                        type: str
                    secondaryIpAddress:
                        description:
                        - It is the Network's secondaryIpAddress.
                        type: str

            syslogServer:
                description:
                - It is the Network's syslogServer.
                type: dict
                suboptions:
                    ipAddresses:
                        description:
                        - It is the Network's ipAddresses.
                        type: list
                    configureDnacIP:
                        description:
                        - It is the Network's configureDnacIP.
                        type: bool

            snmpServer:
                description:
                - It is the Network's snmpServer.
                type: dict
                suboptions:
                    ipAddresses:
                        description:
                        - It is the Network's ipAddresses.
                        type: list
                    configureDnacIP:
                        description:
                        - It is the Network's configureDnacIP.
                        type: bool

            netflowcollector:
                description:
                - It is the Network's netflowcollector.
                type: dict
                suboptions:
                    ipAddress:
                        description:
                        - It is the Network's ipAddress.
                        type: str
                    port:
                        description:
                        - It is the Network's port.
                        type: int

            ntpServer:
                description:
                - It is the Network's ntpServer.
                type: list
            timezone:
                description:
                - It is the Network's timezone.
                type: str
            messageOfTheday:
                description:
                - It is the Network's messageOfTheday.
                type: dict
                suboptions:
                    bannerMessage:
                        description:
                        - It is the Network's bannerMessage.
                        type: str
                    retainExistingBanner:
                        description:
                        - It is the Network's retainExistingBanner.
                        type: bool

            network_aaa:
                description:
                - It is the Network's Network_aaa.
                type: dict
                suboptions:
                    servers:
                        description:
                        - It is the Network's servers.
                        type: str
                    ipAddress:
                        description:
                        - It is the Network's ipAddress.
                        type: str
                    network:
                        description:
                        - It is the Network's Network.
                        type: str
                    protocol:
                        description:
                        - It is the Network's protocol.
                        type: str
                    sharedSecret:
                        description:
                        - It is the Network's sharedSecret.
                        type: str

            clientAndEndpoint_aaa:
                description:
                - It is the Network's clientAndEndpoint_aaa.
                type: dict
                suboptions:
                    servers:
                        description:
                        - It is the Network's servers.
                        type: str
                    ipAddress:
                        description:
                        - It is the Network's ipAddress.
                        type: str
                    network:
                        description:
                        - It is the Network's Network.
                        type: str
                    protocol:
                        description:
                        - It is the Network's protocol.
                        type: str
                    sharedSecret:
                        description:
                        - It is the Network's sharedSecret.
                        type: str


    site_id:
        description:
        - Site id to update the Network settings which is associated with the site.
        type: str
        required: True
    settings:
        description:
        - Settings, property of the request body.
        type: dict
        required: True
        suboptions:
            dhcpServer:
                description:
                - It is the Network's dhcpServer.
                type: list
            dnsServer:
                description:
                - It is the Network's dnsServer.
                type: dict
                suboptions:
                    domainName:
                        description:
                        - It is the Network's domainName.
                        type: str
                    primaryIpAddress:
                        description:
                        - It is the Network's primaryIpAddress.
                        type: str
                    secondaryIpAddress:
                        description:
                        - It is the Network's secondaryIpAddress.
                        type: str

            syslogServer:
                description:
                - It is the Network's syslogServer.
                type: dict
                suboptions:
                    ipAddresses:
                        description:
                        - It is the Network's ipAddresses.
                        type: list
                    configureDnacIP:
                        description:
                        - It is the Network's configureDnacIP.
                        type: bool

            snmpServer:
                description:
                - It is the Network's snmpServer.
                type: dict
                suboptions:
                    ipAddresses:
                        description:
                        - It is the Network's ipAddresses.
                        type: list
                    configureDnacIP:
                        description:
                        - It is the Network's configureDnacIP.
                        type: bool

            netflowcollector:
                description:
                - It is the Network's netflowcollector.
                type: dict
                suboptions:
                    ipAddress:
                        description:
                        - It is the Network's ipAddress.
                        type: str
                    port:
                        description:
                        - It is the Network's port.
                        type: int

            ntpServer:
                description:
                - It is the Network's ntpServer.
                type: list
            timezone:
                description:
                - It is the Network's timezone.
                type: str
            messageOfTheday:
                description:
                - It is the Network's messageOfTheday.
                type: dict
                suboptions:
                    bannerMessage:
                        description:
                        - It is the Network's bannerMessage.
                        type: str
                    retainExistingBanner:
                        description:
                        - It is the Network's retainExistingBanner.
                        type: bool

            network_aaa:
                description:
                - It is the Network's Network_aaa.
                type: dict
                suboptions:
                    servers:
                        description:
                        - It is the Network's servers.
                        type: str
                    ipAddress:
                        description:
                        - It is the Network's ipAddress.
                        type: str
                    network:
                        description:
                        - It is the Network's Network.
                        type: str
                    protocol:
                        description:
                        - It is the Network's protocol.
                        type: str
                    sharedSecret:
                        description:
                        - It is the Network's sharedSecret.
                        type: str

            clientAndEndpoint_aaa:
                description:
                - It is the Network's clientAndEndpoint_aaa.
                type: dict
                suboptions:
                    servers:
                        description:
                        - It is the Network's servers.
                        type: str
                    ipAddress:
                        description:
                        - It is the Network's ipAddress.
                        type: str
                    network:
                        description:
                        - It is the Network's Network.
                        type: str
                    protocol:
                        description:
                        - It is the Network's protocol.
                        type: str
                    sharedSecret:
                        description:
                        - It is the Network's sharedSecret.
                        type: str



requirements:
- dnacentersdk
seealso:
# Reference by module name
- module: cisco.dnac.plugins.module_utils.definitions.network
# Reference by Internet resource
- name: Network reference
  description: Complete reference of the Network object model.
  link: https://developer.cisco.com/docs/dna-center/api/1-3-3-x
# Reference by Internet resource
- name: Network reference
  description: SDK reference.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v2-1-1-summary
'''

EXAMPLES = r'''
'''

RETURN = r'''
data_0:
    description: API to get DHCP and DNS center server details.
    returned: success,changed,always
    type: dict
    contains:
        response:
            description: Response, property of the response body (list of objects).
            returned: success,changed,always
            type: list
            contains:
                instanceType:
                    description: It is the Network's instanceType.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                instanceUuid:
                    description: It is the Network's instanceUuid.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                namespace:
                    description: It is the Network's namespace.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                type:
                    description: It is the Network's type.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                key:
                    description: It is the Network's key.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                version:
                    description: It is the Network's version.
                    returned: success,changed,always
                    type: int
                    sample: 0
                value:
                    description: It is the Network's value.
                    returned: success,changed,always
                    type: list
                    contains:
                        ipAddresses:
                            description: It is the Network's ipAddresses.
                            returned: success,changed,always
                            type: list
                        configureDnacIP:
                            description: It is the Network's configureDnacIP.
                            returned: success,changed,always
                            type: bool
                            sample: false

                groupUuid:
                    description: It is the Network's groupUuid.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                inheritedGroupUuid:
                    description: It is the Network's inheritedGroupUuid.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                inheritedGroupName:
                    description: It is the Network's inheritedGroupName.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'

        version:
            description: Version, property of the response body.
            returned: success,changed,always
            type: str
            sample: 'sample_string'

data_1:
    description: API to create a Network for DHCP and DNS center server settings.
    returned: success,changed,always
    type: dict
    contains:
        executionId:
            description: Execution Id, property of the response body.
            returned: success,changed,always
            type: str
            sample: 'sample_string'
        executionStatusUrl:
            description: Execution Status Url, property of the response body.
            returned: success,changed,always
            type: str
            sample: 'sample_string'
        message:
            description: Message, property of the response body.
            returned: success,changed,always
            type: str
            sample: 'sample_string'

data_2:
    description: API to update Network for DHCP and DNS center server settings.
    returned: success,changed,always
    type: dict
    contains:
        executionId:
            description: Execution Id, property of the response body.
            returned: success,changed,always
            type: str
            sample: 'sample_string'
        executionStatusUrl:
            description: Execution Status Url, property of the response body.
            returned: success,changed,always
            type: str
            sample: 'sample_string'
        message:
            description: Message, property of the response body.
            returned: success,changed,always
            type: str
            sample: 'sample_string'

'''

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.cisco.dnac.plugins.module_utils.dnac import ModuleDefinition, DNACModule, dnac_argument_spec
from ansible_collections.cisco.dnac.plugins.module_utils.definitions.network import module_definition


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

    elif state == "create":
        dnac.exec("post")

    elif state == "update":
        dnac.exec("put")

    dnac.exit_json()


if __name__ == "__main__":
    main()
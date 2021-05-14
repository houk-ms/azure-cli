# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class KeyReleasePolicy(Model):
    """KeyReleasePolicy.

    :param content_type: Content type and version of key release policy.
     Default value: "application/json; charset=utf-8" .
    :type content_type: str
    :param data: Blob encoding the policy rules under which the key can be
     released.
    :type data: bytes
    """

    _attribute_map = {
        'content_type': {'key': 'contentType', 'type': 'str'},
        'data': {'key': 'data', 'type': 'base64'},
    }

    def __init__(self, *, content_type: str="application/json; charset=utf-8", data: bytes=None, **kwargs) -> None:
        super(KeyReleasePolicy, self).__init__(**kwargs)
        self.content_type = content_type
        self.data = data

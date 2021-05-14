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


class SelectiveKeyRestoreOperationParameters(Model):
    """SelectiveKeyRestoreOperationParameters.

    All required parameters must be populated in order to send to Azure.

    :param sas_token_parameters: Required.
    :type sas_token_parameters: ~backuprestore.models.SASTokenParameter
    :param folder: Required. The Folder name of the blob where the previous
     successful full backup was stored
    :type folder: str
    """

    _validation = {
        'sas_token_parameters': {'required': True},
        'folder': {'required': True},
    }

    _attribute_map = {
        'sas_token_parameters': {'key': 'sasTokenParameters', 'type': 'SASTokenParameter'},
        'folder': {'key': 'folder', 'type': 'str'},
    }

    def __init__(self, *, sas_token_parameters, folder: str, **kwargs) -> None:
        super(SelectiveKeyRestoreOperationParameters, self).__init__(**kwargs)
        self.sas_token_parameters = sas_token_parameters
        self.folder = folder

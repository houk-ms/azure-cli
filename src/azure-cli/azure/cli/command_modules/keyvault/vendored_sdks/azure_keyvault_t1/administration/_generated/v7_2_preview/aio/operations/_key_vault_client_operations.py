# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, Generic, Optional, TypeVar, Union
import warnings

from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse, HttpRequest
from azure.core.polling import AsyncLROPoller, AsyncNoPolling, AsyncPollingMethod
from azure.mgmt.core.exceptions import ARMErrorFormat
from azure.mgmt.core.polling.async_arm_polling import AsyncARMPolling

from ... import models as _models

T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class KeyVaultClientOperationsMixin:

    async def _full_backup_initial(
        self,
        vault_base_url: str,
        azure_storage_blob_container_uri: Optional["_models.SASTokenParameter"] = None,
        **kwargs
    ) -> "_models.FullBackupOperation":
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.FullBackupOperation"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "7.2-preview"
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self._full_backup_initial.metadata['url']  # type: ignore
        path_format_arguments = {
            'vaultBaseUrl': self._serialize.url("vault_base_url", vault_base_url, 'str', skip_quote=True),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        if azure_storage_blob_container_uri is not None:
            body_content = self._serialize.body(azure_storage_blob_container_uri, 'SASTokenParameter')
        else:
            body_content = None
        body_content_kwargs['content'] = body_content
        request = self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.KeyVaultError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        response_headers = {}
        response_headers['Retry-After']=self._deserialize('int', response.headers.get('Retry-After'))
        response_headers['Azure-AsyncOperation']=self._deserialize('str', response.headers.get('Azure-AsyncOperation'))
        deserialized = self._deserialize('FullBackupOperation', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, response_headers)

        return deserialized
    _full_backup_initial.metadata = {'url': '/backup'}  # type: ignore

    async def begin_full_backup(
        self,
        vault_base_url: str,
        azure_storage_blob_container_uri: Optional["_models.SASTokenParameter"] = None,
        **kwargs
    ) -> AsyncLROPoller["_models.FullBackupOperation"]:
        """Creates a full backup using a user-provided SAS token to an Azure blob storage container.

        :param vault_base_url: The vault name, for example https://myvault.vault.azure.net.
        :type vault_base_url: str
        :param azure_storage_blob_container_uri: Azure blob shared access signature token pointing to a
         valid Azure blob container where full backup needs to be stored. This token needs to be valid
         for at least next 24 hours from the time of making this call.
        :type azure_storage_blob_container_uri: ~azure.keyvault.v7_2.models.SASTokenParameter
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: Pass in True if you'd like the AsyncARMPolling polling method,
         False for no polling, or your own initialized polling object for a personal polling strategy.
        :paramtype polling: bool or ~azure.core.polling.AsyncPollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no Retry-After header is present.
        :return: An instance of AsyncLROPoller that returns either FullBackupOperation or the result of cls(response)
        :rtype: ~azure.core.polling.AsyncLROPoller[~azure.keyvault.v7_2.models.FullBackupOperation]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        polling = kwargs.pop('polling', True)  # type: Union[bool, AsyncPollingMethod]
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.FullBackupOperation"]
        lro_delay = kwargs.pop(
            'polling_interval',
            self._config.polling_interval
        )
        cont_token = kwargs.pop('continuation_token', None)  # type: Optional[str]
        if cont_token is None:
            raw_result = await self._full_backup_initial(
                vault_base_url=vault_base_url,
                azure_storage_blob_container_uri=azure_storage_blob_container_uri,
                cls=lambda x,y,z: x,
                **kwargs
            )

        kwargs.pop('error_map', None)
        kwargs.pop('content_type', None)

        def get_long_running_output(pipeline_response):
            response_headers = {}
            response = pipeline_response.http_response
            response_headers['Retry-After']=self._deserialize('int', response.headers.get('Retry-After'))
            response_headers['Azure-AsyncOperation']=self._deserialize('str', response.headers.get('Azure-AsyncOperation'))
            deserialized = self._deserialize('FullBackupOperation', pipeline_response)

            if cls:
                return cls(pipeline_response, deserialized, response_headers)
            return deserialized

        path_format_arguments = {
            'vaultBaseUrl': self._serialize.url("vault_base_url", vault_base_url, 'str', skip_quote=True),
        }

        if polling is True: polling_method = AsyncARMPolling(lro_delay, lro_options={'final-state-via': 'azure-async-operation'}, path_format_arguments=path_format_arguments,  **kwargs)
        elif polling is False: polling_method = AsyncNoPolling()
        else: polling_method = polling
        if cont_token:
            return AsyncLROPoller.from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output
            )
        else:
            return AsyncLROPoller(self._client, raw_result, get_long_running_output, polling_method)
    begin_full_backup.metadata = {'url': '/backup'}  # type: ignore

    async def full_backup_status(
        self,
        vault_base_url: str,
        job_id: str,
        **kwargs
    ) -> "_models.FullBackupOperation":
        """Returns the status of full backup operation.

        :param vault_base_url: The vault name, for example https://myvault.vault.azure.net.
        :type vault_base_url: str
        :param job_id: The id returned as part of the backup request.
        :type job_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: FullBackupOperation, or the result of cls(response)
        :rtype: ~azure.keyvault.v7_2.models.FullBackupOperation
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.FullBackupOperation"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "7.2-preview"
        accept = "application/json"

        # Construct URL
        url = self.full_backup_status.metadata['url']  # type: ignore
        path_format_arguments = {
            'vaultBaseUrl': self._serialize.url("vault_base_url", vault_base_url, 'str', skip_quote=True),
            'jobId': self._serialize.url("job_id", job_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.KeyVaultError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('FullBackupOperation', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    full_backup_status.metadata = {'url': '/backup/{jobId}/pending'}  # type: ignore

    async def _full_restore_operation_initial(
        self,
        vault_base_url: str,
        restore_blob_details: Optional["_models.RestoreOperationParameters"] = None,
        **kwargs
    ) -> "_models.RestoreOperation":
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.RestoreOperation"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "7.2-preview"
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self._full_restore_operation_initial.metadata['url']  # type: ignore
        path_format_arguments = {
            'vaultBaseUrl': self._serialize.url("vault_base_url", vault_base_url, 'str', skip_quote=True),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        if restore_blob_details is not None:
            body_content = self._serialize.body(restore_blob_details, 'RestoreOperationParameters')
        else:
            body_content = None
        body_content_kwargs['content'] = body_content
        request = self._client.put(url, query_parameters, header_parameters, **body_content_kwargs)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.KeyVaultError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        response_headers = {}
        response_headers['Retry-After']=self._deserialize('int', response.headers.get('Retry-After'))
        response_headers['Azure-AsyncOperation']=self._deserialize('str', response.headers.get('Azure-AsyncOperation'))
        deserialized = self._deserialize('RestoreOperation', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, response_headers)

        return deserialized
    _full_restore_operation_initial.metadata = {'url': '/restore'}  # type: ignore

    async def begin_full_restore_operation(
        self,
        vault_base_url: str,
        restore_blob_details: Optional["_models.RestoreOperationParameters"] = None,
        **kwargs
    ) -> AsyncLROPoller["_models.RestoreOperation"]:
        """Restores all key materials using the SAS token pointing to a previously stored Azure Blob
        storage backup folder.

        :param vault_base_url: The vault name, for example https://myvault.vault.azure.net.
        :type vault_base_url: str
        :param restore_blob_details: The Azure blob SAS token pointing to a folder where the previous
         successful full backup was stored.
        :type restore_blob_details: ~azure.keyvault.v7_2.models.RestoreOperationParameters
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: Pass in True if you'd like the AsyncARMPolling polling method,
         False for no polling, or your own initialized polling object for a personal polling strategy.
        :paramtype polling: bool or ~azure.core.polling.AsyncPollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no Retry-After header is present.
        :return: An instance of AsyncLROPoller that returns either RestoreOperation or the result of cls(response)
        :rtype: ~azure.core.polling.AsyncLROPoller[~azure.keyvault.v7_2.models.RestoreOperation]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        polling = kwargs.pop('polling', True)  # type: Union[bool, AsyncPollingMethod]
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.RestoreOperation"]
        lro_delay = kwargs.pop(
            'polling_interval',
            self._config.polling_interval
        )
        cont_token = kwargs.pop('continuation_token', None)  # type: Optional[str]
        if cont_token is None:
            raw_result = await self._full_restore_operation_initial(
                vault_base_url=vault_base_url,
                restore_blob_details=restore_blob_details,
                cls=lambda x,y,z: x,
                **kwargs
            )

        kwargs.pop('error_map', None)
        kwargs.pop('content_type', None)

        def get_long_running_output(pipeline_response):
            response_headers = {}
            response = pipeline_response.http_response
            response_headers['Retry-After']=self._deserialize('int', response.headers.get('Retry-After'))
            response_headers['Azure-AsyncOperation']=self._deserialize('str', response.headers.get('Azure-AsyncOperation'))
            deserialized = self._deserialize('RestoreOperation', pipeline_response)

            if cls:
                return cls(pipeline_response, deserialized, response_headers)
            return deserialized

        path_format_arguments = {
            'vaultBaseUrl': self._serialize.url("vault_base_url", vault_base_url, 'str', skip_quote=True),
        }

        if polling is True: polling_method = AsyncARMPolling(lro_delay, lro_options={'final-state-via': 'azure-async-operation'}, path_format_arguments=path_format_arguments,  **kwargs)
        elif polling is False: polling_method = AsyncNoPolling()
        else: polling_method = polling
        if cont_token:
            return AsyncLROPoller.from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output
            )
        else:
            return AsyncLROPoller(self._client, raw_result, get_long_running_output, polling_method)
    begin_full_restore_operation.metadata = {'url': '/restore'}  # type: ignore

    async def restore_status(
        self,
        vault_base_url: str,
        job_id: str,
        **kwargs
    ) -> "_models.RestoreOperation":
        """Returns the status of restore operation.

        :param vault_base_url: The vault name, for example https://myvault.vault.azure.net.
        :type vault_base_url: str
        :param job_id: The Job Id returned part of the restore operation.
        :type job_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: RestoreOperation, or the result of cls(response)
        :rtype: ~azure.keyvault.v7_2.models.RestoreOperation
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.RestoreOperation"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "7.2-preview"
        accept = "application/json"

        # Construct URL
        url = self.restore_status.metadata['url']  # type: ignore
        path_format_arguments = {
            'vaultBaseUrl': self._serialize.url("vault_base_url", vault_base_url, 'str', skip_quote=True),
            'jobId': self._serialize.url("job_id", job_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.KeyVaultError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('RestoreOperation', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    restore_status.metadata = {'url': '/restore/{jobId}/pending'}  # type: ignore

    async def _selective_key_restore_operation_initial(
        self,
        vault_base_url: str,
        key_name: str,
        restore_blob_details: Optional["_models.SelectiveKeyRestoreOperationParameters"] = None,
        **kwargs
    ) -> "_models.SelectiveKeyRestoreOperation":
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.SelectiveKeyRestoreOperation"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "7.2-preview"
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self._selective_key_restore_operation_initial.metadata['url']  # type: ignore
        path_format_arguments = {
            'vaultBaseUrl': self._serialize.url("vault_base_url", vault_base_url, 'str', skip_quote=True),
            'keyName': self._serialize.url("key_name", key_name, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        if restore_blob_details is not None:
            body_content = self._serialize.body(restore_blob_details, 'SelectiveKeyRestoreOperationParameters')
        else:
            body_content = None
        body_content_kwargs['content'] = body_content
        request = self._client.put(url, query_parameters, header_parameters, **body_content_kwargs)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.KeyVaultError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        response_headers = {}
        response_headers['Retry-After']=self._deserialize('int', response.headers.get('Retry-After'))
        response_headers['Azure-AsyncOperation']=self._deserialize('str', response.headers.get('Azure-AsyncOperation'))
        deserialized = self._deserialize('SelectiveKeyRestoreOperation', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, response_headers)

        return deserialized
    _selective_key_restore_operation_initial.metadata = {'url': '/keys/{keyName}/restore'}  # type: ignore

    async def begin_selective_key_restore_operation(
        self,
        vault_base_url: str,
        key_name: str,
        restore_blob_details: Optional["_models.SelectiveKeyRestoreOperationParameters"] = None,
        **kwargs
    ) -> AsyncLROPoller["_models.SelectiveKeyRestoreOperation"]:
        """Restores all key versions of a given key using user supplied SAS token pointing to a previously
        stored Azure Blob storage backup folder.

        :param vault_base_url: The vault name, for example https://myvault.vault.azure.net.
        :type vault_base_url: str
        :param key_name: The name of the key to be restored from the user supplied backup.
        :type key_name: str
        :param restore_blob_details: The Azure blob SAS token pointing to a folder where the previous
         successful full backup was stored.
        :type restore_blob_details: ~azure.keyvault.v7_2.models.SelectiveKeyRestoreOperationParameters
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: Pass in True if you'd like the AsyncARMPolling polling method,
         False for no polling, or your own initialized polling object for a personal polling strategy.
        :paramtype polling: bool or ~azure.core.polling.AsyncPollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no Retry-After header is present.
        :return: An instance of AsyncLROPoller that returns either SelectiveKeyRestoreOperation or the result of cls(response)
        :rtype: ~azure.core.polling.AsyncLROPoller[~azure.keyvault.v7_2.models.SelectiveKeyRestoreOperation]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        polling = kwargs.pop('polling', True)  # type: Union[bool, AsyncPollingMethod]
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.SelectiveKeyRestoreOperation"]
        lro_delay = kwargs.pop(
            'polling_interval',
            self._config.polling_interval
        )
        cont_token = kwargs.pop('continuation_token', None)  # type: Optional[str]
        if cont_token is None:
            raw_result = await self._selective_key_restore_operation_initial(
                vault_base_url=vault_base_url,
                key_name=key_name,
                restore_blob_details=restore_blob_details,
                cls=lambda x,y,z: x,
                **kwargs
            )

        kwargs.pop('error_map', None)
        kwargs.pop('content_type', None)

        def get_long_running_output(pipeline_response):
            response_headers = {}
            response = pipeline_response.http_response
            response_headers['Retry-After']=self._deserialize('int', response.headers.get('Retry-After'))
            response_headers['Azure-AsyncOperation']=self._deserialize('str', response.headers.get('Azure-AsyncOperation'))
            deserialized = self._deserialize('SelectiveKeyRestoreOperation', pipeline_response)

            if cls:
                return cls(pipeline_response, deserialized, response_headers)
            return deserialized

        path_format_arguments = {
            'vaultBaseUrl': self._serialize.url("vault_base_url", vault_base_url, 'str', skip_quote=True),
            'keyName': self._serialize.url("key_name", key_name, 'str'),
        }

        if polling is True: polling_method = AsyncARMPolling(lro_delay, lro_options={'final-state-via': 'azure-async-operation'}, path_format_arguments=path_format_arguments,  **kwargs)
        elif polling is False: polling_method = AsyncNoPolling()
        else: polling_method = polling
        if cont_token:
            return AsyncLROPoller.from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output
            )
        else:
            return AsyncLROPoller(self._client, raw_result, get_long_running_output, polling_method)
    begin_selective_key_restore_operation.metadata = {'url': '/keys/{keyName}/restore'}  # type: ignore

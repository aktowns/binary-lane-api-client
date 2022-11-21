from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.action_response import ActionResponse
from ...models.enable_backups import EnableBackups
from ...models.problem_details import ProblemDetails
from ...models.validation_problem_details import ValidationProblemDetails
from ...types import Response


def _get_kwargs(
    server_id: int,
    *,
    client: Client,
    json_body: EnableBackups,
) -> Dict[str, Any]:
    url = "{}/v2/servers/{server_id}/actions#EnableBackups".format(client.base_url, server_id=server_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(
    *, response: httpx.Response
) -> Optional[Union[ActionResponse, Any, ProblemDetails, ValidationProblemDetails]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ActionResponse.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.ACCEPTED:
        response_202 = cast(Any, None)
        return response_202
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = ValidationProblemDetails.from_dict(response.json())

        return response_400
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = ProblemDetails.from_dict(response.json())

        return response_404
    if response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY:
        response_422 = ProblemDetails.from_dict(response.json())

        return response_422
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = cast(Any, None)
        return response_401
    return None


def _build_response(
    *, response: httpx.Response
) -> Response[Union[ActionResponse, Any, ProblemDetails, ValidationProblemDetails]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    server_id: int,
    *,
    client: Client,
    json_body: EnableBackups,
) -> Response[Union[ActionResponse, Any, ProblemDetails, ValidationProblemDetails]]:
    """Enable Two Daily Backups for an Existing Server

     This will enable two daily backups if the server currently has no backups. This is not an 'un-pause'
    for backups. It will change the server's options to enable two daily backups.
    For greater control over the backup options use Options property on the Resize action.


    Args:
        server_id (int): The target server id.
        json_body (EnableBackups): Enable Two Daily Backups for an Existing Server

    Returns:
        Response[Union[ActionResponse, Any, ProblemDetails, ValidationProblemDetails]]
    """

    kwargs = _get_kwargs(
        server_id=server_id,
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    server_id: int,
    *,
    client: Client,
    json_body: EnableBackups,
) -> Optional[Union[ActionResponse, Any, ProblemDetails, ValidationProblemDetails]]:
    """Enable Two Daily Backups for an Existing Server

     This will enable two daily backups if the server currently has no backups. This is not an 'un-pause'
    for backups. It will change the server's options to enable two daily backups.
    For greater control over the backup options use Options property on the Resize action.


    Args:
        server_id (int): The target server id.
        json_body (EnableBackups): Enable Two Daily Backups for an Existing Server

    Returns:
        Response[Union[ActionResponse, Any, ProblemDetails, ValidationProblemDetails]]
    """

    return sync_detailed(
        server_id=server_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    server_id: int,
    *,
    client: Client,
    json_body: EnableBackups,
) -> Response[Union[ActionResponse, Any, ProblemDetails, ValidationProblemDetails]]:
    """Enable Two Daily Backups for an Existing Server

     This will enable two daily backups if the server currently has no backups. This is not an 'un-pause'
    for backups. It will change the server's options to enable two daily backups.
    For greater control over the backup options use Options property on the Resize action.


    Args:
        server_id (int): The target server id.
        json_body (EnableBackups): Enable Two Daily Backups for an Existing Server

    Returns:
        Response[Union[ActionResponse, Any, ProblemDetails, ValidationProblemDetails]]
    """

    kwargs = _get_kwargs(
        server_id=server_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    server_id: int,
    *,
    client: Client,
    json_body: EnableBackups,
) -> Optional[Union[ActionResponse, Any, ProblemDetails, ValidationProblemDetails]]:
    """Enable Two Daily Backups for an Existing Server

     This will enable two daily backups if the server currently has no backups. This is not an 'un-pause'
    for backups. It will change the server's options to enable two daily backups.
    For greater control over the backup options use Options property on the Resize action.


    Args:
        server_id (int): The target server id.
        json_body (EnableBackups): Enable Two Daily Backups for an Existing Server

    Returns:
        Response[Union[ActionResponse, Any, ProblemDetails, ValidationProblemDetails]]
    """

    return (
        await asyncio_detailed(
            server_id=server_id,
            client=client,
            json_body=json_body,
        )
    ).parsed

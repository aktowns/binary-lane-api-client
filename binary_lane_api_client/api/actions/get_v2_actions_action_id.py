from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.action_response import ActionResponse
from ...models.problem_details import ProblemDetails
from ...types import Response


def _get_kwargs(
    action_id: int,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/v2/actions/{action_id}".format(client.base_url, action_id=action_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[ActionResponse, Any, ProblemDetails]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ActionResponse.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = ProblemDetails.from_dict(response.json())

        return response_404
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = cast(Any, None)
        return response_401
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[ActionResponse, Any, ProblemDetails]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    action_id: int,
    *,
    client: Client,
) -> Response[Union[ActionResponse, Any, ProblemDetails]]:
    """Fetch an Existing Action

    Args:
        action_id (int):

    Returns:
        Response[Union[ActionResponse, Any, ProblemDetails]]
    """

    kwargs = _get_kwargs(
        action_id=action_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    action_id: int,
    *,
    client: Client,
) -> Optional[Union[ActionResponse, Any, ProblemDetails]]:
    """Fetch an Existing Action

    Args:
        action_id (int):

    Returns:
        Response[Union[ActionResponse, Any, ProblemDetails]]
    """

    return sync_detailed(
        action_id=action_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    action_id: int,
    *,
    client: Client,
) -> Response[Union[ActionResponse, Any, ProblemDetails]]:
    """Fetch an Existing Action

    Args:
        action_id (int):

    Returns:
        Response[Union[ActionResponse, Any, ProblemDetails]]
    """

    kwargs = _get_kwargs(
        action_id=action_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    action_id: int,
    *,
    client: Client,
) -> Optional[Union[ActionResponse, Any, ProblemDetails]]:
    """Fetch an Existing Action

    Args:
        action_id (int):

    Returns:
        Response[Union[ActionResponse, Any, ProblemDetails]]
    """

    return (
        await asyncio_detailed(
            action_id=action_id,
            client=client,
        )
    ).parsed

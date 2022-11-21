from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.problem_details import ProblemDetails
from ...models.user_data import UserData
from ...types import Response


def _get_kwargs(
    server_id: int,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/v2/servers/{server_id}/user_data".format(client.base_url, server_id=server_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, ProblemDetails, UserData]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = UserData.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = ProblemDetails.from_dict(response.json())

        return response_404
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = cast(Any, None)
        return response_401
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, ProblemDetails, UserData]]:
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
) -> Response[Union[Any, ProblemDetails, UserData]]:
    """Fetch the Currently Set UserData for a Server

    Args:
        server_id (int): The target server id.

    Returns:
        Response[Union[Any, ProblemDetails, UserData]]
    """

    kwargs = _get_kwargs(
        server_id=server_id,
        client=client,
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
) -> Optional[Union[Any, ProblemDetails, UserData]]:
    """Fetch the Currently Set UserData for a Server

    Args:
        server_id (int): The target server id.

    Returns:
        Response[Union[Any, ProblemDetails, UserData]]
    """

    return sync_detailed(
        server_id=server_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    server_id: int,
    *,
    client: Client,
) -> Response[Union[Any, ProblemDetails, UserData]]:
    """Fetch the Currently Set UserData for a Server

    Args:
        server_id (int): The target server id.

    Returns:
        Response[Union[Any, ProblemDetails, UserData]]
    """

    kwargs = _get_kwargs(
        server_id=server_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    server_id: int,
    *,
    client: Client,
) -> Optional[Union[Any, ProblemDetails, UserData]]:
    """Fetch the Currently Set UserData for a Server

    Args:
        server_id (int): The target server id.

    Returns:
        Response[Union[Any, ProblemDetails, UserData]]
    """

    return (
        await asyncio_detailed(
            server_id=server_id,
            client=client,
        )
    ).parsed

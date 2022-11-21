from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.problem_details import ProblemDetails
from ...types import Response


def _get_kwargs(
    key_id: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/v2/account/keys/{key_id}".format(client.base_url, key_id=key_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "delete",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, ProblemDetails]]:
    if response.status_code == HTTPStatus.NO_CONTENT:
        response_204 = cast(Any, None)
        return response_204
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = ProblemDetails.from_dict(response.json())

        return response_404
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = cast(Any, None)
        return response_401
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, ProblemDetails]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    key_id: str,
    *,
    client: Client,
) -> Response[Union[Any, ProblemDetails]]:
    """Delete an Existing SSH Key

     The key_id may be either the Id or the key fingerprint.

    Args:
        key_id (str):

    Returns:
        Response[Union[Any, ProblemDetails]]
    """

    kwargs = _get_kwargs(
        key_id=key_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    key_id: str,
    *,
    client: Client,
) -> Optional[Union[Any, ProblemDetails]]:
    """Delete an Existing SSH Key

     The key_id may be either the Id or the key fingerprint.

    Args:
        key_id (str):

    Returns:
        Response[Union[Any, ProblemDetails]]
    """

    return sync_detailed(
        key_id=key_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    key_id: str,
    *,
    client: Client,
) -> Response[Union[Any, ProblemDetails]]:
    """Delete an Existing SSH Key

     The key_id may be either the Id or the key fingerprint.

    Args:
        key_id (str):

    Returns:
        Response[Union[Any, ProblemDetails]]
    """

    kwargs = _get_kwargs(
        key_id=key_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    key_id: str,
    *,
    client: Client,
) -> Optional[Union[Any, ProblemDetails]]:
    """Delete an Existing SSH Key

     The key_id may be either the Id or the key fingerprint.

    Args:
        key_id (str):

    Returns:
        Response[Union[Any, ProblemDetails]]
    """

    return (
        await asyncio_detailed(
            key_id=key_id,
            client=client,
        )
    ).parsed

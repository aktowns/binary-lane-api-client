from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.failover_ips_response import FailoverIpsResponse
from ...models.problem_details import ProblemDetails
from ...types import UNSET, Response, Unset


def _get_kwargs(
    server_id: int,
    *,
    client: Client,
    page: Union[Unset, None, int] = 1,
    per_page: Union[Unset, None, int] = 20,
) -> Dict[str, Any]:
    url = "{}/v2/failover_ips/{server_id}".format(client.base_url, server_id=server_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["page"] = page

    params["per_page"] = per_page

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, FailoverIpsResponse, ProblemDetails]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = FailoverIpsResponse.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = ProblemDetails.from_dict(response.json())

        return response_404
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = cast(Any, None)
        return response_401
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, FailoverIpsResponse, ProblemDetails]]:
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
    page: Union[Unset, None, int] = 1,
    per_page: Union[Unset, None, int] = 20,
) -> Response[Union[Any, FailoverIpsResponse, ProblemDetails]]:
    """Fetch the Failover IPs for a Server

    Args:
        server_id (int): The target server id.
        page (Union[Unset, None, int]): The selected page. Page numbering starts at 1 Default: 1.
        per_page (Union[Unset, None, int]): The number of results to show per page. Default: 20.

    Returns:
        Response[Union[Any, FailoverIpsResponse, ProblemDetails]]
    """

    kwargs = _get_kwargs(
        server_id=server_id,
        client=client,
        page=page,
        per_page=per_page,
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
    page: Union[Unset, None, int] = 1,
    per_page: Union[Unset, None, int] = 20,
) -> Optional[Union[Any, FailoverIpsResponse, ProblemDetails]]:
    """Fetch the Failover IPs for a Server

    Args:
        server_id (int): The target server id.
        page (Union[Unset, None, int]): The selected page. Page numbering starts at 1 Default: 1.
        per_page (Union[Unset, None, int]): The number of results to show per page. Default: 20.

    Returns:
        Response[Union[Any, FailoverIpsResponse, ProblemDetails]]
    """

    return sync_detailed(
        server_id=server_id,
        client=client,
        page=page,
        per_page=per_page,
    ).parsed


async def asyncio_detailed(
    server_id: int,
    *,
    client: Client,
    page: Union[Unset, None, int] = 1,
    per_page: Union[Unset, None, int] = 20,
) -> Response[Union[Any, FailoverIpsResponse, ProblemDetails]]:
    """Fetch the Failover IPs for a Server

    Args:
        server_id (int): The target server id.
        page (Union[Unset, None, int]): The selected page. Page numbering starts at 1 Default: 1.
        per_page (Union[Unset, None, int]): The number of results to show per page. Default: 20.

    Returns:
        Response[Union[Any, FailoverIpsResponse, ProblemDetails]]
    """

    kwargs = _get_kwargs(
        server_id=server_id,
        client=client,
        page=page,
        per_page=per_page,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    server_id: int,
    *,
    client: Client,
    page: Union[Unset, None, int] = 1,
    per_page: Union[Unset, None, int] = 20,
) -> Optional[Union[Any, FailoverIpsResponse, ProblemDetails]]:
    """Fetch the Failover IPs for a Server

    Args:
        server_id (int): The target server id.
        page (Union[Unset, None, int]): The selected page. Page numbering starts at 1 Default: 1.
        per_page (Union[Unset, None, int]): The number of results to show per page. Default: 20.

    Returns:
        Response[Union[Any, FailoverIpsResponse, ProblemDetails]]
    """

    return (
        await asyncio_detailed(
            server_id=server_id,
            client=client,
            page=page,
            per_page=per_page,
        )
    ).parsed
from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.current_server_alerts_response import CurrentServerAlertsResponse
from ...models.problem_details import ProblemDetails
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/v2/servers/threshold_alerts".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, CurrentServerAlertsResponse, ProblemDetails]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = CurrentServerAlertsResponse.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = ProblemDetails.from_dict(response.json())

        return response_404
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = cast(Any, None)
        return response_401
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, CurrentServerAlertsResponse, ProblemDetails]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
) -> Response[Union[Any, CurrentServerAlertsResponse, ProblemDetails]]:
    """List any Servers that have a Current Exceeded Threshold Alert

    Returns:
        Response[Union[Any, CurrentServerAlertsResponse, ProblemDetails]]
    """

    kwargs = _get_kwargs(
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
) -> Optional[Union[Any, CurrentServerAlertsResponse, ProblemDetails]]:
    """List any Servers that have a Current Exceeded Threshold Alert

    Returns:
        Response[Union[Any, CurrentServerAlertsResponse, ProblemDetails]]
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
) -> Response[Union[Any, CurrentServerAlertsResponse, ProblemDetails]]:
    """List any Servers that have a Current Exceeded Threshold Alert

    Returns:
        Response[Union[Any, CurrentServerAlertsResponse, ProblemDetails]]
    """

    kwargs = _get_kwargs(
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
) -> Optional[Union[Any, CurrentServerAlertsResponse, ProblemDetails]]:
    """List any Servers that have a Current Exceeded Threshold Alert

    Returns:
        Response[Union[Any, CurrentServerAlertsResponse, ProblemDetails]]
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed

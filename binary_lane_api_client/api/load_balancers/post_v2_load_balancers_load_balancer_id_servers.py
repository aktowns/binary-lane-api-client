from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.problem_details import ProblemDetails
from ...models.server_ids_request import ServerIdsRequest
from ...models.validation_problem_details import ValidationProblemDetails
from ...types import Response


def _get_kwargs(
    load_balancer_id: int,
    *,
    client: Client,
    json_body: ServerIdsRequest,
) -> Dict[str, Any]:
    url = "{}/v2/load_balancers/{load_balancer_id}/servers".format(client.base_url, load_balancer_id=load_balancer_id)

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


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, ProblemDetails, ValidationProblemDetails]]:
    if response.status_code == HTTPStatus.NO_CONTENT:
        response_204 = cast(Any, None)
        return response_204
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


def _build_response(*, response: httpx.Response) -> Response[Union[Any, ProblemDetails, ValidationProblemDetails]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    load_balancer_id: int,
    *,
    client: Client,
    json_body: ServerIdsRequest,
) -> Response[Union[Any, ProblemDetails, ValidationProblemDetails]]:
    """Add Servers to an Existing Load Balancer

    Args:
        load_balancer_id (int):
        json_body (ServerIdsRequest):

    Returns:
        Response[Union[Any, ProblemDetails, ValidationProblemDetails]]
    """

    kwargs = _get_kwargs(
        load_balancer_id=load_balancer_id,
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    load_balancer_id: int,
    *,
    client: Client,
    json_body: ServerIdsRequest,
) -> Optional[Union[Any, ProblemDetails, ValidationProblemDetails]]:
    """Add Servers to an Existing Load Balancer

    Args:
        load_balancer_id (int):
        json_body (ServerIdsRequest):

    Returns:
        Response[Union[Any, ProblemDetails, ValidationProblemDetails]]
    """

    return sync_detailed(
        load_balancer_id=load_balancer_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    load_balancer_id: int,
    *,
    client: Client,
    json_body: ServerIdsRequest,
) -> Response[Union[Any, ProblemDetails, ValidationProblemDetails]]:
    """Add Servers to an Existing Load Balancer

    Args:
        load_balancer_id (int):
        json_body (ServerIdsRequest):

    Returns:
        Response[Union[Any, ProblemDetails, ValidationProblemDetails]]
    """

    kwargs = _get_kwargs(
        load_balancer_id=load_balancer_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    load_balancer_id: int,
    *,
    client: Client,
    json_body: ServerIdsRequest,
) -> Optional[Union[Any, ProblemDetails, ValidationProblemDetails]]:
    """Add Servers to an Existing Load Balancer

    Args:
        load_balancer_id (int):
        json_body (ServerIdsRequest):

    Returns:
        Response[Union[Any, ProblemDetails, ValidationProblemDetails]]
    """

    return (
        await asyncio_detailed(
            load_balancer_id=load_balancer_id,
            client=client,
            json_body=json_body,
        )
    ).parsed

from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.patch_vpc_request import PatchVpcRequest
from ...models.problem_details import ProblemDetails
from ...models.validation_problem_details import ValidationProblemDetails
from ...models.vpc_response import VpcResponse
from ...types import Response


def _get_kwargs(
    vpc_id: int,
    *,
    client: Client,
    json_body: PatchVpcRequest,
) -> Dict[str, Any]:
    url = "{}/v2/vpcs/{vpc_id}".format(client.base_url, vpc_id=vpc_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "patch",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(
    *, response: httpx.Response
) -> Optional[Union[Any, ProblemDetails, ValidationProblemDetails, VpcResponse]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = VpcResponse.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = ValidationProblemDetails.from_dict(response.json())

        return response_400
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = ProblemDetails.from_dict(response.json())

        return response_404
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = cast(Any, None)
        return response_401
    return None


def _build_response(
    *, response: httpx.Response
) -> Response[Union[Any, ProblemDetails, ValidationProblemDetails, VpcResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    vpc_id: int,
    *,
    client: Client,
    json_body: PatchVpcRequest,
) -> Response[Union[Any, ProblemDetails, ValidationProblemDetails, VpcResponse]]:
    """Update an Existing VPC

     Anything not included in this will be un-altered.

    Args:
        vpc_id (int): The target vpc id.
        json_body (PatchVpcRequest):

    Returns:
        Response[Union[Any, ProblemDetails, ValidationProblemDetails, VpcResponse]]
    """

    kwargs = _get_kwargs(
        vpc_id=vpc_id,
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    vpc_id: int,
    *,
    client: Client,
    json_body: PatchVpcRequest,
) -> Optional[Union[Any, ProblemDetails, ValidationProblemDetails, VpcResponse]]:
    """Update an Existing VPC

     Anything not included in this will be un-altered.

    Args:
        vpc_id (int): The target vpc id.
        json_body (PatchVpcRequest):

    Returns:
        Response[Union[Any, ProblemDetails, ValidationProblemDetails, VpcResponse]]
    """

    return sync_detailed(
        vpc_id=vpc_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    vpc_id: int,
    *,
    client: Client,
    json_body: PatchVpcRequest,
) -> Response[Union[Any, ProblemDetails, ValidationProblemDetails, VpcResponse]]:
    """Update an Existing VPC

     Anything not included in this will be un-altered.

    Args:
        vpc_id (int): The target vpc id.
        json_body (PatchVpcRequest):

    Returns:
        Response[Union[Any, ProblemDetails, ValidationProblemDetails, VpcResponse]]
    """

    kwargs = _get_kwargs(
        vpc_id=vpc_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    vpc_id: int,
    *,
    client: Client,
    json_body: PatchVpcRequest,
) -> Optional[Union[Any, ProblemDetails, ValidationProblemDetails, VpcResponse]]:
    """Update an Existing VPC

     Anything not included in this will be un-altered.

    Args:
        vpc_id (int): The target vpc id.
        json_body (PatchVpcRequest):

    Returns:
        Response[Union[Any, ProblemDetails, ValidationProblemDetails, VpcResponse]]
    """

    return (
        await asyncio_detailed(
            vpc_id=vpc_id,
            client=client,
            json_body=json_body,
        )
    ).parsed

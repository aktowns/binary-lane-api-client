from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.image_request import ImageRequest
from ...models.image_response import ImageResponse
from ...models.problem_details import ProblemDetails
from ...models.validation_problem_details import ValidationProblemDetails
from ...types import Response


def _get_kwargs(
    image_id: int,
    *,
    client: Client,
    json_body: ImageRequest,
) -> Dict[str, Any]:
    url = "{}/v2/images/{image_id}".format(client.base_url, image_id=image_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "put",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(
    *, response: httpx.Response
) -> Optional[Union[Any, ImageResponse, ProblemDetails, ValidationProblemDetails]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ImageResponse.from_dict(response.json())

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
) -> Response[Union[Any, ImageResponse, ProblemDetails, ValidationProblemDetails]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    image_id: int,
    *,
    client: Client,
    json_body: ImageRequest,
) -> Response[Union[Any, ImageResponse, ProblemDetails, ValidationProblemDetails]]:
    """Update an Existing Image

     Only updating of user created backups is currently supported.

    Args:
        image_id (int):
        json_body (ImageRequest):

    Returns:
        Response[Union[Any, ImageResponse, ProblemDetails, ValidationProblemDetails]]
    """

    kwargs = _get_kwargs(
        image_id=image_id,
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    image_id: int,
    *,
    client: Client,
    json_body: ImageRequest,
) -> Optional[Union[Any, ImageResponse, ProblemDetails, ValidationProblemDetails]]:
    """Update an Existing Image

     Only updating of user created backups is currently supported.

    Args:
        image_id (int):
        json_body (ImageRequest):

    Returns:
        Response[Union[Any, ImageResponse, ProblemDetails, ValidationProblemDetails]]
    """

    return sync_detailed(
        image_id=image_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    image_id: int,
    *,
    client: Client,
    json_body: ImageRequest,
) -> Response[Union[Any, ImageResponse, ProblemDetails, ValidationProblemDetails]]:
    """Update an Existing Image

     Only updating of user created backups is currently supported.

    Args:
        image_id (int):
        json_body (ImageRequest):

    Returns:
        Response[Union[Any, ImageResponse, ProblemDetails, ValidationProblemDetails]]
    """

    kwargs = _get_kwargs(
        image_id=image_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    image_id: int,
    *,
    client: Client,
    json_body: ImageRequest,
) -> Optional[Union[Any, ImageResponse, ProblemDetails, ValidationProblemDetails]]:
    """Update an Existing Image

     Only updating of user created backups is currently supported.

    Args:
        image_id (int):
        json_body (ImageRequest):

    Returns:
        Response[Union[Any, ImageResponse, ProblemDetails, ValidationProblemDetails]]
    """

    return (
        await asyncio_detailed(
            image_id=image_id,
            client=client,
            json_body=json_body,
        )
    ).parsed

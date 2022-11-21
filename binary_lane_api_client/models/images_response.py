from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.image import Image
    from ..models.links import Links
    from ..models.meta import Meta


T = TypeVar("T", bound="ImagesResponse")


@attr.s(auto_attribs=True)
class ImagesResponse:
    """
    Attributes:
        meta (Meta): Contains metadata about the response, currently this includes the total number of items.
        images (List['Image']):
        links (Union[Unset, None, Links]):
    """

    meta: "Meta"
    images: List["Image"]
    links: Union[Unset, None, "Links"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        meta = self.meta.to_dict()

        images = []
        for images_item_data in self.images:
            images_item = images_item_data.to_dict()

            images.append(images_item)

        links: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict() if self.links else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "meta": meta,
                "images": images,
            }
        )
        if links is not UNSET:
            field_dict["links"] = links

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.image import Image
        from ..models.links import Links
        from ..models.meta import Meta

        d = src_dict.copy()
        meta = Meta.from_dict(d.pop("meta"))

        images = []
        _images = d.pop("images")
        for images_item_data in _images:
            images_item = Image.from_dict(images_item_data)

            images.append(images_item)

        _links = d.pop("links", UNSET)
        links: Union[Unset, None, Links]
        if _links is None:
            links = None
        elif isinstance(_links, Unset):
            links = UNSET
        else:
            links = Links.from_dict(_links)

        images_response = cls(
            meta=meta,
            images=images,
            links=links,
        )

        images_response.additional_properties = d
        return images_response

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties

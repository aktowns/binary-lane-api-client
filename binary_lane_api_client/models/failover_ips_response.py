from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.links import Links
    from ..models.meta import Meta


T = TypeVar("T", bound="FailoverIpsResponse")


@attr.s(auto_attribs=True)
class FailoverIpsResponse:
    """
    Attributes:
        meta (Meta): Contains metadata about the response, currently this includes the total number of items.
        failover_ips (List[str]):
        links (Union[Unset, None, Links]):
    """

    meta: "Meta"
    failover_ips: List[str]
    links: Union[Unset, None, "Links"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        meta = self.meta.to_dict()

        failover_ips = self.failover_ips

        links: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict() if self.links else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "meta": meta,
                "failover_ips": failover_ips,
            }
        )
        if links is not UNSET:
            field_dict["links"] = links

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.links import Links
        from ..models.meta import Meta

        d = src_dict.copy()
        meta = Meta.from_dict(d.pop("meta"))

        failover_ips = cast(List[str], d.pop("failover_ips"))

        _links = d.pop("links", UNSET)
        links: Union[Unset, None, Links]
        if _links is None:
            links = None
        elif isinstance(_links, Unset):
            links = UNSET
        else:
            links = Links.from_dict(_links)

        failover_ips_response = cls(
            meta=meta,
            failover_ips=failover_ips,
            links=links,
        )

        failover_ips_response.additional_properties = d
        return failover_ips_response

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

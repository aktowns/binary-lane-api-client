from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.links import Links
    from ..models.load_balancer import LoadBalancer
    from ..models.meta import Meta


T = TypeVar("T", bound="LoadBalancersResponse")


@attr.s(auto_attribs=True)
class LoadBalancersResponse:
    """
    Attributes:
        meta (Meta): Contains metadata about the response, currently this includes the total number of items.
        load_balancers (List['LoadBalancer']):
        links (Union[Unset, None, Links]):
    """

    meta: "Meta"
    load_balancers: List["LoadBalancer"]
    links: Union[Unset, None, "Links"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        meta = self.meta.to_dict()

        load_balancers = []
        for load_balancers_item_data in self.load_balancers:
            load_balancers_item = load_balancers_item_data.to_dict()

            load_balancers.append(load_balancers_item)

        links: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict() if self.links else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "meta": meta,
                "load_balancers": load_balancers,
            }
        )
        if links is not UNSET:
            field_dict["links"] = links

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.links import Links
        from ..models.load_balancer import LoadBalancer
        from ..models.meta import Meta

        d = src_dict.copy()
        meta = Meta.from_dict(d.pop("meta"))

        load_balancers = []
        _load_balancers = d.pop("load_balancers")
        for load_balancers_item_data in _load_balancers:
            load_balancers_item = LoadBalancer.from_dict(load_balancers_item_data)

            load_balancers.append(load_balancers_item)

        _links = d.pop("links", UNSET)
        links: Union[Unset, None, Links]
        if _links is None:
            links = None
        elif isinstance(_links, Unset):
            links = UNSET
        else:
            links = Links.from_dict(_links)

        load_balancers_response = cls(
            meta=meta,
            load_balancers=load_balancers,
            links=links,
        )

        load_balancers_response.additional_properties = d
        return load_balancers_response

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

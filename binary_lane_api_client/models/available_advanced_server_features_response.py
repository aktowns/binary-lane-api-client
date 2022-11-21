from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.available_advanced_server_features import AvailableAdvancedServerFeatures


T = TypeVar("T", bound="AvailableAdvancedServerFeaturesResponse")


@attr.s(auto_attribs=True)
class AvailableAdvancedServerFeaturesResponse:
    """
    Attributes:
        available_advanced_server_features (AvailableAdvancedServerFeatures):
    """

    available_advanced_server_features: "AvailableAdvancedServerFeatures"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        available_advanced_server_features = self.available_advanced_server_features.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "available_advanced_server_features": available_advanced_server_features,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.available_advanced_server_features import AvailableAdvancedServerFeatures

        d = src_dict.copy()
        available_advanced_server_features = AvailableAdvancedServerFeatures.from_dict(
            d.pop("available_advanced_server_features")
        )

        available_advanced_server_features_response = cls(
            available_advanced_server_features=available_advanced_server_features,
        )

        available_advanced_server_features_response.additional_properties = d
        return available_advanced_server_features_response

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

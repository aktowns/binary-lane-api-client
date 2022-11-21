from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.ssh_key import SshKey


T = TypeVar("T", bound="SshKeyResponse")


@attr.s(auto_attribs=True)
class SshKeyResponse:
    """
    Attributes:
        ssh_key (SshKey):
    """

    ssh_key: "SshKey"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ssh_key = self.ssh_key.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ssh_key": ssh_key,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.ssh_key import SshKey

        d = src_dict.copy()
        ssh_key = SshKey.from_dict(d.pop("ssh_key"))

        ssh_key_response = cls(
            ssh_key=ssh_key,
        )

        ssh_key_response.additional_properties = d
        return ssh_key_response

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

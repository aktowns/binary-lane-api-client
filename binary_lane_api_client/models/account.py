from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.account_status import AccountStatus
from ..models.payment_method import PaymentMethod
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.tax_code import TaxCode


T = TypeVar("T", bound="Account")


@attr.s(auto_attribs=True)
class Account:
    """
    Attributes:
        server_limit (int): Server limits are not currently implemented and this value will always be int32.MaxValue.
        floating_ip_limit (int): Floating IPs are not currently implemented and this value will always be 0.
        volume_limit (int): Volumes are not currently implemented and this value will always be 0.
        email (str): The email address registered for this account.
        uuid (str): The ID of this account.
        email_verified (bool): Whether this account has been verified. Un-verified accounts are subject to some
            restrictions.
        status (AccountStatus):
            | Value | Description |
            | ----- | ----------- |
            | incomplete | An account that exists but is not ready for use. The most common reason for this is a lack of
            payment information. |
            | active | An account in the normal state. |
            | warning | An account that is under review. If you are unsure why your account has this status please urgently
            contact support. |
            | locked | An account that is no longer permitted to access the service. |

        tax_code (TaxCode):
        configured_payment_methods (List[PaymentMethod]): The payment methods that are configured (available) for this
            account.
        status_message (Union[Unset, None, str]): A message explaining the account status. This is not currently
            supported.
    """

    server_limit: int
    floating_ip_limit: int
    volume_limit: int
    email: str
    uuid: str
    email_verified: bool
    status: AccountStatus
    tax_code: "TaxCode"
    configured_payment_methods: List[PaymentMethod]
    status_message: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        server_limit = self.server_limit
        floating_ip_limit = self.floating_ip_limit
        volume_limit = self.volume_limit
        email = self.email
        uuid = self.uuid
        email_verified = self.email_verified
        status = self.status.value

        tax_code = self.tax_code.to_dict()

        configured_payment_methods = []
        for configured_payment_methods_item_data in self.configured_payment_methods:
            configured_payment_methods_item = configured_payment_methods_item_data.value

            configured_payment_methods.append(configured_payment_methods_item)

        status_message = self.status_message

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "server_limit": server_limit,
                "floating_ip_limit": floating_ip_limit,
                "volume_limit": volume_limit,
                "email": email,
                "uuid": uuid,
                "email_verified": email_verified,
                "status": status,
                "tax_code": tax_code,
                "configured_payment_methods": configured_payment_methods,
            }
        )
        if status_message is not UNSET:
            field_dict["status_message"] = status_message

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.tax_code import TaxCode

        d = src_dict.copy()
        server_limit = d.pop("server_limit")

        floating_ip_limit = d.pop("floating_ip_limit")

        volume_limit = d.pop("volume_limit")

        email = d.pop("email")

        uuid = d.pop("uuid")

        email_verified = d.pop("email_verified")

        status = AccountStatus(d.pop("status"))

        tax_code = TaxCode.from_dict(d.pop("tax_code"))

        configured_payment_methods = []
        _configured_payment_methods = d.pop("configured_payment_methods")
        for configured_payment_methods_item_data in _configured_payment_methods:
            configured_payment_methods_item = PaymentMethod(configured_payment_methods_item_data)

            configured_payment_methods.append(configured_payment_methods_item)

        status_message = d.pop("status_message", UNSET)

        account = cls(
            server_limit=server_limit,
            floating_ip_limit=floating_ip_limit,
            volume_limit=volume_limit,
            email=email,
            uuid=uuid,
            email_verified=email_verified,
            status=status,
            tax_code=tax_code,
            configured_payment_methods=configured_payment_methods,
            status_message=status_message,
        )

        account.additional_properties = d
        return account

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

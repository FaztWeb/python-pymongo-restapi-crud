from dataclasses import dataclass
from dataclasses_json import dataclass_json


@dataclass_json
@dataclass(kw_only=True)
class Person:
    document_number: str = None
    name: str = None
    mail_address: str = None
    phone_number: str = None
    type_document: str = None
    gender: str = None
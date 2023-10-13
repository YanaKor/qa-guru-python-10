import dataclasses


@dataclasses.dataclass
class UserInfo:
    first_name: str
    last_name: str
    email: str
    gender: str
    phone_number: str
    birth_day: str
    birth_month: str
    birth_year: str
    subject: str
    hobbies_number: str
    picture: str
    address: str
    state: str
    city: str

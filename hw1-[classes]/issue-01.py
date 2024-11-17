import keyword


class PricePropertyMixin:
    """
    Mixin for validating price.
    Requires _price attribute.
    """
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")
        self._price = value


class JsonToObject:
    """Base class for converting json to object."""

    def __init__(self, json_obj: dict) -> None:
        for key, value in json_obj.items():
            if keyword.iskeyword(key):
                key = f"{key}_"
            if isinstance(value, dict):
                self.__setattr__(key, JsonToObject(value))
            else:
                self.__setattr__(key, value)


class Advert(PricePropertyMixin, JsonToObject):
    """Advert class."""

    def __init__(self, json_obj: dict) -> None:
        self._price = 0
        super().__init__(json_obj)


if __name__ == "__main__":
    json_obj = {
        "title":	"python",
        "price":	100,
        "location":	{
            "address":	"город	Москва,	Лесная,	7",
            "metro_stations":	["Белорусская"]
        }
    }

    a = Advert(json_obj)
    print(a.location.address)
    print(a.price)
    a.price = -100

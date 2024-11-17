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


class ColorizeMixin:
    def __repr__(self):
        return f"\x1b[{self.repr_color_code}m{super().__repr__()}\x1b[0m"


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

    repr_color_code = 32

    def __init__(self, json_obj: dict) -> None:
        self._price = 0
        super().__init__(json_obj)

    def __repr__(self):
        if hasattr(self, "title"):
            return f"{self.title} | {self.price}"
        raise ValueError("Advert has no title")


class ColorizedAdvert(ColorizeMixin, Advert):
    """Colorized Advert class."""


if __name__ == "__main__":
    json_obj = {
        "title":	"python",
        "price":	100,
        "location":	{
            "address":	"город	Москва,	Лесная,	7",
            "metro_stations":	["Белорусская"]
        }
    }

    a = ColorizedAdvert(json_obj)
    print(a.location.address)
    print(a.price)
    a.price = +100
    print(a)

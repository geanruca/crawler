from dataclasses import dataclass, field
from typing import Optional


@dataclass
class IndexSelector:
    source_url: str = field()
    collection_xpath: str = field()

@dataclass
class BusSelector:
    source_url: Optional[str] = field(default=None)
    title: Optional[str] = field(default=None)
    year: Optional[str] = field(default=None)
    make: Optional[str] = field(default=None)
    model: Optional[str] = field(default=None)
    body: Optional[str] = field(default=None)
    chassis: Optional[str] = field(default=None)
    engine: Optional[str] = field(default=None)
    transmission: Optional[str] = field(default=None)
    mileage: Optional[str] = field(default=None)
    passengers: Optional[str] = field(default=None)
    wheelchair: Optional[str] = field(default=None)
    color: Optional[str] = field(default=None)
    interior_color: Optional[str] = field(default=None)
    exterior_color: Optional[str] = field(default=None)
    sold: bool = field(default=False)
    price: Optional[str] = field(default=None)
    vin: Optional[str] = field(default=None)
    location: Optional[str] = field(default=None)
    brake: Optional[str] = field(default=None)
    contact_email: Optional[str] = field(default=None)
    contact_phone: Optional[str] = field(default=None)
    description: Optional[str] = field(default=None)

    def __str__(self):
        return f"Bus(id={self.id}, title={self.title}, year={self.year}, make={self.make}, model={self.model})"
from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional


@dataclass
class Bus:
    id: Optional[int] = field(default=None)
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
    published: bool = field(default=False)
    featured: bool = field(default=False)
    sold: bool = field(default=False)
    scraped: bool = field(default=False)
    draft: bool = field(default=False)
    source: Optional[str] = field(default=None)
    source_url: Optional[str] = field(default=None)
    price: Optional[str] = field(default=None)
    cprice: Optional[str] = field(default=None)
    vin: Optional[str] = field(default=None)
    updated_at: Optional[datetime] = field(default=None)
    created_at: Optional[datetime] = field(default_factory=datetime.now)
    gvwr: Optional[str] = field(default=None)
    dimensions: Optional[str] = field(default=None)
    luggage: bool = field(default=False)
    state_bus_standard: Optional[str] = field(default=None)
    airconditioning: Optional[str] = field(default=None)  # Choices: 'REAR', 'DASH', 'BOTH', 'OTHER', 'NONE'
    location: Optional[str] = field(default=None)
    brake: Optional[str] = field(default=None)
    contact_email: Optional[str] = field(default=None)
    contact_phone: Optional[str] = field(default=None)
    us_region: str = field(
        default="OTHER")  # Choices: 'NORTHEAST', 'MIDWEST', 'WEST', 'SOUTHWEST', 'SOUTHEAST', 'OTHER'
    description: Optional[str] = field(default=None)
    score: bool = field(default=False)
    category_id: Optional[int] = field(default=0)

    def __str__(self):
        return f"Bus(url={self.source_url}, title={self.title}, year={self.year}, make={self.make}, model={self.model})"
from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Bus:
    title: Optional[str] = field(default=None)
    source_url: Optional[str] = field(default=None)
    price: Optional[str] = field(default=None)
    image_url: Optional[str] = field(default=0)

    def __str__(self):
        return f"Bus(url={self.source_url}, title={self.title}, image_url={self.image_url}, price={self.price})"
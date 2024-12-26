from typing import Dict
from datetime import datetime

from src.Domain.Models.Bus import Bus


def map_scrapped_text_to_bus(data: Dict[str, str]) -> Bus:
    return Bus(
        id=int(data.get("id")) if data.get("id") else None,
        title=data.get("title"),
        year=data.get("year"),
        make=data.get("make"),
        model=data.get("model"),
        body=data.get("body"),
        chassis=data.get("chassis"),
        engine=data.get("engine"),
        transmission=data.get("transmission"),
        mileage=data.get("mileage"),
        passengers=data.get("passengers"),
        wheelchair=data.get("wheelchair"),
        color=data.get("color"),
        interior_color=data.get("interior_color"),
        exterior_color=data.get("exterior_color"),
        published=bool(int(data.get("published", 0))),
        featured=bool(int(data.get("featured", 0))),
        sold=bool(int(data.get("sold", 0))),
        scraped=bool(int(data.get("scraped", 0))),
        draft=bool(int(data.get("draft", 0))),
        source=data.get("source"),
        source_url=data.get("source_url"),
        price=data.get("price"),
        cprice=data.get("cprice"),
        vin=data.get("vin"),
        updated_at=datetime.strptime(data.get("updated_at"), '%Y-%m-%d %H:%M:%S') if data.get("updated_at") else None,
        created_at=datetime.strptime(data.get("created_at"), '%Y-%m-%d %H:%M:%S') if data.get("created_at") else None,
        gvwr=data.get("gvwr"),
        dimensions=data.get("dimensions"),
        luggage=bool(int(data.get("luggage", 0))),
        state_bus_standard=data.get("state_bus_standard"),
        airconditioning=data.get("airconditioning"),
        location=data.get("location"),
        brake=data.get("brake"),
        contact_email=data.get("contact_email"),
        contact_phone=data.get("contact_phone"),
        us_region=data.get("us_region", "OTHER"),
        description=data.get("description"),
        score=bool(int(data.get("score", 0))),
        category_id=int(data.get("category_id")) if data.get("category_id") else 0
    )
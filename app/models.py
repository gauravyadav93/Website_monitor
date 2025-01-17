from pydantic import BaseModel, HttpUrl
from typing import Optional

class SiteCreate(BaseModel):
    url: HttpUrl
    check_interval_seconds: Optional[int] = 300
    name: Optional[str] = None
    expected_status_code: Optional[int] = 200

class Site(SiteCreate):
    id: int
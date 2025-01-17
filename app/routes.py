from fastapi import APIRouter, HTTPException
from app.models import Site, SiteCreate
from app.database import add_site, remove_site, get_sites, get_site_history
from app.tasks import start_monitoring

router = APIRouter()

@router.post("/sites", response_model=Site)
async def create_site(site: SiteCreate):
    return await add_site(site)

@router.delete("/sites/{site_id}")
async def delete_site(site_id: int):
    if not await remove_site(site_id):
        raise HTTPException(status_code=404, detail="Site not found")

@router.get("/sites")
async def list_sites():
    return await get_sites()

@router.get("/sites/{site_id}/history")
async def site_history(site_id: int):
    return await get_site_history(site_id)
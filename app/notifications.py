import asyncio
import httpx
from app.models import Site
from app.notifications import send_discord_notification

async def monitor_site(site: Site):
    while True:
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(site.url, timeout=5)
                # Check status and send notifications
                if response.status_code != site.expected_status_code:
                    await send_discord_notification(site, "DOWN", response.status_code)
                else:
                    await send_discord_notification(site, "UP", response.status_code)
        except Exception as e:
            await send_discord_notification(site, "DOWN", str(e))
        await asyncio.sleep(site.check_interval_seconds)
import pytest
from unittest.mock import patch
from app.notifications import send_discord_notification

@pytest.mark.asyncio
async def test_send_discord_notification():
    site = {
        "name": "My Website",
        "url": "https://example.com"
    }
    with patch('httpx.AsyncClient.post') as mock_post:
        await send_discord_notification(site, "DOWN", "Connection timeout")
        assert mock_post.called
        assert mock_post.call_args[1]['json']['content'].startswith("🔴 Website Down Alert")
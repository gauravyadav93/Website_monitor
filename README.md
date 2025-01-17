# Website Monitoring Service

This is a simple service that monitors website availability and sends notifications through Discord webhooks when a site goes down or recovers.

## Features

- Monitor multiple websites
- Send notifications to Discord on status changes
- Track uptime/downtime history

## API Endpoints

### Add a new site to monitor

**POST** `/sites`

**Request Body:**
```json
{
    "url": "https://example.com",
    "check_interval_seconds": 300,
    "name": "My Website",
    "expected_status_code": 200
}

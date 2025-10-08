"""UpdateNotificationOrganizationNotificationsNotificationIdPut tool implementation."""
import json
import logging
from typing import Any
import requests
from server import mcp

logger = logging.getLogger(__name__)


@mcp.tool()
def updatenotificationorganizationnotificationsnotificationidput(
    notification_id: int,
    organization: str,
    name: str,
    target: str,
    type: str,
    description: str = None,
    enabled: bool = None,
    evergreen: bool = None,
    evergreen_last_reminder_at: str = None,
    evergreen_owner: str = None,
    evergreen_reminder_interval: int = None,
    filters: list = None
) -> str:
    """
    Update Notification
    
    Args:
        notification_id: 
        organization: 
        description: 
        enabled: 
        evergreen: 
        evergreen_last_reminder_at: 
        evergreen_owner: 
        evergreen_reminder_interval: 
        filters: 
        name: 
        target: 
        type: Input parameter: An enumeration.
        
    Returns:
        JSON string result
    """
    from config import load_api_config
    config = load_api_config()
    # Validate required path parameters
    if not notification_id:
        return json.dumps({"error": "Missing required path parameter: notification_id"})
    if not organization:
        return json.dumps({"error": "Missing required path parameter: organization"})
    # Build request body
    request_body = {}
    if description is not None:
        request_body["description"] = description
    if enabled is not None:
        request_body["enabled"] = enabled
    if evergreen is not None:
        request_body["evergreen"] = evergreen
    if evergreen_last_reminder_at is not None:
        request_body["evergreen_last_reminder_at"] = evergreen_last_reminder_at
    if evergreen_owner is not None:
        request_body["evergreen_owner"] = evergreen_owner
    if evergreen_reminder_interval is not None:
        request_body["evergreen_reminder_interval"] = evergreen_reminder_interval
    if filters is not None:
        request_body["filters"] = filters
    request_body["name"] = name
    request_body["target"] = target
    request_body["type"] = type
    
    # Build URL
    url = f"{config['base_url']}/{organization}/notifications/{notification_id}"
    
    # Build headers
    headers = {
        "Accept": "application/json",
        "X-Request-Source": "Codeglide-MCP-generator",
    }
    headers["Content-Type"] = "application/json"
    # No specific authentication - add fallback
    if config.get("bearer_token"):
        headers["Authorization"] = f"Bearer {config['bearer_token']}"
    elif config.get("api_key"):
        headers["Authorization"] = f"Bearer {config['api_key']}"
    elif config.get("basic_auth"):
        headers["Authorization"] = f"Basic {config['basic_auth']}"
    
    # Add custom headers
    
    try:
        # Make API request
        response = requests.request(
            method="PUT",
            url=url,
            headers=headers,
            json=request_body,
            timeout=30
        )
        
        if response.status_code >= 400:
            return json.dumps({
                "error": f"API error ({response.status_code})",
                "message": response.text
            })
        
        # Parse response
        try:
            result = response.json()
            return json.dumps(result, indent=2)
        except json.JSONDecodeError:
            return response.text
            
    except requests.RequestException as e:
        logger.error(f"Request failed: {e}")
        return json.dumps({"error": f"Request failed: {str(e)}"})
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        return json.dumps({"error": f"Error: {str(e)}"})
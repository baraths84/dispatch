"""CreateServiceOrganizationServicesPost tool implementation."""
import json
import logging
from typing import Any
import requests
from server import mcp

logger = logging.getLogger(__name__)


@mcp.tool()
def createserviceorganizationservicespost(
    organization: str,
    project: dict,
    description: str = None,
    evergreen: bool = None,
    evergreen_last_reminder_at: str = None,
    evergreen_owner: str = None,
    evergreen_reminder_interval: int = None,
    external_id: str = None,
    filters: list = None,
    is_active: bool = None,
    name: str = None,
    type: str = None
) -> str:
    """
    Create Service
    
    Args:
        organization: 
        description: 
        evergreen: 
        evergreen_last_reminder_at: 
        evergreen_owner: 
        evergreen_reminder_interval: 
        external_id: 
        filters: 
        is_active: 
        name: 
        project: 
        type: 
        
    Returns:
        JSON string result
    """
    from config import load_api_config
    config = load_api_config()
    # Validate required path parameters
    if not organization:
        return json.dumps({"error": "Missing required path parameter: organization"})
    # Build request body
    request_body = {}
    if description is not None:
        request_body["description"] = description
    if evergreen is not None:
        request_body["evergreen"] = evergreen
    if evergreen_last_reminder_at is not None:
        request_body["evergreen_last_reminder_at"] = evergreen_last_reminder_at
    if evergreen_owner is not None:
        request_body["evergreen_owner"] = evergreen_owner
    if evergreen_reminder_interval is not None:
        request_body["evergreen_reminder_interval"] = evergreen_reminder_interval
    if external_id is not None:
        request_body["external_id"] = external_id
    if filters is not None:
        request_body["filters"] = filters
    if is_active is not None:
        request_body["is_active"] = is_active
    if name is not None:
        request_body["name"] = name
    request_body["project"] = project
    if type is not None:
        request_body["type"] = type
    
    # Build URL
    url = f"{config['base_url']}/{organization}/services"
    
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
            method="POST",
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
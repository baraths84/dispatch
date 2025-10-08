"""UpdateTeamOrganizationTeamsTeamContactIdPut tool implementation."""
import json
import logging
from typing import Any
import requests
from server import mcp

logger = logging.getLogger(__name__)


@mcp.tool()
def updateteamorganizationteamsteamcontactidput(
    team_contact_id: int,
    organization: str,
    email: str,
    name: str,
    company: str = None,
    contact_type: str = None,
    evergreen: bool = None,
    evergreen_last_reminder_at: str = None,
    evergreen_owner: str = None,
    evergreen_reminder_interval: int = None,
    filters: list = None,
    is_active: bool = None,
    is_external: bool = None,
    notes: str = None,
    owner: str = None
) -> str:
    """
    Update Team
    
    Args:
        team_contact_id: 
        organization: 
        company: 
        contact_type: 
        email: 
        evergreen: 
        evergreen_last_reminder_at: 
        evergreen_owner: 
        evergreen_reminder_interval: 
        filters: 
        is_active: 
        is_external: 
        name: 
        notes: 
        owner: 
        
    Returns:
        JSON string result
    """
    from config import load_api_config
    config = load_api_config()
    # Validate required path parameters
    if not team_contact_id:
        return json.dumps({"error": "Missing required path parameter: team_contact_id"})
    if not organization:
        return json.dumps({"error": "Missing required path parameter: organization"})
    # Build request body
    request_body = {}
    if company is not None:
        request_body["company"] = company
    if contact_type is not None:
        request_body["contact_type"] = contact_type
    request_body["email"] = email
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
    if is_active is not None:
        request_body["is_active"] = is_active
    if is_external is not None:
        request_body["is_external"] = is_external
    request_body["name"] = name
    if notes is not None:
        request_body["notes"] = notes
    if owner is not None:
        request_body["owner"] = owner
    
    # Build URL
    url = f"{config['base_url']}/{organization}/teams/{team_contact_id}"
    
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
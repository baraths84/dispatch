"""UpdateIncidentPriorityOrganizationIncidentPrioritiesIncidentPriorityIdPut tool implementation."""
import json
import logging
from typing import Any
import requests
from server import mcp

logger = logging.getLogger(__name__)


@mcp.tool()
def updateincidentpriorityorganizationincidentprioritiesincidentpriorityidput(
    incident_priority_id: int,
    organization: str,
    name: str,
    color: str = None,
    default: bool = None,
    description: str = None,
    enabled: bool = None,
    executive_report_reminder: int = None,
    page_commander: bool = None,
    project: dict = None,
    tactical_report_reminder: int = None,
    view_order: int = None
) -> str:
    """
    Update Incident Priority
    
    Args:
        incident_priority_id: 
        organization: 
        color: 
        default: 
        description: 
        enabled: 
        executive_report_reminder: 
        name: 
        page_commander: 
        project: 
        tactical_report_reminder: 
        view_order: 
        
    Returns:
        JSON string result
    """
    from config import load_api_config
    config = load_api_config()
    # Validate required path parameters
    if not incident_priority_id:
        return json.dumps({"error": "Missing required path parameter: incident_priority_id"})
    if not organization:
        return json.dumps({"error": "Missing required path parameter: organization"})
    # Build request body
    request_body = {}
    if color is not None:
        request_body["color"] = color
    if default is not None:
        request_body["default"] = default
    if description is not None:
        request_body["description"] = description
    if enabled is not None:
        request_body["enabled"] = enabled
    if executive_report_reminder is not None:
        request_body["executive_report_reminder"] = executive_report_reminder
    request_body["name"] = name
    if page_commander is not None:
        request_body["page_commander"] = page_commander
    if project is not None:
        request_body["project"] = project
    if tactical_report_reminder is not None:
        request_body["tactical_report_reminder"] = tactical_report_reminder
    if view_order is not None:
        request_body["view_order"] = view_order
    
    # Build URL
    url = f"{config['base_url']}/{organization}/incident_priorities/{incident_priority_id}"
    
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
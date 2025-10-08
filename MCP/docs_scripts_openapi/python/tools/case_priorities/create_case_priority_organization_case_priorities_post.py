"""CreateCasePriorityOrganizationCasePrioritiesPost tool implementation."""
import json
import logging
from typing import Any
import requests
from server import mcp

logger = logging.getLogger(__name__)


@mcp.tool()
def createcasepriorityorganizationcaseprioritiespost(
    organization: str,
    name: str,
    color: str = None,
    default: bool = None,
    description: str = None,
    enabled: bool = None,
    page_assignee: bool = None,
    project: dict = None,
    view_order: int = None
) -> str:
    """
    Create Case Priority
    
    Args:
        organization: 
        color: 
        default: 
        description: 
        enabled: 
        name: 
        page_assignee: 
        project: 
        view_order: 
        
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
    if color is not None:
        request_body["color"] = color
    if default is not None:
        request_body["default"] = default
    if description is not None:
        request_body["description"] = description
    if enabled is not None:
        request_body["enabled"] = enabled
    request_body["name"] = name
    if page_assignee is not None:
        request_body["page_assignee"] = page_assignee
    if project is not None:
        request_body["project"] = project
    if view_order is not None:
        request_body["view_order"] = view_order
    
    # Build URL
    url = f"{config['base_url']}/{organization}/case_priorities"
    
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
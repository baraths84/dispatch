"""UpdateIncidentRoleOrganizationIncidentRolesRolePut tool implementation."""
import json
import logging
from typing import Any
import requests
from server import mcp

logger = logging.getLogger(__name__)


@mcp.tool()
def updateincidentroleorganizationincidentrolesroleput(
    role: str,
    organization: str,
    projectName: str,
    policies: list
) -> str:
    """
    Update Incident Role
    
    Args:
        role: 
        organization: 
        projectName: 
        policies: 
        
    Returns:
        JSON string result
    """
    from config import load_api_config
    config = load_api_config()
    # Validate required path parameters
    if not role:
        return json.dumps({"error": "Missing required path parameter: role"})
    if not organization:
        return json.dumps({"error": "Missing required path parameter: organization"})
    # Build query parameters
    query_params = {}
    if projectName is not None:
        query_params["projectName"] = projectName
    # Build request body
    request_body = {}
    request_body["policies"] = policies
    
    # Build URL
    url = f"{config['base_url']}/{organization}/incident_roles/{role}"
    
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
            params=query_params,
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
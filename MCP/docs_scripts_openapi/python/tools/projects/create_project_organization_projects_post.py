"""CreateProjectOrganizationProjectsPost tool implementation."""
import json
import logging
from typing import Any
import requests
from server import mcp

logger = logging.getLogger(__name__)


@mcp.tool()
def createprojectorganizationprojectspost(
    organization: str,
    name: str,
    organization_body: dict,
    annual_employee_cost: int = None,
    business_year_hours: int = None,
    color: str = None,
    default: bool = None,
    description: str = None,
    id: int = None,
    owner_conversation: str = None,
    owner_email: str = None
) -> str:
    """
    Create a new project.
    
    Args:
        organization: 
        annual_employee_cost: 
        business_year_hours: 
        color: 
        default: 
        description: 
        id: 
        name: 
        organization_body: [Body param: organization] 
        owner_conversation: 
        owner_email: 
        
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
    if annual_employee_cost is not None:
        request_body["annual_employee_cost"] = annual_employee_cost
    if business_year_hours is not None:
        request_body["business_year_hours"] = business_year_hours
    if color is not None:
        request_body["color"] = color
    if default is not None:
        request_body["default"] = default
    if description is not None:
        request_body["description"] = description
    if id is not None:
        request_body["id"] = id
    request_body["name"] = name
    request_body["organization"] = organization_body
    if owner_conversation is not None:
        request_body["owner_conversation"] = owner_conversation
    if owner_email is not None:
        request_body["owner_email"] = owner_email
    
    # Build URL
    url = f"{config['base_url']}/{organization}/projects"
    
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
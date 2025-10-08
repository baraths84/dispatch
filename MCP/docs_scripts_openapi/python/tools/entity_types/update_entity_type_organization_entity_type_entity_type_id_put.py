"""UpdateEntityTypeOrganizationEntityTypeEntityTypeIdPut tool implementation."""
import json
import logging
from typing import Any
import requests
from server import mcp

logger = logging.getLogger(__name__)


@mcp.tool()
def updateentitytypeorganizationentitytypeentitytypeidput(
    entity_type_id: int,
    organization: str,
    description: str = None,
    enabled: bool = None,
    global_find: bool = None,
    id: int = None,
    jpath: str = None,
    name: str = None,
    regular_expression: str = None
) -> str:
    """
    Update Entity Type
    
    Args:
        entity_type_id: 
        organization: 
        description: 
        enabled: 
        global_find: 
        id: 
        jpath: 
        name: 
        regular_expression: 
        
    Returns:
        JSON string result
    """
    from config import load_api_config
    config = load_api_config()
    # Validate required path parameters
    if not entity_type_id:
        return json.dumps({"error": "Missing required path parameter: entity_type_id"})
    if not organization:
        return json.dumps({"error": "Missing required path parameter: organization"})
    # Build request body
    request_body = {}
    if description is not None:
        request_body["description"] = description
    if enabled is not None:
        request_body["enabled"] = enabled
    if global_find is not None:
        request_body["global_find"] = global_find
    if id is not None:
        request_body["id"] = id
    if jpath is not None:
        request_body["jpath"] = jpath
    if name is not None:
        request_body["name"] = name
    if regular_expression is not None:
        request_body["regular_expression"] = regular_expression
    
    # Build URL
    url = f"{config['base_url']}/{organization}/entity_type/{entity_type_id}"
    
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
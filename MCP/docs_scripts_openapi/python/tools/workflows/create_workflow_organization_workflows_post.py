"""CreateWorkflowOrganizationWorkflowsPost tool implementation."""
import json
import logging
from typing import Any
import requests
from server import mcp

logger = logging.getLogger(__name__)


@mcp.tool()
def createworkfloworganizationworkflowspost(
    organization: str,
    name: str,
    plugin_instance: dict,
    project: dict,
    resource_id: str,
    created_at: str = None,
    description: str = None,
    enabled: bool = None,
    parameters: list = None,
    updated_at: str = None
) -> str:
    """
    Create Workflow
    
    Args:
        organization: 
        created_at: 
        description: 
        enabled: 
        name: 
        parameters: 
        plugin_instance: 
        project: 
        resource_id: 
        updated_at: 
        
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
    if created_at is not None:
        request_body["created_at"] = created_at
    if description is not None:
        request_body["description"] = description
    if enabled is not None:
        request_body["enabled"] = enabled
    request_body["name"] = name
    if parameters is not None:
        request_body["parameters"] = parameters
    request_body["plugin_instance"] = plugin_instance
    request_body["project"] = project
    request_body["resource_id"] = resource_id
    if updated_at is not None:
        request_body["updated_at"] = updated_at
    
    # Build URL
    url = f"{config['base_url']}/{organization}/workflows"
    
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
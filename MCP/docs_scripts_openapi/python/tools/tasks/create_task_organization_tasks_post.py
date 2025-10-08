"""CreateTaskOrganizationTasksPost tool implementation."""
import json
import logging
from typing import Any
import requests
from server import mcp

logger = logging.getLogger(__name__)


@mcp.tool()
def createtaskorganizationtaskspost(
    organization: str,
    incident: dict,
    assignees: list = None,
    created_at: str = None,
    creator: dict = None,
    description: str = None,
    owner: dict = None,
    priority: str = None,
    resolve_by: str = None,
    resolved_at: str = None,
    resource_id: str = None,
    resource_type: str = None,
    source: str = None,
    status: str = None,
    updated_at: str = None,
    weblink: str = None
) -> str:
    """
    Create Task
    
    Args:
        organization: 
        assignees: 
        created_at: 
        creator: 
        description: 
        incident: 
        owner: 
        priority: 
        resolve_by: 
        resolved_at: 
        resource_id: 
        resource_type: 
        source: 
        status: 
        updated_at: 
        weblink: 
        
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
    if assignees is not None:
        request_body["assignees"] = assignees
    if created_at is not None:
        request_body["created_at"] = created_at
    if creator is not None:
        request_body["creator"] = creator
    if description is not None:
        request_body["description"] = description
    request_body["incident"] = incident
    if owner is not None:
        request_body["owner"] = owner
    if priority is not None:
        request_body["priority"] = priority
    if resolve_by is not None:
        request_body["resolve_by"] = resolve_by
    if resolved_at is not None:
        request_body["resolved_at"] = resolved_at
    if resource_id is not None:
        request_body["resource_id"] = resource_id
    if resource_type is not None:
        request_body["resource_type"] = resource_type
    if source is not None:
        request_body["source"] = source
    if status is not None:
        request_body["status"] = status
    if updated_at is not None:
        request_body["updated_at"] = updated_at
    if weblink is not None:
        request_body["weblink"] = weblink
    
    # Build URL
    url = f"{config['base_url']}/{organization}/tasks"
    
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
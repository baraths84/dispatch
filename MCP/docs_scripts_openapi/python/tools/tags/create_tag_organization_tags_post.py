"""CreateTagOrganizationTagsPost tool implementation."""
import json
import logging
from typing import Any
import requests
from server import mcp

logger = logging.getLogger(__name__)


@mcp.tool()
def createtagorganizationtagspost(
    organization: str,
    project: dict,
    tag_type: dict,
    description: str = None,
    discoverable: bool = None,
    external_id: str = None,
    id: int = None,
    name: str = None,
    source: str = None,
    uri: str = None
) -> str:
    """
    Create Tag
    
    Args:
        organization: 
        description: 
        discoverable: 
        external_id: 
        id: 
        name: 
        project: 
        source: 
        tag_type: 
        uri: 
        
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
    if discoverable is not None:
        request_body["discoverable"] = discoverable
    if external_id is not None:
        request_body["external_id"] = external_id
    if id is not None:
        request_body["id"] = id
    if name is not None:
        request_body["name"] = name
    request_body["project"] = project
    if source is not None:
        request_body["source"] = source
    request_body["tag_type"] = tag_type
    if uri is not None:
        request_body["uri"] = uri
    
    # Build URL
    url = f"{config['base_url']}/{organization}/tags"
    
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
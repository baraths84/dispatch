"""UpdateQueryOrganizationDataQueriesQueryIdPut tool implementation."""
import json
import logging
from typing import Any
import requests
from server import mcp

logger = logging.getLogger(__name__)


@mcp.tool()
def updatequeryorganizationdataqueriesqueryidput(
    query_id: int,
    organization: str,
    project: dict,
    source: dict,
    description: str = None,
    id: int = None,
    language: str = None,
    name: str = None,
    tags: list = None,
    text: str = None
) -> str:
    """
    Update Query
    
    Args:
        query_id: 
        organization: 
        description: 
        id: 
        language: 
        name: 
        project: 
        source: 
        tags: 
        text: 
        
    Returns:
        JSON string result
    """
    from config import load_api_config
    config = load_api_config()
    # Validate required path parameters
    if not query_id:
        return json.dumps({"error": "Missing required path parameter: query_id"})
    if not organization:
        return json.dumps({"error": "Missing required path parameter: organization"})
    # Build request body
    request_body = {}
    if description is not None:
        request_body["description"] = description
    if id is not None:
        request_body["id"] = id
    if language is not None:
        request_body["language"] = language
    if name is not None:
        request_body["name"] = name
    request_body["project"] = project
    request_body["source"] = source
    if tags is not None:
        request_body["tags"] = tags
    if text is not None:
        request_body["text"] = text
    
    # Build URL
    url = f"{config['base_url']}/{organization}/data/queries/{query_id}"
    
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
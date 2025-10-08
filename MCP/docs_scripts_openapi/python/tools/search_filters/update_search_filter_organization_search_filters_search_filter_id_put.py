"""UpdateSearchFilterOrganizationSearchFiltersSearchFilterIdPut tool implementation."""
import json
import logging
from typing import Any
import requests
from server import mcp

logger = logging.getLogger(__name__)


@mcp.tool()
def updatesearchfilterorganizationsearchfilterssearchfilteridput(
    search_filter_id: int,
    organization: str,
    expression: list,
    name: str,
    description: str = None,
    id: int = None,
    subject: str = None
) -> str:
    """
    Update Search Filter
    
    Args:
        search_filter_id: 
        organization: 
        description: 
        expression: 
        id: 
        name: 
        subject: 
        
    Returns:
        JSON string result
    """
    from config import load_api_config
    config = load_api_config()
    # Validate required path parameters
    if not search_filter_id:
        return json.dumps({"error": "Missing required path parameter: search_filter_id"})
    if not organization:
        return json.dumps({"error": "Missing required path parameter: organization"})
    # Build request body
    request_body = {}
    if description is not None:
        request_body["description"] = description
    request_body["expression"] = expression
    if id is not None:
        request_body["id"] = id
    request_body["name"] = name
    if subject is not None:
        request_body["subject"] = subject
    
    # Build URL
    url = f"{config['base_url']}/{organization}/search/filters/{search_filter_id}"
    
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
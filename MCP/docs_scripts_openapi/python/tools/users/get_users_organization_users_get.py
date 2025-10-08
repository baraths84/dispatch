"""GetUsersOrganizationUsersGet tool implementation."""
import json
import logging
from typing import Any
import requests
from server import mcp

logger = logging.getLogger(__name__)


@mcp.tool()
def getusersorganizationusersget(
    organization: str,
    page: int = None,
    itemsPerPage: int = None,
    q: str = None,
    filter: str = None,
    sortBy: list = None,
    descending: list = None
) -> str:
    """
    Get Users
    
    Args:
        organization: 
        page: 
        itemsPerPage: 
        q: 
        filter: 
        sortBy: 
        descending: 
        
    Returns:
        JSON string result
    """
    from config import load_api_config
    config = load_api_config()
    # Validate required path parameters
    if not organization:
        return json.dumps({"error": "Missing required path parameter: organization"})
    # Build query parameters
    query_params = {}
    if page is not None:
        query_params["page"] = page
    if itemsPerPage is not None:
        query_params["itemsPerPage"] = itemsPerPage
    if q is not None:
        query_params["q"] = q
    if filter is not None:
        query_params["filter"] = filter
    if sortBy is not None:
        query_params["sortBy[]"] = sortBy
    if descending is not None:
        query_params["descending[]"] = descending
    
    # Build URL
    url = f"{config['base_url']}/{organization}/users"
    
    # Build headers
    headers = {
        "Accept": "application/json",
        "X-Request-Source": "Codeglide-MCP-generator",
    }
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
            method="GET",
            url=url,
            params=query_params,
            headers=headers,
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
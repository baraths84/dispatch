"""UpdateTermOrganizationTermsTermIdPut tool implementation."""
import json
import logging
from typing import Any
import requests
from server import mcp

logger = logging.getLogger(__name__)


@mcp.tool()
def updatetermorganizationtermstermidput(
    term_id: int,
    organization: str,
    definitions: list = None,
    discoverable: bool = None,
    id: int = None,
    text: str = None
) -> str:
    """
    Update Term
    
    Args:
        term_id: 
        organization: 
        definitions: 
        discoverable: 
        id: 
        text: 
        
    Returns:
        JSON string result
    """
    from config import load_api_config
    config = load_api_config()
    # Validate required path parameters
    if not term_id:
        return json.dumps({"error": "Missing required path parameter: term_id"})
    if not organization:
        return json.dumps({"error": "Missing required path parameter: organization"})
    # Build request body
    request_body = {}
    if definitions is not None:
        request_body["definitions"] = definitions
    if discoverable is not None:
        request_body["discoverable"] = discoverable
    if id is not None:
        request_body["id"] = id
    if text is not None:
        request_body["text"] = text
    
    # Build URL
    url = f"{config['base_url']}/{organization}/terms/{term_id}"
    
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
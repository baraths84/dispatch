"""CreateCaseOrganizationCasesPost tool implementation."""
import json
import logging
from typing import Any
import requests
from server import mcp

logger = logging.getLogger(__name__)


@mcp.tool()
def createcaseorganizationcasespost(
    organization: str,
    title: str,
    assignee: dict = None,
    case_priority: dict = None,
    case_severity: dict = None,
    case_type: dict = None,
    description: str = None,
    project: dict = None,
    reporter: dict = None,
    resolution: str = None,
    resolution_reason: str = None,
    status: str = None,
    tags: list = None,
    visibility: str = None
) -> str:
    """
    Creates a new case.
    
    Args:
        organization: 
        assignee: 
        case_priority: 
        case_severity: 
        case_type: 
        description: 
        project: 
        reporter: 
        resolution: 
        resolution_reason: Input parameter: An enumeration.
        status: Input parameter: An enumeration.
        tags: 
        title: 
        visibility: Input parameter: An enumeration.
        
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
    if assignee is not None:
        request_body["assignee"] = assignee
    if case_priority is not None:
        request_body["case_priority"] = case_priority
    if case_severity is not None:
        request_body["case_severity"] = case_severity
    if case_type is not None:
        request_body["case_type"] = case_type
    if description is not None:
        request_body["description"] = description
    if project is not None:
        request_body["project"] = project
    if reporter is not None:
        request_body["reporter"] = reporter
    if resolution is not None:
        request_body["resolution"] = resolution
    if resolution_reason is not None:
        request_body["resolution_reason"] = resolution_reason
    if status is not None:
        request_body["status"] = status
    if tags is not None:
        request_body["tags"] = tags
    request_body["title"] = title
    if visibility is not None:
        request_body["visibility"] = visibility
    
    # Build URL
    url = f"{config['base_url']}/{organization}/cases"
    
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
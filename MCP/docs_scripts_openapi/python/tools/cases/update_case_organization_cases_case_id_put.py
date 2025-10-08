"""UpdateCaseOrganizationCasesCaseIdPut tool implementation."""
import json
import logging
from typing import Any
import requests
from server import mcp

logger = logging.getLogger(__name__)


@mcp.tool()
def updatecaseorganizationcasescaseidput(
    organization: str,
    case_id: int,
    title: str,
    assignee: dict = None,
    case_priority: dict = None,
    case_severity: dict = None,
    case_type: dict = None,
    description: str = None,
    duplicates: list = None,
    escalated_at: str = None,
    incidents: list = None,
    related: list = None,
    reported_at: str = None,
    resolution: str = None,
    resolution_reason: str = None,
    status: str = None,
    tags: list = None,
    triage_at: str = None,
    visibility: str = None
) -> str:
    """
    Updates an existing case.
    
    Args:
        organization: 
        case_id: 
        assignee: 
        case_priority: 
        case_severity: 
        case_type: 
        description: 
        duplicates: 
        escalated_at: 
        incidents: 
        related: 
        reported_at: 
        resolution: 
        resolution_reason: Input parameter: An enumeration.
        status: Input parameter: An enumeration.
        tags: 
        title: 
        triage_at: 
        visibility: Input parameter: An enumeration.
        
    Returns:
        JSON string result
    """
    from config import load_api_config
    config = load_api_config()
    # Validate required path parameters
    if not organization:
        return json.dumps({"error": "Missing required path parameter: organization"})
    if not case_id:
        return json.dumps({"error": "Missing required path parameter: case_id"})
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
    if duplicates is not None:
        request_body["duplicates"] = duplicates
    if escalated_at is not None:
        request_body["escalated_at"] = escalated_at
    if incidents is not None:
        request_body["incidents"] = incidents
    if related is not None:
        request_body["related"] = related
    if reported_at is not None:
        request_body["reported_at"] = reported_at
    if resolution is not None:
        request_body["resolution"] = resolution
    if resolution_reason is not None:
        request_body["resolution_reason"] = resolution_reason
    if status is not None:
        request_body["status"] = status
    if tags is not None:
        request_body["tags"] = tags
    request_body["title"] = title
    if triage_at is not None:
        request_body["triage_at"] = triage_at
    if visibility is not None:
        request_body["visibility"] = visibility
    
    # Build URL
    url = f"{config['base_url']}/{organization}/cases/{case_id}"
    
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
"""EscalateCaseOrganizationCasesCaseIdEscalatePut tool implementation."""
import json
import logging
from typing import Any
import requests
from server import mcp

logger = logging.getLogger(__name__)


@mcp.tool()
def escalatecaseorganizationcasescaseidescalateput(
    organization: str,
    description: str,
    title: str,
    commander: dict = None,
    incident_priority: dict = None,
    incident_severity: dict = None,
    incident_type: dict = None,
    project: dict = None,
    reporter: dict = None,
    resolution: str = None,
    status: str = None,
    tags: list = None,
    visibility: str = None
) -> str:
    """
    Escalates an existing case.
    
    Args:
        organization: 
        commander: 
        description: 
        incident_priority: 
        incident_severity: 
        incident_type: 
        project: 
        reporter: 
        resolution: 
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
    if commander is not None:
        request_body["commander"] = commander
    request_body["description"] = description
    if incident_priority is not None:
        request_body["incident_priority"] = incident_priority
    if incident_severity is not None:
        request_body["incident_severity"] = incident_severity
    if incident_type is not None:
        request_body["incident_type"] = incident_type
    if project is not None:
        request_body["project"] = project
    if reporter is not None:
        request_body["reporter"] = reporter
    if resolution is not None:
        request_body["resolution"] = resolution
    if status is not None:
        request_body["status"] = status
    if tags is not None:
        request_body["tags"] = tags
    request_body["title"] = title
    if visibility is not None:
        request_body["visibility"] = visibility
    
    # Build URL
    url = f"{config['base_url']}/{organization}/cases/{case_id}/escalate"
    
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
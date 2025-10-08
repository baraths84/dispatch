"""UpdateIncidentOrganizationIncidentsIncidentIdPut tool implementation."""
import json
import logging
from typing import Any
import requests
from server import mcp

logger = logging.getLogger(__name__)


@mcp.tool()
def updateincidentorganizationincidentsincidentidput(
    organization: str,
    incident_id: int,
    description: str,
    incident_priority: dict,
    incident_severity: dict,
    incident_type: dict,
    title: str,
    cases: list = None,
    commander: dict = None,
    duplicates: list = None,
    incident_costs: list = None,
    reported_at: str = None,
    reporter: dict = None,
    resolution: str = None,
    stable_at: str = None,
    status: str = None,
    tags: list = None,
    terms: list = None,
    visibility: str = None
) -> str:
    """
    Updates an existing incident.
    
    Args:
        organization: 
        incident_id: 
        cases: 
        commander: 
        description: 
        duplicates: 
        incident_costs: 
        incident_priority: 
        incident_severity: 
        incident_type: 
        reported_at: 
        reporter: 
        resolution: 
        stable_at: 
        status: Input parameter: An enumeration.
        tags: 
        terms: 
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
    if not incident_id:
        return json.dumps({"error": "Missing required path parameter: incident_id"})
    # Build request body
    request_body = {}
    if cases is not None:
        request_body["cases"] = cases
    if commander is not None:
        request_body["commander"] = commander
    request_body["description"] = description
    if duplicates is not None:
        request_body["duplicates"] = duplicates
    if incident_costs is not None:
        request_body["incident_costs"] = incident_costs
    request_body["incident_priority"] = incident_priority
    request_body["incident_severity"] = incident_severity
    request_body["incident_type"] = incident_type
    if reported_at is not None:
        request_body["reported_at"] = reported_at
    if reporter is not None:
        request_body["reporter"] = reporter
    if resolution is not None:
        request_body["resolution"] = resolution
    if stable_at is not None:
        request_body["stable_at"] = stable_at
    if status is not None:
        request_body["status"] = status
    if tags is not None:
        request_body["tags"] = tags
    if terms is not None:
        request_body["terms"] = terms
    request_body["title"] = title
    if visibility is not None:
        request_body["visibility"] = visibility
    
    # Build URL
    url = f"{config['base_url']}/{organization}/incidents/{incident_id}"
    
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
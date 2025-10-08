"""CreateExecutiveReportOrganizationIncidentsIncidentIdReportExecutivePost tool implementation."""
import json
import logging
from typing import Any
import requests
from server import mcp

logger = logging.getLogger(__name__)


@mcp.tool()
def createexecutivereportorganizationincidentsincidentidreportexecutivepost(
    organization: str,
    incident_id: int,
    current_status: str,
    next_steps: str,
    overview: str
) -> str:
    """
    Creates an executive report.
    
    Args:
        organization: 
        incident_id: 
        current_status: 
        next_steps: 
        overview: 
        
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
    request_body["current_status"] = current_status
    request_body["next_steps"] = next_steps
    request_body["overview"] = overview
    
    # Build URL
    url = f"{config['base_url']}/{organization}/incidents/{incident_id}/report/executive"
    
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
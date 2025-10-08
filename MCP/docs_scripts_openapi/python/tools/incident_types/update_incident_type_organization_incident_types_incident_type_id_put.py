"""UpdateIncidentTypeOrganizationIncidentTypesIncidentTypeIdPut tool implementation."""
import json
import logging
from typing import Any
import requests
from server import mcp

logger = logging.getLogger(__name__)


@mcp.tool()
def updateincidenttypeorganizationincidenttypesincidenttypeidput(
    incident_type_id: int,
    organization: str,
    name: str,
    default: bool = None,
    description: str = None,
    enabled: bool = None,
    exclude_from_metrics: bool = None,
    executive_template_document: dict = None,
    id: int = None,
    incident_template_document: dict = None,
    plugin_metadata: list = None,
    project: dict = None,
    review_template_document: dict = None,
    tracking_template_document: dict = None,
    visibility: str = None
) -> str:
    """
    Update Incident Type
    
    Args:
        incident_type_id: 
        organization: 
        default: 
        description: 
        enabled: 
        exclude_from_metrics: 
        executive_template_document: 
        id: 
        incident_template_document: 
        name: 
        plugin_metadata: 
        project: 
        review_template_document: 
        tracking_template_document: 
        visibility: 
        
    Returns:
        JSON string result
    """
    from config import load_api_config
    config = load_api_config()
    # Validate required path parameters
    if not incident_type_id:
        return json.dumps({"error": "Missing required path parameter: incident_type_id"})
    if not organization:
        return json.dumps({"error": "Missing required path parameter: organization"})
    # Build request body
    request_body = {}
    if default is not None:
        request_body["default"] = default
    if description is not None:
        request_body["description"] = description
    if enabled is not None:
        request_body["enabled"] = enabled
    if exclude_from_metrics is not None:
        request_body["exclude_from_metrics"] = exclude_from_metrics
    if executive_template_document is not None:
        request_body["executive_template_document"] = executive_template_document
    if id is not None:
        request_body["id"] = id
    if incident_template_document is not None:
        request_body["incident_template_document"] = incident_template_document
    request_body["name"] = name
    if plugin_metadata is not None:
        request_body["plugin_metadata"] = plugin_metadata
    if project is not None:
        request_body["project"] = project
    if review_template_document is not None:
        request_body["review_template_document"] = review_template_document
    if tracking_template_document is not None:
        request_body["tracking_template_document"] = tracking_template_document
    if visibility is not None:
        request_body["visibility"] = visibility
    
    # Build URL
    url = f"{config['base_url']}/{organization}/incident_types/{incident_type_id}"
    
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
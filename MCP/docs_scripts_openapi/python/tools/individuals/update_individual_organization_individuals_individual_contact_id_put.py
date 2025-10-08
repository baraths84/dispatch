"""UpdateIndividualOrganizationIndividualsIndividualContactIdPut tool implementation."""
import json
import logging
from typing import Any
import requests
from server import mcp

logger = logging.getLogger(__name__)


@mcp.tool()
def updateindividualorganizationindividualsindividualcontactidput(
    individual_contact_id: int,
    organization: str,
    email: str,
    company: str = None,
    contact_type: str = None,
    external_id: str = None,
    filters: list = None,
    is_active: bool = None,
    is_external: bool = None,
    mobile_phone: str = None,
    name: str = None,
    notes: str = None,
    office_phone: str = None,
    owner: str = None,
    title: str = None,
    weblink: str = None
) -> str:
    """
    Updates an individual's contact information.
    
    Args:
        individual_contact_id: 
        organization: 
        company: 
        contact_type: 
        email: 
        external_id: 
        filters: 
        is_active: 
        is_external: 
        mobile_phone: 
        name: 
        notes: 
        office_phone: 
        owner: 
        title: 
        weblink: 
        
    Returns:
        JSON string result
    """
    from config import load_api_config
    config = load_api_config()
    # Validate required path parameters
    if not individual_contact_id:
        return json.dumps({"error": "Missing required path parameter: individual_contact_id"})
    if not organization:
        return json.dumps({"error": "Missing required path parameter: organization"})
    # Build request body
    request_body = {}
    if company is not None:
        request_body["company"] = company
    if contact_type is not None:
        request_body["contact_type"] = contact_type
    request_body["email"] = email
    if external_id is not None:
        request_body["external_id"] = external_id
    if filters is not None:
        request_body["filters"] = filters
    if is_active is not None:
        request_body["is_active"] = is_active
    if is_external is not None:
        request_body["is_external"] = is_external
    if mobile_phone is not None:
        request_body["mobile_phone"] = mobile_phone
    if name is not None:
        request_body["name"] = name
    if notes is not None:
        request_body["notes"] = notes
    if office_phone is not None:
        request_body["office_phone"] = office_phone
    if owner is not None:
        request_body["owner"] = owner
    if title is not None:
        request_body["title"] = title
    if weblink is not None:
        request_body["weblink"] = weblink
    
    # Build URL
    url = f"{config['base_url']}/{organization}/individuals/{individual_contact_id}"
    
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
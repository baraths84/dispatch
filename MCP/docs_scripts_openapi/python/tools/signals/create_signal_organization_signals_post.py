"""CreateSignalOrganizationSignalsPost tool implementation."""
import json
import logging
from typing import Any
import requests
from server import mcp

logger = logging.getLogger(__name__)


@mcp.tool()
def createsignalorganizationsignalspost(
    organization: str,
    external_id: str,
    name: str,
    owner: str,
    project: dict,
    case_priority: dict = None,
    case_type: dict = None,
    conversation_target: str = None,
    create_case: bool = None,
    created_at: str = None,
    description: str = None,
    enabled: bool = None,
    entity_types: list = None,
    external_url: str = None,
    filters: list = None,
    oncall_service: dict = None,
    source: dict = None,
    tags: list = None,
    variant: str = None,
    workflows: list = None
) -> str:
    """
    Create Signal
    
    Args:
        organization: 
        case_priority: 
        case_type: 
        conversation_target: 
        create_case: 
        created_at: 
        description: 
        enabled: 
        entity_types: 
        external_id: 
        external_url: 
        filters: 
        name: 
        oncall_service: 
        owner: 
        project: 
        source: 
        tags: 
        variant: 
        workflows: 
        
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
    if case_priority is not None:
        request_body["case_priority"] = case_priority
    if case_type is not None:
        request_body["case_type"] = case_type
    if conversation_target is not None:
        request_body["conversation_target"] = conversation_target
    if create_case is not None:
        request_body["create_case"] = create_case
    if created_at is not None:
        request_body["created_at"] = created_at
    if description is not None:
        request_body["description"] = description
    if enabled is not None:
        request_body["enabled"] = enabled
    if entity_types is not None:
        request_body["entity_types"] = entity_types
    request_body["external_id"] = external_id
    if external_url is not None:
        request_body["external_url"] = external_url
    if filters is not None:
        request_body["filters"] = filters
    request_body["name"] = name
    if oncall_service is not None:
        request_body["oncall_service"] = oncall_service
    request_body["owner"] = owner
    request_body["project"] = project
    if source is not None:
        request_body["source"] = source
    if tags is not None:
        request_body["tags"] = tags
    if variant is not None:
        request_body["variant"] = variant
    if workflows is not None:
        request_body["workflows"] = workflows
    
    # Build URL
    url = f"{config['base_url']}/{organization}/signals"
    
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
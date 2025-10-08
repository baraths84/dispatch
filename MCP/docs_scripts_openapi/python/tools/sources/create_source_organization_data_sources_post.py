"""CreateSourceOrganizationDataSourcesPost tool implementation."""
import json
import logging
from typing import Any
import requests
from server import mcp

logger = logging.getLogger(__name__)


@mcp.tool()
def createsourceorganizationdatasourcespost(
    organization: str,
    project: dict,
    aggregated: bool = None,
    alerts: list = None,
    cost: float = None,
    data_last_loaded_at: str = None,
    delay: int = None,
    description: str = None,
    documentation: str = None,
    external_id: str = None,
    incidents: list = None,
    links: list = None,
    name: str = None,
    owner: str = None,
    queries: list = None,
    retention: int = None,
    sampling_rate: int = None,
    size: int = None,
    source_data_format: dict = None,
    source_environment: dict = None,
    source_schema: str = None,
    source_status: dict = None,
    source_transport: dict = None,
    source_type: dict = None,
    tags: list = None
) -> str:
    """
    Create Source
    
    Args:
        organization: 
        aggregated: 
        alerts: 
        cost: 
        data_last_loaded_at: 
        delay: 
        description: 
        documentation: 
        external_id: 
        incidents: 
        links: 
        name: 
        owner: 
        project: 
        queries: 
        retention: 
        sampling_rate: Input parameter: Rate at which data is sampled (as a percentage) 100% meaning all data is captured.
        size: 
        source_data_format: 
        source_environment: 
        source_schema: 
        source_status: 
        source_transport: 
        source_type: 
        tags: 
        
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
    if aggregated is not None:
        request_body["aggregated"] = aggregated
    if alerts is not None:
        request_body["alerts"] = alerts
    if cost is not None:
        request_body["cost"] = cost
    if data_last_loaded_at is not None:
        request_body["data_last_loaded_at"] = data_last_loaded_at
    if delay is not None:
        request_body["delay"] = delay
    if description is not None:
        request_body["description"] = description
    if documentation is not None:
        request_body["documentation"] = documentation
    if external_id is not None:
        request_body["external_id"] = external_id
    if incidents is not None:
        request_body["incidents"] = incidents
    if links is not None:
        request_body["links"] = links
    if name is not None:
        request_body["name"] = name
    if owner is not None:
        request_body["owner"] = owner
    request_body["project"] = project
    if queries is not None:
        request_body["queries"] = queries
    if retention is not None:
        request_body["retention"] = retention
    if sampling_rate is not None:
        request_body["sampling_rate"] = sampling_rate
    if size is not None:
        request_body["size"] = size
    if source_data_format is not None:
        request_body["source_data_format"] = source_data_format
    if source_environment is not None:
        request_body["source_environment"] = source_environment
    if source_schema is not None:
        request_body["source_schema"] = source_schema
    if source_status is not None:
        request_body["source_status"] = source_status
    if source_transport is not None:
        request_body["source_transport"] = source_transport
    if source_type is not None:
        request_body["source_type"] = source_type
    if tags is not None:
        request_body["tags"] = tags
    
    # Build URL
    url = f"{config['base_url']}/{organization}/data/sources"
    
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
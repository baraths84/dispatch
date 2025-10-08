"""UpdateFeedbackOrganizationFeedbackFeedbackIdPut tool implementation."""
import json
import logging
from typing import Any
import requests
from server import mcp

logger = logging.getLogger(__name__)


@mcp.tool()
def updatefeedbackorganizationfeedbackfeedbackidput(
    feedback_id: int,
    organization: str,
    created_at: str = None,
    feedback: str = None,
    id: int = None,
    incident: dict = None,
    participant: dict = None,
    rating: str = None
) -> str:
    """
    Update Feedback
    
    Args:
        feedback_id: 
        organization: 
        created_at: 
        feedback: 
        id: 
        incident: 
        participant: 
        rating: 
        
    Returns:
        JSON string result
    """
    from config import load_api_config
    config = load_api_config()
    # Validate required path parameters
    if not feedback_id:
        return json.dumps({"error": "Missing required path parameter: feedback_id"})
    if not organization:
        return json.dumps({"error": "Missing required path parameter: organization"})
    # Build request body
    request_body = {}
    if created_at is not None:
        request_body["created_at"] = created_at
    if feedback is not None:
        request_body["feedback"] = feedback
    if id is not None:
        request_body["id"] = id
    if incident is not None:
        request_body["incident"] = incident
    if participant is not None:
        request_body["participant"] = participant
    if rating is not None:
        request_body["rating"] = rating
    
    # Build URL
    url = f"{config['base_url']}/{organization}/feedback/{feedback_id}"
    
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
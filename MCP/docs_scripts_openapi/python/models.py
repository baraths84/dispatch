"""Data models for dispatch."""
from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field


class AlertCreate(BaseModel):
    """AlertCreate schema from the OpenAPI specification."""
    description: str = Field(alias="description")
    external_link: str = Field(alias="external_link")
    id_field: int = Field(alias="id")
    name: str = Field(alias="name")
    originator: str = Field(alias="originator")
    
    class Config:
        populate_by_name = True


class AlertRead(BaseModel):
    """AlertRead schema from the OpenAPI specification."""
    description: str = Field(alias="description")
    external_link: str = Field(alias="external_link")
    id_field: int = Field(alias="id")
    name: str = Field(alias="name")
    originator: str = Field(alias="originator")
    
    class Config:
        populate_by_name = True


class AlertUpdate(BaseModel):
    """AlertUpdate schema from the OpenAPI specification."""
    description: str = Field(alias="description")
    external_link: str = Field(alias="external_link")
    id_field: int = Field(alias="id")
    name: str = Field(alias="name")
    originator: str = Field(alias="originator")
    
    class Config:
        populate_by_name = True


class CaseCreate(BaseModel):
    """CaseCreate schema from the OpenAPI specification."""
    assignee: ParticipantUpdate = Field(alias="assignee")
    case_priority: CasePriorityRead = Field(alias="case_priority")
    case_severity: CaseSeverityRead = Field(alias="case_severity")
    case_type: CaseTypeRead = Field(alias="case_type")
    description: str = Field(alias="description")
    project: DispatchCaseModelsProjectRead = Field(alias="project")
    reporter: ParticipantUpdate = Field(alias="reporter")
    resolution: str = Field(alias="resolution")
    resolution_reason: str = Field(alias="resolution_reason")  # An enumeration.
    status: str = Field(alias="status")  # An enumeration.
    tags: List[TagRead] = Field(alias="tags")
    title: str = Field(alias="title")
    visibility: str = Field(alias="visibility")  # An enumeration.
    
    class Config:
        populate_by_name = True


class CasePriorityBase(BaseModel):
    """CasePriorityBase schema from the OpenAPI specification."""
    color: str = Field(alias="color")
    default: bool = Field(alias="default")
    description: str = Field(alias="description")
    enabled: bool = Field(alias="enabled")
    name: str = Field(alias="name")
    page_assignee: bool = Field(alias="page_assignee")
    project: DispatchProjectModelsProjectRead = Field(alias="project")
    view_order: int = Field(alias="view_order")
    
    class Config:
        populate_by_name = True


class CasePriorityCreate(BaseModel):
    """CasePriorityCreate schema from the OpenAPI specification."""
    color: str = Field(alias="color")
    default: bool = Field(alias="default")
    description: str = Field(alias="description")
    enabled: bool = Field(alias="enabled")
    name: str = Field(alias="name")
    page_assignee: bool = Field(alias="page_assignee")
    project: DispatchProjectModelsProjectRead = Field(alias="project")
    view_order: int = Field(alias="view_order")
    
    class Config:
        populate_by_name = True


class CasePriorityPagination(BaseModel):
    """CasePriorityPagination schema from the OpenAPI specification."""
    items: List[CasePriorityRead] = Field(alias="items")
    total: int = Field(alias="total")
    
    class Config:
        populate_by_name = True


class CasePriorityRead(BaseModel):
    """CasePriorityRead schema from the OpenAPI specification."""
    color: str = Field(alias="color")
    default: bool = Field(alias="default")
    description: str = Field(alias="description")
    enabled: bool = Field(alias="enabled")
    id_field: int = Field(alias="id")
    name: str = Field(alias="name")
    page_assignee: bool = Field(alias="page_assignee")
    project: DispatchProjectModelsProjectRead = Field(alias="project")
    view_order: int = Field(alias="view_order")
    
    class Config:
        populate_by_name = True


class CasePriorityUpdate(BaseModel):
    """CasePriorityUpdate schema from the OpenAPI specification."""
    color: str = Field(alias="color")
    default: bool = Field(alias="default")
    description: str = Field(alias="description")
    enabled: bool = Field(alias="enabled")
    name: str = Field(alias="name")
    page_assignee: bool = Field(alias="page_assignee")
    project: DispatchProjectModelsProjectRead = Field(alias="project")
    view_order: int = Field(alias="view_order")
    
    class Config:
        populate_by_name = True


class CaseReadMinimal(BaseModel):
    """CaseReadMinimal schema from the OpenAPI specification."""
    assignee: ParticipantReadMinimal = Field(alias="assignee")
    case_priority: CasePriorityRead = Field(alias="case_priority")
    case_severity: CaseSeverityRead = Field(alias="case_severity")
    case_type: CaseTypeRead = Field(alias="case_type")
    closed_at: str = Field(alias="closed_at")
    created_at: str = Field(alias="created_at")
    description: str = Field(alias="description")
    duplicates: List[CaseReadMinimal] = Field(alias="duplicates")
    escalated_at: str = Field(alias="escalated_at")
    id_field: int = Field(alias="id")
    incidents: List[IncidentReadMinimal] = Field(alias="incidents")
    name: str = Field(alias="name")
    project: DispatchCaseModelsProjectRead = Field(alias="project")
    related: List[CaseReadMinimal] = Field(alias="related")
    reported_at: str = Field(alias="reported_at")
    resolution: str = Field(alias="resolution")
    resolution_reason: str = Field(alias="resolution_reason")  # An enumeration.
    status: str = Field(alias="status")  # An enumeration.
    title: str = Field(alias="title")
    triage_at: str = Field(alias="triage_at")
    visibility: str = Field(alias="visibility")  # An enumeration.
    
    class Config:
        populate_by_name = True


class CaseSeverityBase(BaseModel):
    """CaseSeverityBase schema from the OpenAPI specification."""
    color: str = Field(alias="color")
    default: bool = Field(alias="default")
    description: str = Field(alias="description")
    enabled: bool = Field(alias="enabled")
    name: str = Field(alias="name")
    project: DispatchProjectModelsProjectRead = Field(alias="project")
    view_order: int = Field(alias="view_order")
    
    class Config:
        populate_by_name = True


class CaseSeverityCreate(BaseModel):
    """CaseSeverityCreate schema from the OpenAPI specification."""
    color: str = Field(alias="color")
    default: bool = Field(alias="default")
    description: str = Field(alias="description")
    enabled: bool = Field(alias="enabled")
    name: str = Field(alias="name")
    project: DispatchProjectModelsProjectRead = Field(alias="project")
    view_order: int = Field(alias="view_order")
    
    class Config:
        populate_by_name = True


class CaseSeverityPagination(BaseModel):
    """CaseSeverityPagination schema from the OpenAPI specification."""
    items: List[CaseSeverityRead] = Field(alias="items")
    total: int = Field(alias="total")
    
    class Config:
        populate_by_name = True


class CaseSeverityRead(BaseModel):
    """CaseSeverityRead schema from the OpenAPI specification."""
    color: str = Field(alias="color")
    default: bool = Field(alias="default")
    description: str = Field(alias="description")
    enabled: bool = Field(alias="enabled")
    id_field: int = Field(alias="id")
    name: str = Field(alias="name")
    project: DispatchProjectModelsProjectRead = Field(alias="project")
    view_order: int = Field(alias="view_order")
    
    class Config:
        populate_by_name = True


class CaseSeverityUpdate(BaseModel):
    """CaseSeverityUpdate schema from the OpenAPI specification."""
    color: str = Field(alias="color")
    default: bool = Field(alias="default")
    description: str = Field(alias="description")
    enabled: bool = Field(alias="enabled")
    name: str = Field(alias="name")
    project: DispatchProjectModelsProjectRead = Field(alias="project")
    view_order: int = Field(alias="view_order")
    
    class Config:
        populate_by_name = True


class CaseTypeBase(BaseModel):
    """CaseTypeBase schema from the OpenAPI specification."""
    case_template_document: DispatchCaseTypeModelsDocument = Field(alias="case_template_document")
    conversation_target: str = Field(alias="conversation_target")
    default: bool = Field(alias="default")
    description: str = Field(alias="description")
    enabled: bool = Field(alias="enabled")
    exclude_from_metrics: bool = Field(alias="exclude_from_metrics")
    incident_type: IncidentType = Field(alias="incident_type")
    name: str = Field(alias="name")
    oncall_service: DispatchCaseTypeModelsService = Field(alias="oncall_service")
    plugin_metadata: List[PluginMetadata] = Field(alias="plugin_metadata")
    project: DispatchProjectModelsProjectRead = Field(alias="project")
    visibility: str = Field(alias="visibility")
    
    class Config:
        populate_by_name = True


class CaseTypeCreate(BaseModel):
    """CaseTypeCreate schema from the OpenAPI specification."""
    case_template_document: DispatchCaseTypeModelsDocument = Field(alias="case_template_document")
    conversation_target: str = Field(alias="conversation_target")
    default: bool = Field(alias="default")
    description: str = Field(alias="description")
    enabled: bool = Field(alias="enabled")
    exclude_from_metrics: bool = Field(alias="exclude_from_metrics")
    incident_type: IncidentType = Field(alias="incident_type")
    name: str = Field(alias="name")
    oncall_service: DispatchCaseTypeModelsService = Field(alias="oncall_service")
    plugin_metadata: List[PluginMetadata] = Field(alias="plugin_metadata")
    project: DispatchProjectModelsProjectRead = Field(alias="project")
    visibility: str = Field(alias="visibility")
    
    class Config:
        populate_by_name = True


class CaseTypePagination(BaseModel):
    """CaseTypePagination schema from the OpenAPI specification."""
    items: List[CaseTypeRead] = Field(alias="items")
    total: int = Field(alias="total")
    
    class Config:
        populate_by_name = True


class CaseTypeRead(BaseModel):
    """CaseTypeRead schema from the OpenAPI specification."""
    case_template_document: DispatchCaseTypeModelsDocument = Field(alias="case_template_document")
    conversation_target: str = Field(alias="conversation_target")
    default: bool = Field(alias="default")
    description: str = Field(alias="description")
    enabled: bool = Field(alias="enabled")
    exclude_from_metrics: bool = Field(alias="exclude_from_metrics")
    id_field: int = Field(alias="id")
    incident_type: IncidentType = Field(alias="incident_type")
    name: str = Field(alias="name")
    oncall_service: DispatchCaseTypeModelsService = Field(alias="oncall_service")
    plugin_metadata: List[PluginMetadata] = Field(alias="plugin_metadata")
    project: DispatchProjectModelsProjectRead = Field(alias="project")
    visibility: str = Field(alias="visibility")
    
    class Config:
        populate_by_name = True


class CaseTypeUpdate(BaseModel):
    """CaseTypeUpdate schema from the OpenAPI specification."""
    case_template_document: DispatchCaseTypeModelsDocument = Field(alias="case_template_document")
    conversation_target: str = Field(alias="conversation_target")
    default: bool = Field(alias="default")
    description: str = Field(alias="description")
    enabled: bool = Field(alias="enabled")
    exclude_from_metrics: bool = Field(alias="exclude_from_metrics")
    id_field: int = Field(alias="id")
    incident_type: IncidentType = Field(alias="incident_type")
    name: str = Field(alias="name")
    oncall_service: DispatchCaseTypeModelsService = Field(alias="oncall_service")
    plugin_metadata: List[PluginMetadata] = Field(alias="plugin_metadata")
    project: DispatchProjectModelsProjectRead = Field(alias="project")
    visibility: str = Field(alias="visibility")
    
    class Config:
        populate_by_name = True


class CaseUpdate(BaseModel):
    """CaseUpdate schema from the OpenAPI specification."""
    assignee: ParticipantUpdate = Field(alias="assignee")
    case_priority: CasePriorityBase = Field(alias="case_priority")
    case_severity: CaseSeverityBase = Field(alias="case_severity")
    case_type: CaseTypeBase = Field(alias="case_type")
    description: str = Field(alias="description")
    duplicates: List[DispatchCaseModelsCaseRead] = Field(alias="duplicates")
    escalated_at: str = Field(alias="escalated_at")
    incidents: List[IncidentReadMinimal] = Field(alias="incidents")
    related: List[DispatchCaseModelsCaseRead] = Field(alias="related")
    reported_at: str = Field(alias="reported_at")
    resolution: str = Field(alias="resolution")
    resolution_reason: str = Field(alias="resolution_reason")  # An enumeration.
    status: str = Field(alias="status")  # An enumeration.
    tags: List[TagRead] = Field(alias="tags")
    title: str = Field(alias="title")
    triage_at: str = Field(alias="triage_at")
    visibility: str = Field(alias="visibility")  # An enumeration.
    
    class Config:
        populate_by_name = True


class ConferenceRead(BaseModel):
    """ConferenceRead schema from the OpenAPI specification."""
    conference_challenge: str = Field(alias="conference_challenge")
    conference_id: str = Field(alias="conference_id")
    description: str = Field(alias="description")
    resource_id: str = Field(alias="resource_id")
    resource_type: str = Field(alias="resource_type")
    weblink: str = Field(alias="weblink")
    
    class Config:
        populate_by_name = True


class ConversationRead(BaseModel):
    """ConversationRead schema from the OpenAPI specification."""
    channel_id: str = Field(alias="channel_id")
    description: str = Field(alias="description")
    id_field: int = Field(alias="id")
    resource_id: str = Field(alias="resource_id")
    resource_type: str = Field(alias="resource_type")
    thread_id: str = Field(alias="thread_id")
    weblink: str = Field(alias="weblink")
    
    class Config:
        populate_by_name = True


class DefinitionCreate(BaseModel):
    """DefinitionCreate schema from the OpenAPI specification."""
    project: DispatchProjectModelsProjectRead = Field(alias="project")
    source: str = Field(alias="source")
    terms: List[DefinitionTerm] = Field(alias="terms")
    text: str = Field(alias="text")
    
    class Config:
        populate_by_name = True


class DefinitionPagination(BaseModel):
    """DefinitionPagination schema from the OpenAPI specification."""
    items: List[DefinitionRead] = Field(alias="items")
    total: int = Field(alias="total")
    
    class Config:
        populate_by_name = True


class DefinitionRead(BaseModel):
    """DefinitionRead schema from the OpenAPI specification."""
    id_field: int = Field(alias="id")
    source: str = Field(alias="source")
    terms: List[DefinitionTerm] = Field(alias="terms")
    text: str = Field(alias="text")
    
    class Config:
        populate_by_name = True


class DefinitionTerm(BaseModel):
    """DefinitionTerm schema from the OpenAPI specification."""
    id_field: int = Field(alias="id")
    text: str = Field(alias="text")
    
    class Config:
        populate_by_name = True


class DefinitionUpdate(BaseModel):
    """DefinitionUpdate schema from the OpenAPI specification."""
    source: str = Field(alias="source")
    terms: List[DefinitionTerm] = Field(alias="terms")
    text: str = Field(alias="text")
    
    class Config:
        populate_by_name = True


class DocumentCreate(BaseModel):
    """DocumentCreate schema from the OpenAPI specification."""
    created_at: str = Field(alias="created_at")
    description: str = Field(alias="description")
    evergreen: bool = Field(alias="evergreen")
    evergreen_last_reminder_at: str = Field(alias="evergreen_last_reminder_at")
    evergreen_owner: str = Field(alias="evergreen_owner")
    evergreen_reminder_interval: int = Field(alias="evergreen_reminder_interval")
    filters: List[SearchFilterRead] = Field(alias="filters")
    name: str = Field(alias="name")
    project: DispatchProjectModelsProjectRead = Field(alias="project")
    resource_id: str = Field(alias="resource_id")
    resource_type: str = Field(alias="resource_type")
    updated_at: str = Field(alias="updated_at")
    weblink: str = Field(alias="weblink")
    
    class Config:
        populate_by_name = True


class DocumentPagination(BaseModel):
    """DocumentPagination schema from the OpenAPI specification."""
    items: List[DocumentRead] = Field(alias="items")
    total: int = Field(alias="total")
    
    class Config:
        populate_by_name = True


class DocumentRead(BaseModel):
    """DocumentRead schema from the OpenAPI specification."""
    created_at: str = Field(alias="created_at")
    description: str = Field(alias="description")
    evergreen: bool = Field(alias="evergreen")
    evergreen_last_reminder_at: str = Field(alias="evergreen_last_reminder_at")
    evergreen_owner: str = Field(alias="evergreen_owner")
    evergreen_reminder_interval: int = Field(alias="evergreen_reminder_interval")
    filters: List[SearchFilterRead] = Field(alias="filters")
    id_field: int = Field(alias="id")
    name: str = Field(alias="name")
    project: DispatchProjectModelsProjectRead = Field(alias="project")
    resource_id: str = Field(alias="resource_id")
    resource_type: str = Field(alias="resource_type")
    updated_at: str = Field(alias="updated_at")
    weblink: str = Field(alias="weblink")
    
    class Config:
        populate_by_name = True


class DocumentUpdate(BaseModel):
    """DocumentUpdate schema from the OpenAPI specification."""
    created_at: str = Field(alias="created_at")
    description: str = Field(alias="description")
    evergreen: bool = Field(alias="evergreen")
    evergreen_last_reminder_at: str = Field(alias="evergreen_last_reminder_at")
    evergreen_owner: str = Field(alias="evergreen_owner")
    evergreen_reminder_interval: int = Field(alias="evergreen_reminder_interval")
    filters: List[SearchFilterRead] = Field(alias="filters")
    name: str = Field(alias="name")
    resource_id: str = Field(alias="resource_id")
    resource_type: str = Field(alias="resource_type")
    updated_at: str = Field(alias="updated_at")
    weblink: str = Field(alias="weblink")
    
    class Config:
        populate_by_name = True


class EntityCreate(BaseModel):
    """EntityCreate schema from the OpenAPI specification."""
    description: str = Field(alias="description")
    entity_type: EntityTypeCreate = Field(alias="entity_type")
    id_field: int = Field(alias="id")
    name: str = Field(alias="name")
    project: DispatchProjectModelsProjectRead = Field(alias="project")
    source: str = Field(alias="source")
    value: str = Field(alias="value")
    
    class Config:
        populate_by_name = True


class EntityPagination(BaseModel):
    """EntityPagination schema from the OpenAPI specification."""
    items: List[EntityRead] = Field(alias="items")
    total: int = Field(alias="total")
    
    class Config:
        populate_by_name = True


class EntityRead(BaseModel):
    """EntityRead schema from the OpenAPI specification."""
    description: str = Field(alias="description")
    entity_type: EntityTypeRead = Field(alias="entity_type")
    id_field: int = Field(alias="id")
    name: str = Field(alias="name")
    project: DispatchProjectModelsProjectRead = Field(alias="project")
    source: str = Field(alias="source")
    value: str = Field(alias="value")
    
    class Config:
        populate_by_name = True


class EntityTypeCreate(BaseModel):
    """EntityTypeCreate schema from the OpenAPI specification."""
    description: str = Field(alias="description")
    enabled: bool = Field(alias="enabled")
    global_find: bool = Field(alias="global_find")
    id_field: int = Field(alias="id")
    jpath: str = Field(alias="jpath")
    name: str = Field(alias="name")
    project: DispatchProjectModelsProjectRead = Field(alias="project")
    regular_expression: str = Field(alias="regular_expression")
    
    class Config:
        populate_by_name = True


class EntityTypePagination(BaseModel):
    """EntityTypePagination schema from the OpenAPI specification."""
    items: List[EntityTypeRead] = Field(alias="items")
    total: int = Field(alias="total")
    
    class Config:
        populate_by_name = True


class EntityTypeRead(BaseModel):
    """EntityTypeRead schema from the OpenAPI specification."""
    description: str = Field(alias="description")
    enabled: bool = Field(alias="enabled")
    global_find: bool = Field(alias="global_find")
    id_field: int = Field(alias="id")
    jpath: str = Field(alias="jpath")
    name: str = Field(alias="name")
    project: DispatchProjectModelsProjectRead = Field(alias="project")
    regular_expression: str = Field(alias="regular_expression")
    
    class Config:
        populate_by_name = True


class EntityTypeUpdate(BaseModel):
    """EntityTypeUpdate schema from the OpenAPI specification."""
    description: str = Field(alias="description")
    enabled: bool = Field(alias="enabled")
    global_find: bool = Field(alias="global_find")
    id_field: int = Field(alias="id")
    jpath: str = Field(alias="jpath")
    name: str = Field(alias="name")
    regular_expression: str = Field(alias="regular_expression")
    
    class Config:
        populate_by_name = True


class EntityUpdate(BaseModel):
    """EntityUpdate schema from the OpenAPI specification."""
    description: str = Field(alias="description")
    entity_type: EntityTypeUpdate = Field(alias="entity_type")
    id_field: int = Field(alias="id")
    name: str = Field(alias="name")
    source: str = Field(alias="source")
    value: str = Field(alias="value")
    
    class Config:
        populate_by_name = True


class ErrorMessage(BaseModel):
    """ErrorMessage schema from the OpenAPI specification."""
    msg: str = Field(alias="msg")
    
    class Config:
        populate_by_name = True


class ErrorResponse(BaseModel):
    """ErrorResponse schema from the OpenAPI specification."""
    detail: List[ErrorMessage] = Field(alias="detail")
    
    class Config:
        populate_by_name = True


class EventRead(BaseModel):
    """EventRead schema from the OpenAPI specification."""
    description: str = Field(alias="description")
    details: Dict[str, Any] = Field(alias="details")
    ended_at: str = Field(alias="ended_at")
    source: str = Field(alias="source")
    started_at: str = Field(alias="started_at")
    uuid: str = Field(alias="uuid")
    
    class Config:
        populate_by_name = True


class ExecutiveReportCreate(BaseModel):
    """ExecutiveReportCreate schema from the OpenAPI specification."""
    current_status: str = Field(alias="current_status")
    next_steps: str = Field(alias="next_steps")
    overview: str = Field(alias="overview")
    
    class Config:
        populate_by_name = True


class FeedbackCreate(BaseModel):
    """FeedbackCreate schema from the OpenAPI specification."""
    created_at: str = Field(alias="created_at")
    feedback: str = Field(alias="feedback")
    incident: IncidentReadMinimal = Field(alias="incident")
    participant: ParticipantRead = Field(alias="participant")
    rating: Any = Field(alias="rating")
    
    class Config:
        populate_by_name = True


class FeedbackPagination(BaseModel):
    """FeedbackPagination schema from the OpenAPI specification."""
    items: List[FeedbackRead] = Field(alias="items")
    total: int = Field(alias="total")
    
    class Config:
        populate_by_name = True


class FeedbackRead(BaseModel):
    """FeedbackRead schema from the OpenAPI specification."""
    created_at: str = Field(alias="created_at")
    feedback: str = Field(alias="feedback")
    id_field: int = Field(alias="id")
    incident: IncidentReadMinimal = Field(alias="incident")
    participant: ParticipantRead = Field(alias="participant")
    project: DispatchProjectModelsProjectRead = Field(alias="project")
    rating: Any = Field(alias="rating")
    
    class Config:
        populate_by_name = True


class FeedbackUpdate(BaseModel):
    """FeedbackUpdate schema from the OpenAPI specification."""
    created_at: str = Field(alias="created_at")
    feedback: str = Field(alias="feedback")
    id_field: int = Field(alias="id")
    incident: IncidentReadMinimal = Field(alias="incident")
    participant: ParticipantRead = Field(alias="participant")
    rating: Any = Field(alias="rating")
    
    class Config:
        populate_by_name = True


class GroupRead(BaseModel):
    """GroupRead schema from the OpenAPI specification."""
    description: str = Field(alias="description")
    email: str = Field(alias="email")
    id_field: int = Field(alias="id")
    name: str = Field(alias="name")
    resource_id: str = Field(alias="resource_id")
    resource_type: str = Field(alias="resource_type")
    weblink: str = Field(alias="weblink")
    
    class Config:
        populate_by_name = True


class HTTPValidationError(BaseModel):
    """HTTPValidationError schema from the OpenAPI specification."""
    detail: List[ValidationError] = Field(alias="detail")
    
    class Config:
        populate_by_name = True


class IncidentCostCreate(BaseModel):
    """IncidentCostCreate schema from the OpenAPI specification."""
    amount: float = Field(alias="amount")
    incident_cost_type: IncidentCostTypeRead = Field(alias="incident_cost_type")
    project: DispatchProjectModelsProjectRead = Field(alias="project")
    
    class Config:
        populate_by_name = True


class IncidentCostPagination(BaseModel):
    """IncidentCostPagination schema from the OpenAPI specification."""
    items: List[IncidentCostRead] = Field(alias="items")
    total: int = Field(alias="total")
    
    class Config:
        populate_by_name = True


class IncidentCostRead(BaseModel):
    """IncidentCostRead schema from the OpenAPI specification."""
    amount: float = Field(alias="amount")
    id_field: int = Field(alias="id")
    incident_cost_type: IncidentCostTypeRead = Field(alias="incident_cost_type")
    
    class Config:
        populate_by_name = True


class IncidentCostTypeCreate(BaseModel):
    """IncidentCostTypeCreate schema from the OpenAPI specification."""
    category: str = Field(alias="category")
    created_at: str = Field(alias="created_at")
    default: bool = Field(alias="default")
    description: str = Field(alias="description")
    details: Dict[str, Any] = Field(alias="details")
    editable: bool = Field(alias="editable")
    name: str = Field(alias="name")
    project: DispatchProjectModelsProjectRead = Field(alias="project")
    
    class Config:
        populate_by_name = True


class IncidentCostTypePagination(BaseModel):
    """IncidentCostTypePagination schema from the OpenAPI specification."""
    items: List[IncidentCostTypeRead] = Field(alias="items")
    total: int = Field(alias="total")
    
    class Config:
        populate_by_name = True


class IncidentCostTypeRead(BaseModel):
    """IncidentCostTypeRead schema from the OpenAPI specification."""
    category: str = Field(alias="category")
    created_at: str = Field(alias="created_at")
    default: bool = Field(alias="default")
    description: str = Field(alias="description")
    details: Dict[str, Any] = Field(alias="details")
    editable: bool = Field(alias="editable")
    id_field: int = Field(alias="id")
    name: str = Field(alias="name")
    
    class Config:
        populate_by_name = True


class IncidentCostTypeUpdate(BaseModel):
    """IncidentCostTypeUpdate schema from the OpenAPI specification."""
    category: str = Field(alias="category")
    created_at: str = Field(alias="created_at")
    default: bool = Field(alias="default")
    description: str = Field(alias="description")
    details: Dict[str, Any] = Field(alias="details")
    editable: bool = Field(alias="editable")
    id_field: int = Field(alias="id")
    name: str = Field(alias="name")
    
    class Config:
        populate_by_name = True


class IncidentCostUpdate(BaseModel):
    """IncidentCostUpdate schema from the OpenAPI specification."""
    amount: float = Field(alias="amount")
    id_field: int = Field(alias="id")
    incident_cost_type: IncidentCostTypeRead = Field(alias="incident_cost_type")
    
    class Config:
        populate_by_name = True


class IncidentCreate(BaseModel):
    """IncidentCreate schema from the OpenAPI specification."""
    commander: ParticipantUpdate = Field(alias="commander")
    description: str = Field(alias="description")
    incident_priority: IncidentPriorityCreate = Field(alias="incident_priority")
    incident_severity: IncidentSeverityCreate = Field(alias="incident_severity")
    incident_type: IncidentTypeCreate = Field(alias="incident_type")
    project: DispatchIncidentModelsProjectRead = Field(alias="project")
    reporter: ParticipantUpdate = Field(alias="reporter")
    resolution: str = Field(alias="resolution")
    status: str = Field(alias="status")  # An enumeration.
    tags: List[TagRead] = Field(alias="tags")
    title: str = Field(alias="title")
    visibility: str = Field(alias="visibility")  # An enumeration.
    
    class Config:
        populate_by_name = True


class IncidentPriorityBase(BaseModel):
    """IncidentPriorityBase schema from the OpenAPI specification."""
    color: str = Field(alias="color")
    default: bool = Field(alias="default")
    description: str = Field(alias="description")
    enabled: bool = Field(alias="enabled")
    executive_report_reminder: int = Field(alias="executive_report_reminder")
    name: str = Field(alias="name")
    page_commander: bool = Field(alias="page_commander")
    project: DispatchProjectModelsProjectRead = Field(alias="project")
    tactical_report_reminder: int = Field(alias="tactical_report_reminder")
    view_order: int = Field(alias="view_order")
    
    class Config:
        populate_by_name = True


class IncidentPriorityCreate(BaseModel):
    """IncidentPriorityCreate schema from the OpenAPI specification."""
    color: str = Field(alias="color")
    default: bool = Field(alias="default")
    description: str = Field(alias="description")
    enabled: bool = Field(alias="enabled")
    executive_report_reminder: int = Field(alias="executive_report_reminder")
    name: str = Field(alias="name")
    page_commander: bool = Field(alias="page_commander")
    project: DispatchProjectModelsProjectRead = Field(alias="project")
    tactical_report_reminder: int = Field(alias="tactical_report_reminder")
    view_order: int = Field(alias="view_order")
    
    class Config:
        populate_by_name = True


class IncidentPriorityPagination(BaseModel):
    """IncidentPriorityPagination schema from the OpenAPI specification."""
    items: List[IncidentPriorityRead] = Field(alias="items")
    total: int = Field(alias="total")
    
    class Config:
        populate_by_name = True


class IncidentPriorityRead(BaseModel):
    """IncidentPriorityRead schema from the OpenAPI specification."""
    color: str = Field(alias="color")
    default: bool = Field(alias="default")
    description: str = Field(alias="description")
    enabled: bool = Field(alias="enabled")
    executive_report_reminder: int = Field(alias="executive_report_reminder")
    id_field: int = Field(alias="id")
    name: str = Field(alias="name")
    page_commander: bool = Field(alias="page_commander")
    project: DispatchProjectModelsProjectRead = Field(alias="project")
    tactical_report_reminder: int = Field(alias="tactical_report_reminder")
    view_order: int = Field(alias="view_order")
    
    class Config:
        populate_by_name = True


class IncidentPriorityReadMinimal(BaseModel):
    """IncidentPriorityReadMinimal schema from the OpenAPI specification."""
    color: str = Field(alias="color")
    default: bool = Field(alias="default")
    description: str = Field(alias="description")
    enabled: bool = Field(alias="enabled")
    executive_report_reminder: int = Field(alias="executive_report_reminder")
    id_field: int = Field(alias="id")
    name: str = Field(alias="name")
    page_commander: bool = Field(alias="page_commander")
    tactical_report_reminder: int = Field(alias="tactical_report_reminder")
    view_order: int = Field(alias="view_order")
    
    class Config:
        populate_by_name = True


class IncidentPriorityUpdate(BaseModel):
    """IncidentPriorityUpdate schema from the OpenAPI specification."""
    color: str = Field(alias="color")
    default: bool = Field(alias="default")
    description: str = Field(alias="description")
    enabled: bool = Field(alias="enabled")
    executive_report_reminder: int = Field(alias="executive_report_reminder")
    name: str = Field(alias="name")
    page_commander: bool = Field(alias="page_commander")
    project: DispatchProjectModelsProjectRead = Field(alias="project")
    tactical_report_reminder: int = Field(alias="tactical_report_reminder")
    view_order: int = Field(alias="view_order")
    
    class Config:
        populate_by_name = True


class IncidentRead(BaseModel):
    """IncidentRead schema from the OpenAPI specification."""
    cases: List[DispatchIncidentModelsCaseRead] = Field(alias="cases")
    closed_at: str = Field(alias="closed_at")
    commander: ParticipantRead = Field(alias="commander")
    commanders_location: str = Field(alias="commanders_location")
    conference: ConferenceRead = Field(alias="conference")
    conversation: ConversationRead = Field(alias="conversation")
    created_at: str = Field(alias="created_at")
    description: str = Field(alias="description")
    documents: List[DocumentRead] = Field(alias="documents")
    duplicates: List[IncidentReadMinimal] = Field(alias="duplicates")
    events: List[EventRead] = Field(alias="events")
    id_field: int = Field(alias="id")
    incident_costs: List[IncidentCostRead] = Field(alias="incident_costs")
    incident_priority: IncidentPriorityRead = Field(alias="incident_priority")
    incident_severity: IncidentSeverityRead = Field(alias="incident_severity")
    incident_type: IncidentTypeRead = Field(alias="incident_type")
    last_executive_report: ReportRead = Field(alias="last_executive_report")
    last_tactical_report: ReportRead = Field(alias="last_tactical_report")
    name: str = Field(alias="name")
    participants: List[ParticipantRead] = Field(alias="participants")
    participants_location: str = Field(alias="participants_location")
    participants_team: str = Field(alias="participants_team")
    project: DispatchIncidentModelsProjectRead = Field(alias="project")
    reported_at: str = Field(alias="reported_at")
    reporter: ParticipantRead = Field(alias="reporter")
    reporters_location: str = Field(alias="reporters_location")
    resolution: str = Field(alias="resolution")
    stable_at: str = Field(alias="stable_at")
    status: str = Field(alias="status")  # An enumeration.
    storage: StorageRead = Field(alias="storage")
    tags: List[TagRead] = Field(alias="tags")
    tasks: List[DispatchIncidentModelsTaskRead] = Field(alias="tasks")
    terms: List[TermRead] = Field(alias="terms")
    ticket: TicketRead = Field(alias="ticket")
    title: str = Field(alias="title")
    total_cost: float = Field(alias="total_cost")
    visibility: str = Field(alias="visibility")  # An enumeration.
    workflow_instances: List[WorkflowInstanceRead] = Field(alias="workflow_instances")
    
    class Config:
        populate_by_name = True


class IncidentReadMinimal(BaseModel):
    """IncidentReadMinimal schema from the OpenAPI specification."""
    closed_at: str = Field(alias="closed_at")
    commander: ParticipantReadMinimal = Field(alias="commander")
    commanders_location: str = Field(alias="commanders_location")
    created_at: str = Field(alias="created_at")
    description: str = Field(alias="description")
    duplicates: List[IncidentReadMinimal] = Field(alias="duplicates")
    id_field: int = Field(alias="id")
    incident_costs: List[IncidentCostRead] = Field(alias="incident_costs")
    incident_priority: IncidentPriorityReadMinimal = Field(alias="incident_priority")
    incident_severity: IncidentSeverityReadMinimal = Field(alias="incident_severity")
    incident_type: IncidentTypeReadMinimal = Field(alias="incident_type")
    name: str = Field(alias="name")
    participants_location: str = Field(alias="participants_location")
    participants_team: str = Field(alias="participants_team")
    project: DispatchIncidentModelsProjectRead = Field(alias="project")
    reported_at: str = Field(alias="reported_at")
    reporter: ParticipantReadMinimal = Field(alias="reporter")
    reporters_location: str = Field(alias="reporters_location")
    resolution: str = Field(alias="resolution")
    stable_at: str = Field(alias="stable_at")
    status: str = Field(alias="status")  # An enumeration.
    tags: List[TagRead] = Field(alias="tags")
    title: str = Field(alias="title")
    total_cost: float = Field(alias="total_cost")
    visibility: str = Field(alias="visibility")  # An enumeration.
    
    class Config:
        populate_by_name = True


class IncidentRoleCreateUpdate(BaseModel):
    """IncidentRoleCreateUpdate schema from the OpenAPI specification."""
    enabled: bool = Field(alias="enabled")
    id_field: int = Field(alias="id")
    incident_priorities: List[IncidentPriorityRead] = Field(alias="incident_priorities")
    incident_types: List[IncidentTypeRead] = Field(alias="incident_types")
    individual: IndividualContactRead = Field(alias="individual")
    order: int = Field(alias="order")
    project: DispatchProjectModelsProjectRead = Field(alias="project")
    service: ServiceRead = Field(alias="service")
    tags: List[TagRead] = Field(alias="tags")
    
    class Config:
        populate_by_name = True


class IncidentRoleRead(BaseModel):
    """IncidentRoleRead schema from the OpenAPI specification."""
    created_at: str = Field(alias="created_at")
    enabled: bool = Field(alias="enabled")
    id_field: int = Field(alias="id")
    incident_priorities: List[IncidentPriorityRead] = Field(alias="incident_priorities")
    incident_types: List[IncidentTypeRead] = Field(alias="incident_types")
    individual: IndividualContactRead = Field(alias="individual")
    order: int = Field(alias="order")
    role: str = Field(alias="role")  # An enumeration.
    service: ServiceRead = Field(alias="service")
    tags: List[TagRead] = Field(alias="tags")
    updated_at: str = Field(alias="updated_at")
    
    class Config:
        populate_by_name = True


class IncidentRoles(BaseModel):
    """IncidentRoles schema from the OpenAPI specification."""
    policies: List[IncidentRoleRead] = Field(alias="policies")
    
    class Config:
        populate_by_name = True


class IncidentRolesCreateUpdate(BaseModel):
    """IncidentRolesCreateUpdate schema from the OpenAPI specification."""
    policies: List[IncidentRoleCreateUpdate] = Field(alias="policies")
    
    class Config:
        populate_by_name = True


class IncidentSeverityBase(BaseModel):
    """IncidentSeverityBase schema from the OpenAPI specification."""
    color: str = Field(alias="color")
    default: bool = Field(alias="default")
    description: str = Field(alias="description")
    enabled: bool = Field(alias="enabled")
    name: str = Field(alias="name")
    project: DispatchProjectModelsProjectRead = Field(alias="project")
    view_order: int = Field(alias="view_order")
    
    class Config:
        populate_by_name = True


class IncidentSeverityCreate(BaseModel):
    """IncidentSeverityCreate schema from the OpenAPI specification."""
    color: str = Field(alias="color")
    default: bool = Field(alias="default")
    description: str = Field(alias="description")
    enabled: bool = Field(alias="enabled")
    name: str = Field(alias="name")
    project: DispatchProjectModelsProjectRead = Field(alias="project")
    view_order: int = Field(alias="view_order")
    
    class Config:
        populate_by_name = True


class IncidentSeverityPagination(BaseModel):
    """IncidentSeverityPagination schema from the OpenAPI specification."""
    items: List[IncidentSeverityRead] = Field(alias="items")
    total: int = Field(alias="total")
    
    class Config:
        populate_by_name = True


class IncidentSeverityRead(BaseModel):
    """IncidentSeverityRead schema from the OpenAPI specification."""
    color: str = Field(alias="color")
    default: bool = Field(alias="default")
    description: str = Field(alias="description")
    enabled: bool = Field(alias="enabled")
    id_field: int = Field(alias="id")
    name: str = Field(alias="name")
    project: DispatchProjectModelsProjectRead = Field(alias="project")
    view_order: int = Field(alias="view_order")
    
    class Config:
        populate_by_name = True


class IncidentSeverityReadMinimal(BaseModel):
    """IncidentSeverityReadMinimal schema from the OpenAPI specification."""
    color: str = Field(alias="color")
    default: bool = Field(alias="default")
    description: str = Field(alias="description")
    enabled: bool = Field(alias="enabled")
    id_field: int = Field(alias="id")
    name: str = Field(alias="name")
    
    class Config:
        populate_by_name = True


class IncidentSeverityUpdate(BaseModel):
    """IncidentSeverityUpdate schema from the OpenAPI specification."""
    color: str = Field(alias="color")
    default: bool = Field(alias="default")
    description: str = Field(alias="description")
    enabled: bool = Field(alias="enabled")
    name: str = Field(alias="name")
    project: DispatchProjectModelsProjectRead = Field(alias="project")
    view_order: int = Field(alias="view_order")
    
    class Config:
        populate_by_name = True


class IncidentType(BaseModel):
    """IncidentType schema from the OpenAPI specification."""
    description: str = Field(alias="description")
    id_field: int = Field(alias="id")
    name: str = Field(alias="name")
    visibility: str = Field(alias="visibility")
    
    class Config:
        populate_by_name = True


class IncidentTypeBase(BaseModel):
    """IncidentTypeBase schema from the OpenAPI specification."""
    default: bool = Field(alias="default")
    description: str = Field(alias="description")
    enabled: bool = Field(alias="enabled")
    exclude_from_metrics: bool = Field(alias="exclude_from_metrics")
    executive_template_document: DispatchIncidentTypeModelsDocument = Field(alias="executive_template_document")
    incident_template_document: DispatchIncidentTypeModelsDocument = Field(alias="incident_template_document")
    name: str = Field(alias="name")
    plugin_metadata: List[PluginMetadata] = Field(alias="plugin_metadata")
    project: DispatchProjectModelsProjectRead = Field(alias="project")
    review_template_document: DispatchIncidentTypeModelsDocument = Field(alias="review_template_document")
    tracking_template_document: DispatchIncidentTypeModelsDocument = Field(alias="tracking_template_document")
    visibility: str = Field(alias="visibility")
    
    class Config:
        populate_by_name = True


class IncidentTypeCreate(BaseModel):
    """IncidentTypeCreate schema from the OpenAPI specification."""
    default: bool = Field(alias="default")
    description: str = Field(alias="description")
    enabled: bool = Field(alias="enabled")
    exclude_from_metrics: bool = Field(alias="exclude_from_metrics")
    executive_template_document: DispatchIncidentTypeModelsDocument = Field(alias="executive_template_document")
    incident_template_document: DispatchIncidentTypeModelsDocument = Field(alias="incident_template_document")
    name: str = Field(alias="name")
    plugin_metadata: List[PluginMetadata] = Field(alias="plugin_metadata")
    project: DispatchProjectModelsProjectRead = Field(alias="project")
    review_template_document: DispatchIncidentTypeModelsDocument = Field(alias="review_template_document")
    tracking_template_document: DispatchIncidentTypeModelsDocument = Field(alias="tracking_template_document")
    visibility: str = Field(alias="visibility")
    
    class Config:
        populate_by_name = True


class IncidentTypePagination(BaseModel):
    """IncidentTypePagination schema from the OpenAPI specification."""
    items: List[IncidentTypeRead] = Field(alias="items")
    total: int = Field(alias="total")
    
    class Config:
        populate_by_name = True


class IncidentTypeRead(BaseModel):
    """IncidentTypeRead schema from the OpenAPI specification."""
    default: bool = Field(alias="default")
    description: str = Field(alias="description")
    enabled: bool = Field(alias="enabled")
    exclude_from_metrics: bool = Field(alias="exclude_from_metrics")
    executive_template_document: DispatchIncidentTypeModelsDocument = Field(alias="executive_template_document")
    id_field: int = Field(alias="id")
    incident_template_document: DispatchIncidentTypeModelsDocument = Field(alias="incident_template_document")
    name: str = Field(alias="name")
    plugin_metadata: List[PluginMetadata] = Field(alias="plugin_metadata")
    project: DispatchProjectModelsProjectRead = Field(alias="project")
    review_template_document: DispatchIncidentTypeModelsDocument = Field(alias="review_template_document")
    tracking_template_document: DispatchIncidentTypeModelsDocument = Field(alias="tracking_template_document")
    visibility: str = Field(alias="visibility")
    
    class Config:
        populate_by_name = True


class IncidentTypeReadMinimal(BaseModel):
    """IncidentTypeReadMinimal schema from the OpenAPI specification."""
    default: bool = Field(alias="default")
    description: str = Field(alias="description")
    enabled: bool = Field(alias="enabled")
    exclude_from_metrics: bool = Field(alias="exclude_from_metrics")
    id_field: int = Field(alias="id")
    name: str = Field(alias="name")
    visibility: str = Field(alias="visibility")
    
    class Config:
        populate_by_name = True


class IncidentTypeUpdate(BaseModel):
    """IncidentTypeUpdate schema from the OpenAPI specification."""
    default: bool = Field(alias="default")
    description: str = Field(alias="description")
    enabled: bool = Field(alias="enabled")
    exclude_from_metrics: bool = Field(alias="exclude_from_metrics")
    executive_template_document: DispatchIncidentTypeModelsDocument = Field(alias="executive_template_document")
    id_field: int = Field(alias="id")
    incident_template_document: DispatchIncidentTypeModelsDocument = Field(alias="incident_template_document")
    name: str = Field(alias="name")
    plugin_metadata: List[PluginMetadata] = Field(alias="plugin_metadata")
    project: DispatchProjectModelsProjectRead = Field(alias="project")
    review_template_document: DispatchIncidentTypeModelsDocument = Field(alias="review_template_document")
    tracking_template_document: DispatchIncidentTypeModelsDocument = Field(alias="tracking_template_document")
    visibility: str = Field(alias="visibility")
    
    class Config:
        populate_by_name = True


class IncidentUpdate(BaseModel):
    """IncidentUpdate schema from the OpenAPI specification."""
    cases: List[DispatchIncidentModelsCaseRead] = Field(alias="cases")
    commander: ParticipantUpdate = Field(alias="commander")
    description: str = Field(alias="description")
    duplicates: List[IncidentReadMinimal] = Field(alias="duplicates")
    incident_costs: List[IncidentCostUpdate] = Field(alias="incident_costs")
    incident_priority: IncidentPriorityBase = Field(alias="incident_priority")
    incident_severity: IncidentSeverityBase = Field(alias="incident_severity")
    incident_type: IncidentTypeBase = Field(alias="incident_type")
    reported_at: str = Field(alias="reported_at")
    reporter: ParticipantUpdate = Field(alias="reporter")
    resolution: str = Field(alias="resolution")
    stable_at: str = Field(alias="stable_at")
    status: str = Field(alias="status")  # An enumeration.
    tags: List[TagRead] = Field(alias="tags")
    terms: List[TermRead] = Field(alias="terms")
    title: str = Field(alias="title")
    visibility: str = Field(alias="visibility")  # An enumeration.
    
    class Config:
        populate_by_name = True


class IndividualContactCreate(BaseModel):
    """IndividualContactCreate schema from the OpenAPI specification."""
    company: str = Field(alias="company")
    contact_type: str = Field(alias="contact_type")
    email: str = Field(alias="email")
    external_id: str = Field(alias="external_id")
    filters: List[SearchFilterRead] = Field(alias="filters")
    is_active: bool = Field(alias="is_active")
    is_external: bool = Field(alias="is_external")
    mobile_phone: str = Field(alias="mobile_phone")
    name: str = Field(alias="name")
    notes: str = Field(alias="notes")
    office_phone: str = Field(alias="office_phone")
    owner: str = Field(alias="owner")
    project: DispatchProjectModelsProjectRead = Field(alias="project")
    title: str = Field(alias="title")
    weblink: str = Field(alias="weblink")
    
    class Config:
        populate_by_name = True


class IndividualContactPagination(BaseModel):
    """IndividualContactPagination schema from the OpenAPI specification."""
    items: List[IndividualContactRead] = Field(alias="items")
    total: int = Field(alias="total")
    
    class Config:
        populate_by_name = True


class IndividualContactRead(BaseModel):
    """IndividualContactRead schema from the OpenAPI specification."""
    company: str = Field(alias="company")
    contact_type: str = Field(alias="contact_type")
    created_at: str = Field(alias="created_at")
    email: str = Field(alias="email")
    external_id: str = Field(alias="external_id")
    filters: List[SearchFilterRead] = Field(alias="filters")
    id_field: int = Field(alias="id")
    is_active: bool = Field(alias="is_active")
    is_external: bool = Field(alias="is_external")
    mobile_phone: str = Field(alias="mobile_phone")
    name: str = Field(alias="name")
    notes: str = Field(alias="notes")
    office_phone: str = Field(alias="office_phone")
    owner: str = Field(alias="owner")
    title: str = Field(alias="title")
    updated_at: str = Field(alias="updated_at")
    weblink: str = Field(alias="weblink")
    
    class Config:
        populate_by_name = True


class IndividualContactReadMinimal(BaseModel):
    """IndividualContactReadMinimal schema from the OpenAPI specification."""
    company: str = Field(alias="company")
    contact_type: str = Field(alias="contact_type")
    created_at: str = Field(alias="created_at")
    email: str = Field(alias="email")
    external_id: str = Field(alias="external_id")
    id_field: int = Field(alias="id")
    is_active: bool = Field(alias="is_active")
    is_external: bool = Field(alias="is_external")
    mobile_phone: str = Field(alias="mobile_phone")
    name: str = Field(alias="name")
    notes: str = Field(alias="notes")
    office_phone: str = Field(alias="office_phone")
    owner: str = Field(alias="owner")
    title: str = Field(alias="title")
    updated_at: str = Field(alias="updated_at")
    weblink: str = Field(alias="weblink")
    
    class Config:
        populate_by_name = True


class IndividualContactUpdate(BaseModel):
    """IndividualContactUpdate schema from the OpenAPI specification."""
    company: str = Field(alias="company")
    contact_type: str = Field(alias="contact_type")
    email: str = Field(alias="email")
    external_id: str = Field(alias="external_id")
    filters: List[SearchFilterRead] = Field(alias="filters")
    is_active: bool = Field(alias="is_active")
    is_external: bool = Field(alias="is_external")
    mobile_phone: str = Field(alias="mobile_phone")
    name: str = Field(alias="name")
    notes: str = Field(alias="notes")
    office_phone: str = Field(alias="office_phone")
    owner: str = Field(alias="owner")
    title: str = Field(alias="title")
    weblink: str = Field(alias="weblink")
    
    class Config:
        populate_by_name = True


class KeyValue(BaseModel):
    """KeyValue schema from the OpenAPI specification."""
    key: str = Field(alias="key")
    value: str = Field(alias="value")
    
    class Config:
        populate_by_name = True


class NotificationCreate(BaseModel):
    """NotificationCreate schema from the OpenAPI specification."""
    description: str = Field(alias="description")
    enabled: bool = Field(alias="enabled")
    evergreen: bool = Field(alias="evergreen")
    evergreen_last_reminder_at: str = Field(alias="evergreen_last_reminder_at")
    evergreen_owner: str = Field(alias="evergreen_owner")
    evergreen_reminder_interval: int = Field(alias="evergreen_reminder_interval")
    filters: List[SearchFilterRead] = Field(alias="filters")
    name: str = Field(alias="name")
    project: DispatchProjectModelsProjectRead = Field(alias="project")
    target: str = Field(alias="target")
    type_field: str = Field(alias="type")  # An enumeration.
    
    class Config:
        populate_by_name = True


class NotificationPagination(BaseModel):
    """NotificationPagination schema from the OpenAPI specification."""
    items: List[NotificationRead] = Field(alias="items")
    total: int = Field(alias="total")
    
    class Config:
        populate_by_name = True


class NotificationRead(BaseModel):
    """NotificationRead schema from the OpenAPI specification."""
    created_at: str = Field(alias="created_at")
    description: str = Field(alias="description")
    enabled: bool = Field(alias="enabled")
    evergreen: bool = Field(alias="evergreen")
    evergreen_last_reminder_at: str = Field(alias="evergreen_last_reminder_at")
    evergreen_owner: str = Field(alias="evergreen_owner")
    evergreen_reminder_interval: int = Field(alias="evergreen_reminder_interval")
    filters: List[SearchFilterRead] = Field(alias="filters")
    id_field: int = Field(alias="id")
    name: str = Field(alias="name")
    target: str = Field(alias="target")
    type_field: str = Field(alias="type")  # An enumeration.
    updated_at: str = Field(alias="updated_at")
    
    class Config:
        populate_by_name = True


class NotificationUpdate(BaseModel):
    """NotificationUpdate schema from the OpenAPI specification."""
    description: str = Field(alias="description")
    enabled: bool = Field(alias="enabled")
    evergreen: bool = Field(alias="evergreen")
    evergreen_last_reminder_at: str = Field(alias="evergreen_last_reminder_at")
    evergreen_owner: str = Field(alias="evergreen_owner")
    evergreen_reminder_interval: int = Field(alias="evergreen_reminder_interval")
    filters: List[SearchFilterUpdate] = Field(alias="filters")
    name: str = Field(alias="name")
    target: str = Field(alias="target")
    type_field: str = Field(alias="type")  # An enumeration.
    
    class Config:
        populate_by_name = True


class OrganizationCreate(BaseModel):
    """OrganizationCreate schema from the OpenAPI specification."""
    banner_color: str = Field(alias="banner_color")
    banner_enabled: bool = Field(alias="banner_enabled")
    banner_text: str = Field(alias="banner_text")
    default: bool = Field(alias="default")
    description: str = Field(alias="description")
    id_field: int = Field(alias="id")
    name: str = Field(alias="name")
    
    class Config:
        populate_by_name = True


class OrganizationPagination(BaseModel):
    """OrganizationPagination schema from the OpenAPI specification."""
    items: List[OrganizationRead] = Field(alias="items")
    total: int = Field(alias="total")
    
    class Config:
        populate_by_name = True


class OrganizationRead(BaseModel):
    """OrganizationRead schema from the OpenAPI specification."""
    banner_color: str = Field(alias="banner_color")
    banner_enabled: bool = Field(alias="banner_enabled")
    banner_text: str = Field(alias="banner_text")
    default: bool = Field(alias="default")
    description: str = Field(alias="description")
    id_field: int = Field(alias="id")
    name: str = Field(alias="name")
    slug: str = Field(alias="slug")
    
    class Config:
        populate_by_name = True


class OrganizationUpdate(BaseModel):
    """OrganizationUpdate schema from the OpenAPI specification."""
    banner_color: str = Field(alias="banner_color")
    banner_enabled: bool = Field(alias="banner_enabled")
    banner_text: str = Field(alias="banner_text")
    default: bool = Field(alias="default")
    description: str = Field(alias="description")
    id_field: int = Field(alias="id")
    
    class Config:
        populate_by_name = True


class ParticipantRead(BaseModel):
    """ParticipantRead schema from the OpenAPI specification."""
    added_reason: str = Field(alias="added_reason")
    department: str = Field(alias="department")
    id_field: int = Field(alias="id")
    individual: IndividualContactRead = Field(alias="individual")
    location: str = Field(alias="location")
    participant_roles: List[ParticipantRoleRead] = Field(alias="participant_roles")
    team: str = Field(alias="team")
    
    class Config:
        populate_by_name = True


class ParticipantReadMinimal(BaseModel):
    """ParticipantReadMinimal schema from the OpenAPI specification."""
    added_reason: str = Field(alias="added_reason")
    department: str = Field(alias="department")
    id_field: int = Field(alias="id")
    individual: IndividualContactReadMinimal = Field(alias="individual")
    location: str = Field(alias="location")
    participant_roles: List[ParticipantRoleReadMinimal] = Field(alias="participant_roles")
    team: str = Field(alias="team")
    
    class Config:
        populate_by_name = True


class ParticipantRoleRead(BaseModel):
    """ParticipantRoleRead schema from the OpenAPI specification."""
    activity: int = Field(alias="activity")
    assumed_at: str = Field(alias="assumed_at")
    id_field: int = Field(alias="id")
    renounced_at: str = Field(alias="renounced_at")
    role: str = Field(alias="role")
    
    class Config:
        populate_by_name = True


class ParticipantRoleReadMinimal(BaseModel):
    """ParticipantRoleReadMinimal schema from the OpenAPI specification."""
    activity: int = Field(alias="activity")
    assumed_at: str = Field(alias="assumed_at")
    id_field: int = Field(alias="id")
    renounced_at: str = Field(alias="renounced_at")
    role: str = Field(alias="role")
    
    class Config:
        populate_by_name = True


class ParticipantUpdate(BaseModel):
    """ParticipantUpdate schema from the OpenAPI specification."""
    added_reason: str = Field(alias="added_reason")
    department: str = Field(alias="department")
    individual: IndividualContactRead = Field(alias="individual")
    location: str = Field(alias="location")
    team: str = Field(alias="team")
    
    class Config:
        populate_by_name = True


class PluginInstanceCreate(BaseModel):
    """PluginInstanceCreate schema from the OpenAPI specification."""
    configuration: Dict[str, Any] = Field(alias="configuration")
    enabled: bool = Field(alias="enabled")
    plugin: PluginRead = Field(alias="plugin")
    project: DispatchProjectModelsProjectRead = Field(alias="project")
    
    class Config:
        populate_by_name = True


class PluginInstancePagination(BaseModel):
    """PluginInstancePagination schema from the OpenAPI specification."""
    items: List[PluginInstanceRead] = Field(alias="items")
    total: int = Field(alias="total")
    
    class Config:
        populate_by_name = True


class PluginInstanceRead(BaseModel):
    """PluginInstanceRead schema from the OpenAPI specification."""
    configuration: Dict[str, Any] = Field(alias="configuration")
    configuration_schema: Any = Field(alias="configuration_schema")
    enabled: bool = Field(alias="enabled")
    id_field: int = Field(alias="id")
    plugin: PluginRead = Field(alias="plugin")
    project: DispatchProjectModelsProjectRead = Field(alias="project")
    
    class Config:
        populate_by_name = True


class PluginInstanceUpdate(BaseModel):
    """PluginInstanceUpdate schema from the OpenAPI specification."""
    configuration: Dict[str, Any] = Field(alias="configuration")
    enabled: bool = Field(alias="enabled")
    id_field: int = Field(alias="id")
    
    class Config:
        populate_by_name = True


class PluginMetadata(BaseModel):
    """PluginMetadata schema from the OpenAPI specification."""
    metadata: List[KeyValue] = Field(alias="metadata")
    slug: str = Field(alias="slug")
    
    class Config:
        populate_by_name = True


class PluginPagination(BaseModel):
    """PluginPagination schema from the OpenAPI specification."""
    items: List[PluginRead] = Field(alias="items")
    total: int = Field(alias="total")
    
    class Config:
        populate_by_name = True


class PluginRead(BaseModel):
    """PluginRead schema from the OpenAPI specification."""
    author: str = Field(alias="author")
    author_url: str = Field(alias="author_url")
    configuration_schema: Any = Field(alias="configuration_schema")
    description: str = Field(alias="description")
    id_field: int = Field(alias="id")
    multiple: bool = Field(alias="multiple")
    slug: str = Field(alias="slug")
    title: str = Field(alias="title")
    type_field: str = Field(alias="type")
    
    class Config:
        populate_by_name = True


class ProjectCreate(BaseModel):
    """ProjectCreate schema from the OpenAPI specification."""
    annual_employee_cost: int = Field(alias="annual_employee_cost")
    business_year_hours: int = Field(alias="business_year_hours")
    color: str = Field(alias="color")
    default: bool = Field(alias="default")
    description: str = Field(alias="description")
    id_field: int = Field(alias="id")
    name: str = Field(alias="name")
    organization: OrganizationRead = Field(alias="organization")
    owner_conversation: str = Field(alias="owner_conversation")
    owner_email: str = Field(alias="owner_email")
    
    class Config:
        populate_by_name = True


class ProjectPagination(BaseModel):
    """ProjectPagination schema from the OpenAPI specification."""
    items: List[DispatchProjectModelsProjectRead] = Field(alias="items")
    total: int = Field(alias="total")
    
    class Config:
        populate_by_name = True


class ProjectUpdate(BaseModel):
    """ProjectUpdate schema from the OpenAPI specification."""
    annual_employee_cost: int = Field(alias="annual_employee_cost")
    business_year_hours: int = Field(alias="business_year_hours")
    color: str = Field(alias="color")
    default: bool = Field(alias="default")
    description: str = Field(alias="description")
    id_field: int = Field(alias="id")
    name: str = Field(alias="name")
    owner_conversation: str = Field(alias="owner_conversation")
    owner_email: str = Field(alias="owner_email")
    
    class Config:
        populate_by_name = True


class QueryCreate(BaseModel):
    """QueryCreate schema from the OpenAPI specification."""
    description: str = Field(alias="description")
    language: str = Field(alias="language")
    name: str = Field(alias="name")
    project: DispatchProjectModelsProjectRead = Field(alias="project")
    source: SourceRead = Field(alias="source")
    tags: List[TagRead] = Field(alias="tags")
    text: str = Field(alias="text")
    
    class Config:
        populate_by_name = True


class QueryPagination(BaseModel):
    """QueryPagination schema from the OpenAPI specification."""
    items: List[QueryRead] = Field(alias="items")
    total: int = Field(alias="total")
    
    class Config:
        populate_by_name = True


class QueryRead(BaseModel):
    """QueryRead schema from the OpenAPI specification."""
    description: str = Field(alias="description")
    id_field: int = Field(alias="id")
    language: str = Field(alias="language")
    name: str = Field(alias="name")
    project: DispatchProjectModelsProjectRead = Field(alias="project")
    source: SourceRead = Field(alias="source")
    tags: List[TagRead] = Field(alias="tags")
    text: str = Field(alias="text")
    
    class Config:
        populate_by_name = True


class QueryReadMinimal(BaseModel):
    """QueryReadMinimal schema from the OpenAPI specification."""
    description: str = Field(alias="description")
    id_field: int = Field(alias="id")
    name: str = Field(alias="name")
    
    class Config:
        populate_by_name = True


class QueryUpdate(BaseModel):
    """QueryUpdate schema from the OpenAPI specification."""
    description: str = Field(alias="description")
    id_field: int = Field(alias="id")
    language: str = Field(alias="language")
    name: str = Field(alias="name")
    project: DispatchProjectModelsProjectRead = Field(alias="project")
    source: SourceRead = Field(alias="source")
    tags: List[TagRead] = Field(alias="tags")
    text: str = Field(alias="text")
    
    class Config:
        populate_by_name = True


class ReportRead(BaseModel):
    """ReportRead schema from the OpenAPI specification."""
    created_at: str = Field(alias="created_at")
    details: Dict[str, Any] = Field(alias="details")
    id_field: int = Field(alias="id")
    type_field: str = Field(alias="type")  # An enumeration.
    
    class Config:
        populate_by_name = True


class SearchFilterCreate(BaseModel):
    """SearchFilterCreate schema from the OpenAPI specification."""
    description: str = Field(alias="description")
    expression: List[Dict[str, Any]] = Field(alias="expression")
    name: str = Field(alias="name")
    project: DispatchProjectModelsProjectRead = Field(alias="project")
    subject: Any = Field(alias="subject")
    
    class Config:
        populate_by_name = True


class SearchFilterPagination(BaseModel):
    """SearchFilterPagination schema from the OpenAPI specification."""
    items: List[SearchFilterRead] = Field(alias="items")
    total: int = Field(alias="total")
    
    class Config:
        populate_by_name = True


class SearchFilterRead(BaseModel):
    """SearchFilterRead schema from the OpenAPI specification."""
    creator: UserRead = Field(alias="creator")
    description: str = Field(alias="description")
    expression: List[Dict[str, Any]] = Field(alias="expression")
    id_field: int = Field(alias="id")
    name: str = Field(alias="name")
    subject: Any = Field(alias="subject")
    
    class Config:
        populate_by_name = True


class SearchFilterUpdate(BaseModel):
    """SearchFilterUpdate schema from the OpenAPI specification."""
    description: str = Field(alias="description")
    expression: List[Dict[str, Any]] = Field(alias="expression")
    id_field: int = Field(alias="id")
    name: str = Field(alias="name")
    subject: Any = Field(alias="subject")
    
    class Config:
        populate_by_name = True


class ServiceCreate(BaseModel):
    """ServiceCreate schema from the OpenAPI specification."""
    description: str = Field(alias="description")
    evergreen: bool = Field(alias="evergreen")
    evergreen_last_reminder_at: str = Field(alias="evergreen_last_reminder_at")
    evergreen_owner: str = Field(alias="evergreen_owner")
    evergreen_reminder_interval: int = Field(alias="evergreen_reminder_interval")
    external_id: str = Field(alias="external_id")
    filters: List[SearchFilterRead] = Field(alias="filters")
    is_active: bool = Field(alias="is_active")
    name: str = Field(alias="name")
    project: DispatchProjectModelsProjectRead = Field(alias="project")
    type_field: str = Field(alias="type")
    
    class Config:
        populate_by_name = True


class ServicePagination(BaseModel):
    """ServicePagination schema from the OpenAPI specification."""
    items: List[ServiceRead] = Field(alias="items")
    total: int = Field(alias="total")
    
    class Config:
        populate_by_name = True


class ServiceRead(BaseModel):
    """ServiceRead schema from the OpenAPI specification."""
    created_at: str = Field(alias="created_at")
    description: str = Field(alias="description")
    evergreen: bool = Field(alias="evergreen")
    evergreen_last_reminder_at: str = Field(alias="evergreen_last_reminder_at")
    evergreen_owner: str = Field(alias="evergreen_owner")
    evergreen_reminder_interval: int = Field(alias="evergreen_reminder_interval")
    external_id: str = Field(alias="external_id")
    filters: List[SearchFilterRead] = Field(alias="filters")
    id_field: int = Field(alias="id")
    is_active: bool = Field(alias="is_active")
    name: str = Field(alias="name")
    type_field: str = Field(alias="type")
    updated_at: str = Field(alias="updated_at")
    
    class Config:
        populate_by_name = True


class ServiceUpdate(BaseModel):
    """ServiceUpdate schema from the OpenAPI specification."""
    description: str = Field(alias="description")
    evergreen: bool = Field(alias="evergreen")
    evergreen_last_reminder_at: str = Field(alias="evergreen_last_reminder_at")
    evergreen_owner: str = Field(alias="evergreen_owner")
    evergreen_reminder_interval: int = Field(alias="evergreen_reminder_interval")
    external_id: str = Field(alias="external_id")
    filters: List[SearchFilterRead] = Field(alias="filters")
    is_active: bool = Field(alias="is_active")
    name: str = Field(alias="name")
    type_field: str = Field(alias="type")
    
    class Config:
        populate_by_name = True


class SignalCreate(BaseModel):
    """SignalCreate schema from the OpenAPI specification."""
    case_priority: CasePriorityRead = Field(alias="case_priority")
    case_type: CaseTypeRead = Field(alias="case_type")
    conversation_target: str = Field(alias="conversation_target")
    create_case: bool = Field(alias="create_case")
    created_at: str = Field(alias="created_at")
    description: str = Field(alias="description")
    enabled: bool = Field(alias="enabled")
    entity_types: List[EntityTypeRead] = Field(alias="entity_types")
    external_id: str = Field(alias="external_id")
    external_url: str = Field(alias="external_url")
    filters: List[SignalFilterRead] = Field(alias="filters")
    name: str = Field(alias="name")
    oncall_service: DispatchSignalModelsService = Field(alias="oncall_service")
    owner: str = Field(alias="owner")
    project: DispatchProjectModelsProjectRead = Field(alias="project")
    source: SourceBase = Field(alias="source")
    tags: List[TagRead] = Field(alias="tags")
    variant: str = Field(alias="variant")
    workflows: List[WorkflowRead] = Field(alias="workflows")
    
    class Config:
        populate_by_name = True


class SignalFilterCreate(BaseModel):
    """SignalFilterCreate schema from the OpenAPI specification."""
    action: Any = Field(alias="action")
    description: str = Field(alias="description")
    expiration: str = Field(alias="expiration")
    expression: List[Dict[str, Any]] = Field(alias="expression")
    mode: Any = Field(alias="mode")
    name: str = Field(alias="name")
    project: DispatchProjectModelsProjectRead = Field(alias="project")
    window: int = Field(alias="window")
    
    class Config:
        populate_by_name = True


class SignalFilterPagination(BaseModel):
    """SignalFilterPagination schema from the OpenAPI specification."""
    items: List[SignalFilterRead] = Field(alias="items")
    total: int = Field(alias="total")
    
    class Config:
        populate_by_name = True


class SignalFilterRead(BaseModel):
    """SignalFilterRead schema from the OpenAPI specification."""
    action: Any = Field(alias="action")
    description: str = Field(alias="description")
    expiration: str = Field(alias="expiration")
    expression: List[Dict[str, Any]] = Field(alias="expression")
    id_field: int = Field(alias="id")
    mode: Any = Field(alias="mode")
    name: str = Field(alias="name")
    window: int = Field(alias="window")
    
    class Config:
        populate_by_name = True


class SignalFilterUpdate(BaseModel):
    """SignalFilterUpdate schema from the OpenAPI specification."""
    action: Any = Field(alias="action")
    description: str = Field(alias="description")
    expiration: str = Field(alias="expiration")
    expression: List[Dict[str, Any]] = Field(alias="expression")
    id_field: int = Field(alias="id")
    mode: Any = Field(alias="mode")
    name: str = Field(alias="name")
    window: int = Field(alias="window")
    
    class Config:
        populate_by_name = True


class SignalInstanceCreate(BaseModel):
    """SignalInstanceCreate schema from the OpenAPI specification."""
    case: DispatchCaseModelsCaseRead = Field(alias="case")
    created_at: str = Field(alias="created_at")
    entities: List[EntityRead] = Field(alias="entities")
    filter_action: str = Field(alias="filter_action")  # An enumeration.
    project: DispatchProjectModelsProjectRead = Field(alias="project")
    raw: Dict[str, Any] = Field(alias="raw")
    signal: DispatchSignalModelsSignalRead = Field(alias="signal")
    
    class Config:
        populate_by_name = True


class SignalInstancePagination(BaseModel):
    """SignalInstancePagination schema from the OpenAPI specification."""
    items: List[DispatchSignalModelsSignalInstanceRead] = Field(alias="items")
    total: int = Field(alias="total")
    
    class Config:
        populate_by_name = True


class SignalPagination(BaseModel):
    """SignalPagination schema from the OpenAPI specification."""
    items: List[DispatchSignalModelsSignalRead] = Field(alias="items")
    total: int = Field(alias="total")
    
    class Config:
        populate_by_name = True


class SignalUpdate(BaseModel):
    """SignalUpdate schema from the OpenAPI specification."""
    case_priority: CasePriorityRead = Field(alias="case_priority")
    case_type: CaseTypeRead = Field(alias="case_type")
    conversation_target: str = Field(alias="conversation_target")
    create_case: bool = Field(alias="create_case")
    created_at: str = Field(alias="created_at")
    description: str = Field(alias="description")
    enabled: bool = Field(alias="enabled")
    entity_types: List[EntityTypeRead] = Field(alias="entity_types")
    external_id: str = Field(alias="external_id")
    external_url: str = Field(alias="external_url")
    filters: List[SignalFilterRead] = Field(alias="filters")
    id_field: int = Field(alias="id")
    name: str = Field(alias="name")
    oncall_service: DispatchSignalModelsService = Field(alias="oncall_service")
    owner: str = Field(alias="owner")
    project: DispatchProjectModelsProjectRead = Field(alias="project")
    source: SourceBase = Field(alias="source")
    tags: List[TagRead] = Field(alias="tags")
    variant: str = Field(alias="variant")
    workflows: List[WorkflowRead] = Field(alias="workflows")
    
    class Config:
        populate_by_name = True


class SourceBase(BaseModel):
    """SourceBase schema from the OpenAPI specification."""
    aggregated: bool = Field(alias="aggregated")
    alerts: List[AlertRead] = Field(alias="alerts")
    cost: float = Field(alias="cost")
    data_last_loaded_at: str = Field(alias="data_last_loaded_at")
    delay: int = Field(alias="delay")
    description: str = Field(alias="description")
    documentation: str = Field(alias="documentation")
    external_id: str = Field(alias="external_id")
    incidents: List[IncidentRead] = Field(alias="incidents")
    links: List[Any] = Field(alias="links")
    name: str = Field(alias="name")
    owner: Any = Field(alias="owner")
    project: DispatchProjectModelsProjectRead = Field(alias="project")
    queries: List[QueryReadMinimal] = Field(alias="queries")
    retention: int = Field(alias="retention")
    sampling_rate: int = Field(alias="sampling_rate")  # Rate at which data is sampled (as a percentage) 100% meaning all data is captured.
    size: int = Field(alias="size")
    source_data_format: SourceDataFormatRead = Field(alias="source_data_format")
    source_environment: SourceEnvironmentRead = Field(alias="source_environment")
    source_schema: str = Field(alias="source_schema")
    source_status: SourceStatusRead = Field(alias="source_status")
    source_transport: SourceTransportRead = Field(alias="source_transport")
    source_type: SourceTypeRead = Field(alias="source_type")
    tags: List[TagRead] = Field(alias="tags")
    
    class Config:
        populate_by_name = True


class SourceCreate(BaseModel):
    """SourceCreate schema from the OpenAPI specification."""
    aggregated: bool = Field(alias="aggregated")
    alerts: List[AlertRead] = Field(alias="alerts")
    cost: float = Field(alias="cost")
    data_last_loaded_at: str = Field(alias="data_last_loaded_at")
    delay: int = Field(alias="delay")
    description: str = Field(alias="description")
    documentation: str = Field(alias="documentation")
    external_id: str = Field(alias="external_id")
    incidents: List[IncidentRead] = Field(alias="incidents")
    links: List[Any] = Field(alias="links")
    name: str = Field(alias="name")
    owner: Any = Field(alias="owner")
    project: DispatchProjectModelsProjectRead = Field(alias="project")
    queries: List[QueryReadMinimal] = Field(alias="queries")
    retention: int = Field(alias="retention")
    sampling_rate: int = Field(alias="sampling_rate")  # Rate at which data is sampled (as a percentage) 100% meaning all data is captured.
    size: int = Field(alias="size")
    source_data_format: SourceDataFormatRead = Field(alias="source_data_format")
    source_environment: SourceEnvironmentRead = Field(alias="source_environment")
    source_schema: str = Field(alias="source_schema")
    source_status: SourceStatusRead = Field(alias="source_status")
    source_transport: SourceTransportRead = Field(alias="source_transport")
    source_type: SourceTypeRead = Field(alias="source_type")
    tags: List[TagRead] = Field(alias="tags")
    
    class Config:
        populate_by_name = True


class SourceDataFormatCreate(BaseModel):
    """SourceDataFormatCreate schema from the OpenAPI specification."""
    description: str = Field(alias="description")
    name: str = Field(alias="name")
    project: DispatchProjectModelsProjectRead = Field(alias="project")
    
    class Config:
        populate_by_name = True


class SourceDataFormatPagination(BaseModel):
    """SourceDataFormatPagination schema from the OpenAPI specification."""
    items: List[SourceDataFormatRead] = Field(alias="items")
    total: int = Field(alias="total")
    
    class Config:
        populate_by_name = True


class SourceDataFormatRead(BaseModel):
    """SourceDataFormatRead schema from the OpenAPI specification."""
    description: str = Field(alias="description")
    id_field: int = Field(alias="id")
    name: str = Field(alias="name")
    project: DispatchProjectModelsProjectRead = Field(alias="project")
    
    class Config:
        populate_by_name = True


class SourceDataFormatUpdate(BaseModel):
    """SourceDataFormatUpdate schema from the OpenAPI specification."""
    description: str = Field(alias="description")
    id_field: int = Field(alias="id")
    name: str = Field(alias="name")
    
    class Config:
        populate_by_name = True


class SourceEnvironmentCreate(BaseModel):
    """SourceEnvironmentCreate schema from the OpenAPI specification."""
    description: str = Field(alias="description")
    name: str = Field(alias="name")
    project: DispatchProjectModelsProjectRead = Field(alias="project")
    
    class Config:
        populate_by_name = True


class SourceEnvironmentPagination(BaseModel):
    """SourceEnvironmentPagination schema from the OpenAPI specification."""
    items: List[SourceEnvironmentRead] = Field(alias="items")
    total: int = Field(alias="total")
    
    class Config:
        populate_by_name = True


class SourceEnvironmentRead(BaseModel):
    """SourceEnvironmentRead schema from the OpenAPI specification."""
    description: str = Field(alias="description")
    id_field: int = Field(alias="id")
    name: str = Field(alias="name")
    project: DispatchProjectModelsProjectRead = Field(alias="project")
    
    class Config:
        populate_by_name = True


class SourceEnvironmentUpdate(BaseModel):
    """SourceEnvironmentUpdate schema from the OpenAPI specification."""
    description: str = Field(alias="description")
    id_field: int = Field(alias="id")
    name: str = Field(alias="name")
    
    class Config:
        populate_by_name = True


class SourcePagination(BaseModel):
    """SourcePagination schema from the OpenAPI specification."""
    items: List[SourceRead] = Field(alias="items")
    total: int = Field(alias="total")
    
    class Config:
        populate_by_name = True


class SourceRead(BaseModel):
    """SourceRead schema from the OpenAPI specification."""
    aggregated: bool = Field(alias="aggregated")
    alerts: List[AlertRead] = Field(alias="alerts")
    cost: float = Field(alias="cost")
    data_last_loaded_at: str = Field(alias="data_last_loaded_at")
    delay: int = Field(alias="delay")
    description: str = Field(alias="description")
    documentation: str = Field(alias="documentation")
    external_id: str = Field(alias="external_id")
    id_field: int = Field(alias="id")
    incidents: List[IncidentRead] = Field(alias="incidents")
    links: List[Any] = Field(alias="links")
    name: str = Field(alias="name")
    owner: Any = Field(alias="owner")
    project: DispatchProjectModelsProjectRead = Field(alias="project")
    queries: List[QueryReadMinimal] = Field(alias="queries")
    retention: int = Field(alias="retention")
    sampling_rate: int = Field(alias="sampling_rate")  # Rate at which data is sampled (as a percentage) 100% meaning all data is captured.
    size: int = Field(alias="size")
    source_data_format: SourceDataFormatRead = Field(alias="source_data_format")
    source_environment: SourceEnvironmentRead = Field(alias="source_environment")
    source_schema: str = Field(alias="source_schema")
    source_status: SourceStatusRead = Field(alias="source_status")
    source_transport: SourceTransportRead = Field(alias="source_transport")
    source_type: SourceTypeRead = Field(alias="source_type")
    tags: List[TagRead] = Field(alias="tags")
    
    class Config:
        populate_by_name = True


class SourceStatusCreate(BaseModel):
    """SourceStatusCreate schema from the OpenAPI specification."""
    description: str = Field(alias="description")
    name: str = Field(alias="name")
    project: DispatchProjectModelsProjectRead = Field(alias="project")
    
    class Config:
        populate_by_name = True


class SourceStatusPagination(BaseModel):
    """SourceStatusPagination schema from the OpenAPI specification."""
    items: List[SourceStatusRead] = Field(alias="items")
    total: int = Field(alias="total")
    
    class Config:
        populate_by_name = True


class SourceStatusRead(BaseModel):
    """SourceStatusRead schema from the OpenAPI specification."""
    description: str = Field(alias="description")
    id_field: int = Field(alias="id")
    name: str = Field(alias="name")
    project: DispatchProjectModelsProjectRead = Field(alias="project")
    
    class Config:
        populate_by_name = True


class SourceStatusUpdate(BaseModel):
    """SourceStatusUpdate schema from the OpenAPI specification."""
    description: str = Field(alias="description")
    id_field: int = Field(alias="id")
    name: str = Field(alias="name")
    
    class Config:
        populate_by_name = True


class SourceTransportCreate(BaseModel):
    """SourceTransportCreate schema from the OpenAPI specification."""
    description: str = Field(alias="description")
    name: str = Field(alias="name")
    project: DispatchProjectModelsProjectRead = Field(alias="project")
    
    class Config:
        populate_by_name = True


class SourceTransportPagination(BaseModel):
    """SourceTransportPagination schema from the OpenAPI specification."""
    items: List[SourceTransportRead] = Field(alias="items")
    total: int = Field(alias="total")
    
    class Config:
        populate_by_name = True


class SourceTransportRead(BaseModel):
    """SourceTransportRead schema from the OpenAPI specification."""
    description: str = Field(alias="description")
    id_field: int = Field(alias="id")
    name: str = Field(alias="name")
    project: DispatchProjectModelsProjectRead = Field(alias="project")
    
    class Config:
        populate_by_name = True


class SourceTransportUpdate(BaseModel):
    """SourceTransportUpdate schema from the OpenAPI specification."""
    description: str = Field(alias="description")
    id_field: int = Field(alias="id")
    name: str = Field(alias="name")
    
    class Config:
        populate_by_name = True


class SourceTypeCreate(BaseModel):
    """SourceTypeCreate schema from the OpenAPI specification."""
    description: str = Field(alias="description")
    name: str = Field(alias="name")
    project: DispatchProjectModelsProjectRead = Field(alias="project")
    
    class Config:
        populate_by_name = True


class SourceTypePagination(BaseModel):
    """SourceTypePagination schema from the OpenAPI specification."""
    items: List[SourceTypeRead] = Field(alias="items")
    total: int = Field(alias="total")
    
    class Config:
        populate_by_name = True


class SourceTypeRead(BaseModel):
    """SourceTypeRead schema from the OpenAPI specification."""
    description: str = Field(alias="description")
    id_field: int = Field(alias="id")
    name: str = Field(alias="name")
    project: DispatchProjectModelsProjectRead = Field(alias="project")
    
    class Config:
        populate_by_name = True


class SourceTypeUpdate(BaseModel):
    """SourceTypeUpdate schema from the OpenAPI specification."""
    description: str = Field(alias="description")
    id_field: int = Field(alias="id")
    name: str = Field(alias="name")
    
    class Config:
        populate_by_name = True


class SourceUpdate(BaseModel):
    """SourceUpdate schema from the OpenAPI specification."""
    aggregated: bool = Field(alias="aggregated")
    alerts: List[AlertRead] = Field(alias="alerts")
    cost: float = Field(alias="cost")
    data_last_loaded_at: str = Field(alias="data_last_loaded_at")
    delay: int = Field(alias="delay")
    description: str = Field(alias="description")
    documentation: str = Field(alias="documentation")
    external_id: str = Field(alias="external_id")
    id_field: int = Field(alias="id")
    incidents: List[IncidentRead] = Field(alias="incidents")
    links: List[Any] = Field(alias="links")
    name: str = Field(alias="name")
    owner: Any = Field(alias="owner")
    project: DispatchProjectModelsProjectRead = Field(alias="project")
    queries: List[QueryReadMinimal] = Field(alias="queries")
    retention: int = Field(alias="retention")
    sampling_rate: int = Field(alias="sampling_rate")  # Rate at which data is sampled (as a percentage) 100% meaning all data is captured.
    size: int = Field(alias="size")
    source_data_format: SourceDataFormatRead = Field(alias="source_data_format")
    source_environment: SourceEnvironmentRead = Field(alias="source_environment")
    source_schema: str = Field(alias="source_schema")
    source_status: SourceStatusRead = Field(alias="source_status")
    source_transport: SourceTransportRead = Field(alias="source_transport")
    source_type: SourceTypeRead = Field(alias="source_type")
    tags: List[TagRead] = Field(alias="tags")
    
    class Config:
        populate_by_name = True


class StorageRead(BaseModel):
    """StorageRead schema from the OpenAPI specification."""
    description: str = Field(alias="description")
    resource_id: str = Field(alias="resource_id")
    resource_type: str = Field(alias="resource_type")
    weblink: str = Field(alias="weblink")
    
    class Config:
        populate_by_name = True


class TacticalReportCreate(BaseModel):
    """TacticalReportCreate schema from the OpenAPI specification."""
    actions: str = Field(alias="actions")
    conditions: str = Field(alias="conditions")
    needs: str = Field(alias="needs")
    
    class Config:
        populate_by_name = True


class TagCreate(BaseModel):
    """TagCreate schema from the OpenAPI specification."""
    description: str = Field(alias="description")
    discoverable: bool = Field(alias="discoverable")
    external_id: str = Field(alias="external_id")
    id_field: int = Field(alias="id")
    name: str = Field(alias="name")
    project: DispatchProjectModelsProjectRead = Field(alias="project")
    source: str = Field(alias="source")
    tag_type: TagTypeCreate = Field(alias="tag_type")
    uri: str = Field(alias="uri")
    
    class Config:
        populate_by_name = True


class TagPagination(BaseModel):
    """TagPagination schema from the OpenAPI specification."""
    items: List[TagRead] = Field(alias="items")
    total: int = Field(alias="total")
    
    class Config:
        populate_by_name = True


class TagRead(BaseModel):
    """TagRead schema from the OpenAPI specification."""
    description: str = Field(alias="description")
    discoverable: bool = Field(alias="discoverable")
    external_id: str = Field(alias="external_id")
    id_field: int = Field(alias="id")
    name: str = Field(alias="name")
    project: DispatchProjectModelsProjectRead = Field(alias="project")
    source: str = Field(alias="source")
    tag_type: TagTypeRead = Field(alias="tag_type")
    uri: str = Field(alias="uri")
    
    class Config:
        populate_by_name = True


class TagTypeCreate(BaseModel):
    """TagTypeCreate schema from the OpenAPI specification."""
    description: str = Field(alias="description")
    exclusive: bool = Field(alias="exclusive")
    name: str = Field(alias="name")
    project: DispatchProjectModelsProjectRead = Field(alias="project")
    
    class Config:
        populate_by_name = True


class TagTypePagination(BaseModel):
    """TagTypePagination schema from the OpenAPI specification."""
    items: List[TagTypeRead] = Field(alias="items")
    total: int = Field(alias="total")
    
    class Config:
        populate_by_name = True


class TagTypeRead(BaseModel):
    """TagTypeRead schema from the OpenAPI specification."""
    description: str = Field(alias="description")
    exclusive: bool = Field(alias="exclusive")
    id_field: int = Field(alias="id")
    name: str = Field(alias="name")
    project: DispatchProjectModelsProjectRead = Field(alias="project")
    
    class Config:
        populate_by_name = True


class TagTypeUpdate(BaseModel):
    """TagTypeUpdate schema from the OpenAPI specification."""
    description: str = Field(alias="description")
    exclusive: bool = Field(alias="exclusive")
    id_field: int = Field(alias="id")
    name: str = Field(alias="name")
    
    class Config:
        populate_by_name = True


class TagUpdate(BaseModel):
    """TagUpdate schema from the OpenAPI specification."""
    description: str = Field(alias="description")
    discoverable: bool = Field(alias="discoverable")
    external_id: str = Field(alias="external_id")
    id_field: int = Field(alias="id")
    name: str = Field(alias="name")
    source: str = Field(alias="source")
    tag_type: TagTypeUpdate = Field(alias="tag_type")
    uri: str = Field(alias="uri")
    
    class Config:
        populate_by_name = True


class TaskCreate(BaseModel):
    """TaskCreate schema from the OpenAPI specification."""
    assignees: List[ParticipantUpdate] = Field(alias="assignees")
    created_at: str = Field(alias="created_at")
    creator: ParticipantUpdate = Field(alias="creator")
    description: str = Field(alias="description")
    incident: IncidentReadMinimal = Field(alias="incident")
    owner: ParticipantUpdate = Field(alias="owner")
    priority: str = Field(alias="priority")
    resolve_by: str = Field(alias="resolve_by")
    resolved_at: str = Field(alias="resolved_at")
    resource_id: str = Field(alias="resource_id")
    resource_type: str = Field(alias="resource_type")
    source: str = Field(alias="source")
    status: Any = Field(alias="status")
    updated_at: str = Field(alias="updated_at")
    weblink: str = Field(alias="weblink")
    
    class Config:
        populate_by_name = True


class TaskUpdate(BaseModel):
    """TaskUpdate schema from the OpenAPI specification."""
    assignees: List[ParticipantUpdate] = Field(alias="assignees")
    created_at: str = Field(alias="created_at")
    creator: ParticipantUpdate = Field(alias="creator")
    description: str = Field(alias="description")
    incident: IncidentReadMinimal = Field(alias="incident")
    owner: ParticipantUpdate = Field(alias="owner")
    priority: str = Field(alias="priority")
    resolve_by: str = Field(alias="resolve_by")
    resolved_at: str = Field(alias="resolved_at")
    resource_id: str = Field(alias="resource_id")
    resource_type: str = Field(alias="resource_type")
    source: str = Field(alias="source")
    status: Any = Field(alias="status")
    updated_at: str = Field(alias="updated_at")
    weblink: str = Field(alias="weblink")
    
    class Config:
        populate_by_name = True


class TeamContactCreate(BaseModel):
    """TeamContactCreate schema from the OpenAPI specification."""
    company: str = Field(alias="company")
    contact_type: str = Field(alias="contact_type")
    email: str = Field(alias="email")
    evergreen: bool = Field(alias="evergreen")
    evergreen_last_reminder_at: str = Field(alias="evergreen_last_reminder_at")
    evergreen_owner: str = Field(alias="evergreen_owner")
    evergreen_reminder_interval: int = Field(alias="evergreen_reminder_interval")
    filters: List[SearchFilterRead] = Field(alias="filters")
    is_active: bool = Field(alias="is_active")
    is_external: bool = Field(alias="is_external")
    name: str = Field(alias="name")
    notes: str = Field(alias="notes")
    owner: str = Field(alias="owner")
    project: DispatchProjectModelsProjectRead = Field(alias="project")
    
    class Config:
        populate_by_name = True


class TeamContactRead(BaseModel):
    """TeamContactRead schema from the OpenAPI specification."""
    company: str = Field(alias="company")
    contact_type: str = Field(alias="contact_type")
    created_at: str = Field(alias="created_at")
    email: str = Field(alias="email")
    evergreen: bool = Field(alias="evergreen")
    evergreen_last_reminder_at: str = Field(alias="evergreen_last_reminder_at")
    evergreen_owner: str = Field(alias="evergreen_owner")
    evergreen_reminder_interval: int = Field(alias="evergreen_reminder_interval")
    filters: List[SearchFilterRead] = Field(alias="filters")
    id_field: int = Field(alias="id")
    is_active: bool = Field(alias="is_active")
    is_external: bool = Field(alias="is_external")
    name: str = Field(alias="name")
    notes: str = Field(alias="notes")
    owner: str = Field(alias="owner")
    updated_at: str = Field(alias="updated_at")
    
    class Config:
        populate_by_name = True


class TeamContactUpdate(BaseModel):
    """TeamContactUpdate schema from the OpenAPI specification."""
    company: str = Field(alias="company")
    contact_type: str = Field(alias="contact_type")
    email: str = Field(alias="email")
    evergreen: bool = Field(alias="evergreen")
    evergreen_last_reminder_at: str = Field(alias="evergreen_last_reminder_at")
    evergreen_owner: str = Field(alias="evergreen_owner")
    evergreen_reminder_interval: int = Field(alias="evergreen_reminder_interval")
    filters: List[SearchFilterRead] = Field(alias="filters")
    is_active: bool = Field(alias="is_active")
    is_external: bool = Field(alias="is_external")
    name: str = Field(alias="name")
    notes: str = Field(alias="notes")
    owner: str = Field(alias="owner")
    
    class Config:
        populate_by_name = True


class TeamPagination(BaseModel):
    """TeamPagination schema from the OpenAPI specification."""
    items: List[TeamContactRead] = Field(alias="items")
    total: int = Field(alias="total")
    
    class Config:
        populate_by_name = True


class TermCreate(BaseModel):
    """TermCreate schema from the OpenAPI specification."""
    definitions: List[DefinitionRead] = Field(alias="definitions")
    discoverable: bool = Field(alias="discoverable")
    id_field: int = Field(alias="id")
    project: DispatchProjectModelsProjectRead = Field(alias="project")
    text: str = Field(alias="text")
    
    class Config:
        populate_by_name = True


class TermPagination(BaseModel):
    """TermPagination schema from the OpenAPI specification."""
    items: List[TermRead] = Field(alias="items")
    total: int = Field(alias="total")
    
    class Config:
        populate_by_name = True


class TermRead(BaseModel):
    """TermRead schema from the OpenAPI specification."""
    definitions: List[DefinitionRead] = Field(alias="definitions")
    discoverable: bool = Field(alias="discoverable")
    id_field: int = Field(alias="id")
    text: str = Field(alias="text")
    
    class Config:
        populate_by_name = True


class TermUpdate(BaseModel):
    """TermUpdate schema from the OpenAPI specification."""
    definitions: List[DefinitionRead] = Field(alias="definitions")
    discoverable: bool = Field(alias="discoverable")
    id_field: int = Field(alias="id")
    text: str = Field(alias="text")
    
    class Config:
        populate_by_name = True


class TicketRead(BaseModel):
    """TicketRead schema from the OpenAPI specification."""
    description: str = Field(alias="description")
    resource_id: str = Field(alias="resource_id")
    resource_type: str = Field(alias="resource_type")
    weblink: str = Field(alias="weblink")
    
    class Config:
        populate_by_name = True


class UserLogin(BaseModel):
    """UserLogin schema from the OpenAPI specification."""
    email: str = Field(alias="email")
    organizations: List[UserOrganization] = Field(alias="organizations")
    password: str = Field(alias="password")
    projects: List[UserProject] = Field(alias="projects")
    
    class Config:
        populate_by_name = True


class UserLoginResponse(BaseModel):
    """UserLoginResponse schema from the OpenAPI specification."""
    projects: List[UserProject] = Field(alias="projects")
    token: str = Field(alias="token")
    
    class Config:
        populate_by_name = True


class UserOrganization(BaseModel):
    """UserOrganization schema from the OpenAPI specification."""
    default: bool = Field(alias="default")
    organization: OrganizationRead = Field(alias="organization")
    role: str = Field(alias="role")
    
    class Config:
        populate_by_name = True


class UserPagination(BaseModel):
    """UserPagination schema from the OpenAPI specification."""
    items: List[UserRead] = Field(alias="items")
    total: int = Field(alias="total")
    
    class Config:
        populate_by_name = True


class UserProject(BaseModel):
    """UserProject schema from the OpenAPI specification."""
    default: bool = Field(alias="default")
    project: DispatchProjectModelsProjectRead = Field(alias="project")
    role: str = Field(alias="role")
    
    class Config:
        populate_by_name = True


class UserRead(BaseModel):
    """UserRead schema from the OpenAPI specification."""
    email: str = Field(alias="email")
    id_field: int = Field(alias="id")
    organizations: List[UserOrganization] = Field(alias="organizations")
    projects: List[UserProject] = Field(alias="projects")
    role: str = Field(alias="role")
    
    class Config:
        populate_by_name = True


class UserRegister(BaseModel):
    """UserRegister schema from the OpenAPI specification."""
    email: str = Field(alias="email")
    organizations: List[UserOrganization] = Field(alias="organizations")
    password: str = Field(alias="password")
    projects: List[UserProject] = Field(alias="projects")
    
    class Config:
        populate_by_name = True


class UserRegisterResponse(BaseModel):
    """UserRegisterResponse schema from the OpenAPI specification."""
    token: str = Field(alias="token")
    
    class Config:
        populate_by_name = True


class UserUpdate(BaseModel):
    """UserUpdate schema from the OpenAPI specification."""
    id_field: int = Field(alias="id")
    organizations: List[UserOrganization] = Field(alias="organizations")
    password: str = Field(alias="password")
    projects: List[UserProject] = Field(alias="projects")
    role: str = Field(alias="role")
    
    class Config:
        populate_by_name = True


class ValidationError(BaseModel):
    """ValidationError schema from the OpenAPI specification."""
    loc: List[str] = Field(alias="loc")
    msg: str = Field(alias="msg")
    type_field: str = Field(alias="type")
    
    class Config:
        populate_by_name = True


class WorkflowCase(BaseModel):
    """WorkflowCase schema from the OpenAPI specification."""
    id_field: int = Field(alias="id")
    name: str = Field(alias="name")
    
    class Config:
        populate_by_name = True


class WorkflowCreate(BaseModel):
    """WorkflowCreate schema from the OpenAPI specification."""
    created_at: str = Field(alias="created_at")
    description: str = Field(alias="description")
    enabled: bool = Field(alias="enabled")
    name: str = Field(alias="name")
    parameters: List[Dict[str, Any]] = Field(alias="parameters")
    plugin_instance: PluginInstanceRead = Field(alias="plugin_instance")
    project: DispatchProjectModelsProjectRead = Field(alias="project")
    resource_id: str = Field(alias="resource_id")
    updated_at: str = Field(alias="updated_at")
    
    class Config:
        populate_by_name = True


class WorkflowIncident(BaseModel):
    """WorkflowIncident schema from the OpenAPI specification."""
    id_field: int = Field(alias="id")
    name: str = Field(alias="name")
    
    class Config:
        populate_by_name = True


class WorkflowInstanceCreate(BaseModel):
    """WorkflowInstanceCreate schema from the OpenAPI specification."""
    artifacts: List[DocumentCreate] = Field(alias="artifacts")
    case: WorkflowCase = Field(alias="case")
    created_at: str = Field(alias="created_at")
    creator: ParticipantRead = Field(alias="creator")
    incident: WorkflowIncident = Field(alias="incident")
    parameters: List[Dict[str, Any]] = Field(alias="parameters")
    resource_id: str = Field(alias="resource_id")
    resource_type: str = Field(alias="resource_type")
    run_reason: str = Field(alias="run_reason")
    signal: WorkflowSignal = Field(alias="signal")
    status: str = Field(alias="status")  # An enumeration.
    updated_at: str = Field(alias="updated_at")
    weblink: str = Field(alias="weblink")
    
    class Config:
        populate_by_name = True


class WorkflowInstanceRead(BaseModel):
    """WorkflowInstanceRead schema from the OpenAPI specification."""
    artifacts: List[DocumentCreate] = Field(alias="artifacts")
    case: WorkflowCase = Field(alias="case")
    created_at: str = Field(alias="created_at")
    creator: ParticipantRead = Field(alias="creator")
    id_field: int = Field(alias="id")
    incident: WorkflowIncident = Field(alias="incident")
    parameters: List[Dict[str, Any]] = Field(alias="parameters")
    resource_id: str = Field(alias="resource_id")
    resource_type: str = Field(alias="resource_type")
    run_reason: str = Field(alias="run_reason")
    signal: WorkflowSignal = Field(alias="signal")
    status: str = Field(alias="status")  # An enumeration.
    updated_at: str = Field(alias="updated_at")
    weblink: str = Field(alias="weblink")
    workflow: WorkflowRead = Field(alias="workflow")
    
    class Config:
        populate_by_name = True


class WorkflowPagination(BaseModel):
    """WorkflowPagination schema from the OpenAPI specification."""
    items: List[WorkflowRead] = Field(alias="items")
    total: int = Field(alias="total")
    
    class Config:
        populate_by_name = True


class WorkflowRead(BaseModel):
    """WorkflowRead schema from the OpenAPI specification."""
    created_at: str = Field(alias="created_at")
    description: str = Field(alias="description")
    enabled: bool = Field(alias="enabled")
    id_field: int = Field(alias="id")
    name: str = Field(alias="name")
    parameters: List[Dict[str, Any]] = Field(alias="parameters")
    plugin_instance: PluginInstanceRead = Field(alias="plugin_instance")
    resource_id: str = Field(alias="resource_id")
    updated_at: str = Field(alias="updated_at")
    
    class Config:
        populate_by_name = True


class WorkflowSignal(BaseModel):
    """WorkflowSignal schema from the OpenAPI specification."""
    id_field: int = Field(alias="id")
    name: str = Field(alias="name")
    
    class Config:
        populate_by_name = True


class WorkflowUpdate(BaseModel):
    """WorkflowUpdate schema from the OpenAPI specification."""
    created_at: str = Field(alias="created_at")
    description: str = Field(alias="description")
    enabled: bool = Field(alias="enabled")
    id_field: int = Field(alias="id")
    name: str = Field(alias="name")
    parameters: List[Dict[str, Any]] = Field(alias="parameters")
    plugin_instance: PluginInstanceRead = Field(alias="plugin_instance")
    resource_id: str = Field(alias="resource_id")
    updated_at: str = Field(alias="updated_at")
    
    class Config:
        populate_by_name = True


class DispatchCaseModelsCaseRead(BaseModel):
    """DispatchCaseModelsCaseRead schema from the OpenAPI specification."""
    assignee: ParticipantRead = Field(alias="assignee")
    case_priority: CasePriorityRead = Field(alias="case_priority")
    case_severity: CaseSeverityRead = Field(alias="case_severity")
    case_type: CaseTypeRead = Field(alias="case_type")
    closed_at: str = Field(alias="closed_at")
    created_at: str = Field(alias="created_at")
    description: str = Field(alias="description")
    documents: List[DocumentRead] = Field(alias="documents")
    duplicates: List[CaseReadMinimal] = Field(alias="duplicates")
    escalated_at: str = Field(alias="escalated_at")
    events: List[EventRead] = Field(alias="events")
    groups: List[GroupRead] = Field(alias="groups")
    id_field: int = Field(alias="id")
    incidents: List[IncidentReadMinimal] = Field(alias="incidents")
    name: str = Field(alias="name")
    participants: List[ParticipantRead] = Field(alias="participants")
    project: DispatchCaseModelsProjectRead = Field(alias="project")
    related: List[CaseReadMinimal] = Field(alias="related")
    reported_at: str = Field(alias="reported_at")
    resolution: str = Field(alias="resolution")
    resolution_reason: str = Field(alias="resolution_reason")  # An enumeration.
    signal_instances: List[DispatchCaseModelsSignalInstanceRead] = Field(alias="signal_instances")
    status: str = Field(alias="status")  # An enumeration.
    storage: StorageRead = Field(alias="storage")
    tags: List[TagRead] = Field(alias="tags")
    ticket: TicketRead = Field(alias="ticket")
    title: str = Field(alias="title")
    triage_at: str = Field(alias="triage_at")
    visibility: str = Field(alias="visibility")  # An enumeration.
    workflow_instances: List[WorkflowInstanceRead] = Field(alias="workflow_instances")
    
    class Config:
        populate_by_name = True


class DispatchCaseModelsProjectRead(BaseModel):
    """DispatchCaseModelsProjectRead schema from the OpenAPI specification."""
    color: str = Field(alias="color")
    id_field: int = Field(alias="id")
    name: str = Field(alias="name")
    
    class Config:
        populate_by_name = True


class DispatchCaseModelsSignalInstanceRead(BaseModel):
    """DispatchCaseModelsSignalInstanceRead schema from the OpenAPI specification."""
    created_at: str = Field(alias="created_at")
    entities: List[EntityRead] = Field(alias="entities")
    fingerprint: str = Field(alias="fingerprint")
    raw: Any = Field(alias="raw")
    signal: DispatchCaseModelsSignalRead = Field(alias="signal")
    tags: List[TagRead] = Field(alias="tags")
    
    class Config:
        populate_by_name = True


class DispatchCaseModelsSignalRead(BaseModel):
    """DispatchCaseModelsSignalRead schema from the OpenAPI specification."""
    description: str = Field(alias="description")
    external_id: str = Field(alias="external_id")
    external_url: str = Field(alias="external_url")
    id_field: int = Field(alias="id")
    name: str = Field(alias="name")
    owner: str = Field(alias="owner")
    variant: str = Field(alias="variant")
    workflow_instances: List[WorkflowInstanceRead] = Field(alias="workflow_instances")
    
    class Config:
        populate_by_name = True


class DispatchCaseTypeModelsDocument(BaseModel):
    """DispatchCaseTypeModelsDocument schema from the OpenAPI specification."""
    description: str = Field(alias="description")
    id_field: int = Field(alias="id")
    name: str = Field(alias="name")
    resource_id: str = Field(alias="resource_id")
    resource_type: str = Field(alias="resource_type")
    weblink: str = Field(alias="weblink")
    
    class Config:
        populate_by_name = True


class DispatchCaseTypeModelsService(BaseModel):
    """DispatchCaseTypeModelsService schema from the OpenAPI specification."""
    description: str = Field(alias="description")
    external_id: str = Field(alias="external_id")
    id_field: int = Field(alias="id")
    is_active: bool = Field(alias="is_active")
    name: str = Field(alias="name")
    type_field: str = Field(alias="type")
    
    class Config:
        populate_by_name = True


class DispatchIncidentModelsCaseRead(BaseModel):
    """DispatchIncidentModelsCaseRead schema from the OpenAPI specification."""
    id_field: int = Field(alias="id")
    name: str = Field(alias="name")
    
    class Config:
        populate_by_name = True


class DispatchIncidentModelsProjectRead(BaseModel):
    """DispatchIncidentModelsProjectRead schema from the OpenAPI specification."""
    color: str = Field(alias="color")
    id_field: int = Field(alias="id")
    name: str = Field(alias="name")
    
    class Config:
        populate_by_name = True


class DispatchIncidentModelsTaskRead(BaseModel):
    """DispatchIncidentModelsTaskRead schema from the OpenAPI specification."""
    assignees: List[ParticipantRead] = Field(alias="assignees")
    created_at: str = Field(alias="created_at")
    description: str = Field(alias="description")
    id_field: int = Field(alias="id")
    status: Any = Field(alias="status")
    weblink: str = Field(alias="weblink")
    
    class Config:
        populate_by_name = True


class DispatchIncidentTypeModelsDocument(BaseModel):
    """DispatchIncidentTypeModelsDocument schema from the OpenAPI specification."""
    description: str = Field(alias="description")
    id_field: int = Field(alias="id")
    name: str = Field(alias="name")
    resource_id: str = Field(alias="resource_id")
    resource_type: str = Field(alias="resource_type")
    weblink: str = Field(alias="weblink")
    
    class Config:
        populate_by_name = True


class DispatchProjectModelsProjectRead(BaseModel):
    """DispatchProjectModelsProjectRead schema from the OpenAPI specification."""
    annual_employee_cost: int = Field(alias="annual_employee_cost")
    business_year_hours: int = Field(alias="business_year_hours")
    color: str = Field(alias="color")
    default: bool = Field(alias="default")
    description: str = Field(alias="description")
    id_field: int = Field(alias="id")
    name: str = Field(alias="name")
    owner_conversation: str = Field(alias="owner_conversation")
    owner_email: str = Field(alias="owner_email")
    
    class Config:
        populate_by_name = True


class DispatchSignalModelsService(BaseModel):
    """DispatchSignalModelsService schema from the OpenAPI specification."""
    description: str = Field(alias="description")
    external_id: str = Field(alias="external_id")
    id_field: int = Field(alias="id")
    is_active: bool = Field(alias="is_active")
    name: str = Field(alias="name")
    type_field: str = Field(alias="type")
    
    class Config:
        populate_by_name = True


class DispatchSignalModelsSignalInstanceRead(BaseModel):
    """DispatchSignalModelsSignalInstanceRead schema from the OpenAPI specification."""
    case: DispatchCaseModelsCaseRead = Field(alias="case")
    created_at: str = Field(alias="created_at")
    entities: List[EntityRead] = Field(alias="entities")
    filter_action: str = Field(alias="filter_action")  # An enumeration.
    fingerprint: str = Field(alias="fingerprint")
    id_field: str = Field(alias="id")
    project: DispatchProjectModelsProjectRead = Field(alias="project")
    raw: Dict[str, Any] = Field(alias="raw")
    signal: DispatchSignalModelsSignalRead = Field(alias="signal")
    
    class Config:
        populate_by_name = True


class DispatchSignalModelsSignalRead(BaseModel):
    """DispatchSignalModelsSignalRead schema from the OpenAPI specification."""
    case_priority: CasePriorityRead = Field(alias="case_priority")
    case_type: CaseTypeRead = Field(alias="case_type")
    conversation_target: str = Field(alias="conversation_target")
    create_case: bool = Field(alias="create_case")
    created_at: str = Field(alias="created_at")
    description: str = Field(alias="description")
    enabled: bool = Field(alias="enabled")
    entity_types: List[EntityTypeRead] = Field(alias="entity_types")
    external_id: str = Field(alias="external_id")
    external_url: str = Field(alias="external_url")
    filters: List[SignalFilterRead] = Field(alias="filters")
    id_field: int = Field(alias="id")
    name: str = Field(alias="name")
    oncall_service: DispatchSignalModelsService = Field(alias="oncall_service")
    owner: str = Field(alias="owner")
    project: DispatchProjectModelsProjectRead = Field(alias="project")
    source: SourceBase = Field(alias="source")
    tags: List[TagRead] = Field(alias="tags")
    variant: str = Field(alias="variant")
    workflows: List[WorkflowRead] = Field(alias="workflows")
    
    class Config:
        populate_by_name = True


class DispatchTaskModelsTaskRead(BaseModel):
    """DispatchTaskModelsTaskRead schema from the OpenAPI specification."""
    assignees: List[ParticipantRead] = Field(alias="assignees")
    created_at: str = Field(alias="created_at")
    creator: ParticipantRead = Field(alias="creator")
    description: str = Field(alias="description")
    id_field: int = Field(alias="id")
    incident: IncidentReadMinimal = Field(alias="incident")
    owner: ParticipantRead = Field(alias="owner")
    priority: str = Field(alias="priority")
    project: DispatchProjectModelsProjectRead = Field(alias="project")
    resolve_by: str = Field(alias="resolve_by")
    resolved_at: str = Field(alias="resolved_at")
    resource_id: str = Field(alias="resource_id")
    resource_type: str = Field(alias="resource_type")
    source: str = Field(alias="source")
    status: Any = Field(alias="status")
    updated_at: str = Field(alias="updated_at")
    weblink: str = Field(alias="weblink")
    
    class Config:
        populate_by_name = True
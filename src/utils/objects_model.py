class DataResponse():
    
    message: str = ""
    errors:dict | list = {}
    data:dict | list = {}
    status: int = 200
    
    
class MessagesUsersServices:
    ERROR_CREATE_USER = "Error creating user"
    ERROR_VALIDATE_CREATE_USER = "Error validating data to create user"
    CREATION_USER = "User created successfully"
    CORRECT_LOGIN = "Successful Login"
    CREDENTIALS_INVALID = "Invalid credentials"
    ERROR_LOGIN = "Error trying to access the application"
    USER_NOT_FOUND = "User not found"
    USER_DETAIL_NOT_FOUND = "There is no user with that ID."
    CORRECT_RETURN_DATA_USER = "User information obtained successfully"
    ERROR_DETAIL_USER = "Error returning user information"
    
    
class MessagesRolesServices:
    NOT_SEARCH_DATA_ROLE = "Role not found"
    RETURN_DATA_LIST_ROLE = "Role data returned successfully"
    ERROR_DATA_LIST_ROLE = "Error returning role data"
    ERROR_CREATE_VALIDATE = "Data validation error for role creation"
    CREATION_ROLE = "Role created successfully"
    ERROR_UPDATE_VALIDATE = "Data validation error for role updated"
    RETURN_DELETE_ROLE = "Role Successfully Deleted"
    
class MessagesEventsServices:
    NOT_SEARCH_DATA_EVENT = "Event not found"
    RETURN_DATA_LIST_EVENT = "Event data returned successfully"
    ERROR_DATA_LIST_EVENT = "Error returning event data"
    ERROR_CREATE_VALIDATE = "Data validation error for event creation"
    CREATION_EVENT = "Event created successfully"
    ERROR_UPDATE_VALIDATE = "Data validation error for event updated"
    RETURN_DELETE_EVENT = "Event Successfully Deleted"
    FIELDS_REQUIRED_EVENT = "Missing required fields"
    ACCESS_DENIED = "You do not have permission to delete this event"
    
    
class MessagesSessionServices:
    NOT_SEARCH_DATA_SESSION = "Session not found"
    RETURN_DATA_LIST_SESSION = "Session data returned successfully"
    ERROR_DATA_LIST_SESSION = "Error returning session data"
    ERROR_CREATION_SESSION = "Error creation session"
    ERROR_UPDATE_SESSION = "Error update session"
    ERROR_CREATE_VALIDATE = "Data validation error for session creation"
    CREATION_SESSION = "Session created successfully"
    UPDATED_SESSION = "Session updated successfully"
    ERROR_UPDATE_VALIDATE = "Data validation error for session updated"
    RETURN_DELETE_SESSION = "Session Successfully Deleted"
    ERROR_DELETE_SESSION = "Error deleting session"
    CONFLICT_SESSIONS = "Cannot create session, A session with the same schedule already exists"
    EXCEEDS_CAPACITY_SESSION = "Session capacity exceeds event capacity"
    
class MessagesRegistrationServices:
    EVENT_NOT_FOUND = "Event not found",
    OVERLOAD_EVENT = "Event capacity reached",
    EXIST_REGISTRED_EVENT = "You are already registered for this event",
    CREATION_REGISTRED_EVENT = "Event registration successful",
    FAILED_REGISTRED_EVENT = "Event registration failed"
    ERROR_CREATE_VALIDATE = "Data validation error for registration creation"
    RECOREDED_EVENTS = "Recorded events"
    ERROR_DATA_LIST_EVENTS = "Error returning events for user data"
    
    
class MessagesRolePermissionServices:
    ERROR_CREATE_VALIDATE = "Data validation error for role and permission association"
    ERROR_DELETE_VALIDATE = "Data validation error for role and permission delete"
    ERROR_ASSOCIATE_ROLE_PERMISSION = "Data validation error for role and permission association"
    NOT_SEARCH_DATA_ROLE = "Role not found"
    NOT_SEARCH_DATA_PERMISSIONS = "Permissions not found:"
    ASSOCIATED_PERMISSIONS = "Successfully associated permissions"
    NOT_DELETE_FOUND = "No relationships were found to delete"
    CORRECT_DELETE ="Relationships successfully deleted"
    
class MessagesUserRoleServices:
    NOT_SEARCH_DATA_ROLE = "Role not found"
    ERROR_CREATE_VALIDATE = "Data validation error for role and users association"
    NOT_SEARCH_DATA_USERS = "Users not found:"
    ASSOCIATED_USERS = "Successfully associated users"
    ERROR_DELETE_VALIDATE = "Data validation error for role and users delete"
    NOT_DELETE_FOUND = "No relationships were found to delete"
    CORRECT_DELETE ="Relationships successfully deleted"
    LIST_ROLES_USERS = "Return list of roles and users"
    ERROR_LIST_ROLES_USERS = "Error listing roles and users"
    
    
    
class Attributes:
    ERROR_ATTRIBUTE = "error"
    NAME_ATTRIBUTE = "name"
    ID_ATTRIBUTE = "id"
    PASSWORD_ATTRIBUTE = "password"  
    EMAIL_ATTRIBUTE = "email"
    EVENT_ID_ATTRIBUTE = "event_id"
    PERMISSIONS_ATTRIBUTE = "permissions"
    USER_ATTRIBUTE = "user"
    
    
class EventAttributes:
    TITLE = "title"
    DESCRIPTION = "description"
    STATUS = "status"
    START_DATE = "start_date"
    END_DATE = "end_date"
    CAPACITY = "capacity"
    CREATED_BY = "created_by"
    
class EventStates:
    PROGRAMMED = "programmed"
    
class MessagesPermissionssServices:
    ACTION_DENIED = "You do not have permission for this action"
    
    
class ValidateDataAttributes:
    EVENTS_ATTRIBUTES = [EventAttributes.TITLE,EventAttributes.DESCRIPTION,EventAttributes.START_DATE ,EventAttributes.END_DATE, EventAttributes.CAPACITY]


class Permissions:
    POST_ROLE_CREATE = "post_role_create"
    POST_EVENT_CREATE = "post_event_create"
    POST_SESSION_CREATE = "post_session_create"
    POST_REGISTRATION_CREATE = "post_registration_create"
    POST_ROLE_PERMISSIONS_CREATE = "post_role_permissions_create"
    POST_ROLE_USERS_CREATE = "post_role_users_create"

    DEL_ROLE_PERMISSIONS_DELETE = "del_role_permissions_delete"
    DEL_ROLE_USERS_DELETE = "del_role_users_delete"

    GET_ROLE = "get_role"
    GET_EVENT = "get_event"
    GET_SESSION = "get_session"

    DEL_ROLE_DELETE = "del_role_delete"
    DEL_EVENT_DELETE = "del_event_delete"
    DEL_SESSION_DELETE = "del_session_delete"

    GET_LIST_ROLES = "get_list_roles"
    GET_LIST_EVENTS = "get_list_events"
    GET_DETAIL_USER = "get_detail_user"
    GET_LIST_SESSIONS = "get_list_sessions"
    GET_LIST_ROLE_USERS = "get_list_role_users"
    GET_LIST_REGISTRATIONS = "get_list_registrations"

    PUT_ROLE_UPDATE = "put_role_update"
    PUT_EVENT_UPDATE = "put_event_update"
    PUT_SESSION_UPDATE = "put_session_update"


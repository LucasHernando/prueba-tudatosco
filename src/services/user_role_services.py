from querys.user_role_query import UserRoleQuerys
from querys.role_query import RoleQuerys
from querys.user_query import UserQuerys
from serializers.requests.user_role_request import UserRoleSchema
from serializers.responses.role_user_responses import UserRoleListSchema
from utils.objects_model import DataResponse, MessagesUserRoleServices, Attributes
from http import HTTPStatus
from marshmallow import ValidationError

class UserRoleServices():
    
    user_role_schema = UserRoleSchema()
    users_roles_schema = UserRoleSchema(many=True)
    user_role_querys = UserRoleQuerys()
    messages = MessagesUserRoleServices()
    
    def service_create_role_users(self, data:dict):
        
        
        data_response = DataResponse()
        
        role_query = RoleQuerys()
        
        try:
            validated_data = self.user_role_schema.load(data)
        except ValidationError as err:
            data_response.status = HTTPStatus.BAD_REQUEST
            data_response.message = self.messages.ERROR_CREATE_VALIDATE
            data_response.errors = err.messages
                 
            return data_response

        role_id = validated_data["role_id"]
        user_ids = validated_data["user_ids"]

        role = role_query.get_role_by_id(role_id=role_id)
        if not role:
            data_response.status = HTTPStatus.NOT_FOUND
            data_response.message = self.messages.NOT_SEARCH_DATA_ROLE
            
            return data_response

        user_query = UserQuerys()
        users = user_query.get_all_list_users(user_ids=user_ids)
        found_ids = [u.id for u in users]
        missing = set(user_ids) - set(found_ids)
        if missing:
            
            data_response.status = HTTPStatus.NOT_FOUND
            data_response.message = f'{self.messages.NOT_SEARCH_DATA_USERS}{list(missing)}'
                 
            return data_response

        created = []
        for uid in user_ids:
            exists = self.user_role_querys.get_first_role_user(user_id=uid, role_id=role_id)
            if not exists:
                user_role = self.user_role_querys.get_object(user_id=uid, role_id=role_id)
                self.user_role_querys.add_values_session(value=user_role)
                created.append(uid)

        self.user_role_querys.add_execute_session()
        data_response.status = HTTPStatus.CREATED
        data_response.message = self.messages.ASSOCIATED_USERS
        data_response.data = created
                
        return data_response
    
    
    def service_delete_role_users(self, data:dict):
        
        data_response = DataResponse()
        
        try:
            validated_data = self.user_role_schema.load(data)
        except ValidationError as err:
            data_response.status = HTTPStatus.BAD_REQUEST
            data_response.message = self.messages.ERROR_DELETE_VALIDATE
                
            return data_response

        role_id = validated_data["role_id"]
        user_ids = validated_data["user_ids"]

        deleted = []
        for uid in user_ids:
            relation = self.user_role_querys.get_first_role_user(role_id=role_id, user_id=uid)
            if relation:
                self.user_role_querys.delete_values_session(value=relation)
                deleted.append(uid)

        self.user_role_querys.add_execute_session()

        if not deleted:
            data_response.status = HTTPStatus.NOT_FOUND
            data_response.message = self.messages.NOT_DELETE_FOUND
                
            return data_response
        
        data_response.status = HTTPStatus.OK
        data_response.message = self.messages.CORRECT_DELETE
        data_response.data = deleted
            
        return data_response
    
    
    def service_get_list_roles_users(self, role_id=None):
        
        #role_id = request.args.get("role_id", type=int)
        data_response = DataResponse()
        
        try:
            if role_id:
                query = self.user_role_querys.get_list_role_users(role_id=role_id)
            else:
                query = self.user_role_querys.get_list_role_users()
            
            
            associations = query

            raw_data = [
                {
                    "role_id": r.role_id,
                    "role_name": r.role_name,
                    "user_id": r.user_id,
                    "user_email": r.user_email
                }
                for r in associations
            ]

            result = UserRoleListSchema(many=True).dump(raw_data)
            data_response.status = HTTPStatus.OK
            data_response.message = self.messages.LIST_ROLES_USERS
            data_response.data = result
        except Exception as ex:
            data_response.status = HTTPStatus.INTERNAL_SERVER_ERROR
            data_response.message = self.messages.ERROR_LIST_ROLES_USERS
            data_response.errors = [{Attributes.ERROR_ATTRIBUTE: str(ex.args)}]
            
                        
        return data_response
    

from querys.role_query import RoleQuerys
from serializers.requests.role_requests import RoleSchema
from utils.objects_model import DataResponse, MessagesRolesServices, Attributes
from http import HTTPStatus

class RoleServices():
    
    role_schema = RoleSchema()
    roles_schema = RoleSchema(many=True)
    role_querys = RoleQuerys()
    messages = MessagesRolesServices()
    
    
    def service_get_roles(self, role_id=None):
        
        data_response = DataResponse()
        
        try:
            if role_id:
                role = self.role_querys.get_role_by_id(role_id)
                if not role:
                    
                    data_response.status = HTTPStatus.BAD_REQUEST
                    data_response.message = self.messages.NOT_SEARCH_DATA_ROLE
                 
                    return data_response
                
                
                data_response.data = dict(self.role_schema.dump(role))
                data_response.status = HTTPStatus.OK
                data_response.message = self.messages.RETURN_DATA_LIST_ROLE
                return data_response
            else:
                roles = self.role_querys.get_all_roles()
                
                
                data_response.data = self.roles_schema.dump(roles)
                data_response.status = HTTPStatus.OK
                data_response.message = self.messages.RETURN_DATA_LIST_ROLE
                
                return data_response
        except Exception as ex:
            data_response.data = []
            data_response.status = HTTPStatus.INTERNAL_SERVER_ERROR
            data_response.message = self.messages.ERROR_DATA_LIST_ROLE
            data_response.errors = [{Attributes.ERROR_ATTRIBUTE: str(ex.args)}]
            
            return data_response
            

    
    def service_create_role(self, data:dict):
        #data = request.get_json()
        
        data_response = DataResponse()
        
        try:
            errors = self.role_schema.validate(data)
            
            if errors:
                data_response.status = HTTPStatus.BAD_REQUEST
                data_response.message = self.messages.ERROR_CREATE_VALIDATE
                data_response.errors = [{Attributes.ERROR_ATTRIBUTE:errors}]
                
                return data_response

            role = self.role_querys.create_role(data[Attributes.NAME_ATTRIBUTE])
            
            
            data_response.data = [{Attributes.ID_ATTRIBUTE: role.id}]
            data_response.status = HTTPStatus.CREATED
            data_response.message = self.messages.CREATION_ROLE
            
            return data_response
        except Exception as ex:
            data_response.data = []
            data_response.status = HTTPStatus.INTERNAL_SERVER_ERROR
            data_response.message = self.messages.ERROR_DATA_LIST_ROLE
            data_response.errors = [{Attributes.ERROR_ATTRIBUTE: str(ex.args)}]
            
            return data_response

    
    def service_update_role(self, role_id:int, data:dict):
        
        data_response = DataResponse()
        
        try:
            role = self.role_querys.get_role_by_id(role_id)
            
            if not role:
                data_response.status = HTTPStatus.NOT_FOUND
                data_response.message = self.messages.NOT_SEARCH_DATA_ROLE
                
                return data_response
            
            #data = request.get_json()
            errors = self.role_schema.validate(data)
            if errors:
                data_response.status = HTTPStatus.BAD_REQUEST
                data_response.message = self.messages.ERROR_UPDATE_VALIDATE
                data_response.errors = [{Attributes.ERROR_ATTRIBUTE:errors}]
                
                return data_response
                
            updated = self.role_querys.update_role(role, data[Attributes.NAME_ATTRIBUTE])
            
            data_response.data = [self.role_schema.dump(updated)]
            data_response.status = HTTPStatus.OK
            data_response.message = self.messages.CREATION_ROLE
        
            return data_response
        except Exception as ex:
            data_response.data = []
            data_response.status = HTTPStatus.INTERNAL_SERVER_ERROR
            data_response.message = self.messages.ERROR_DATA_LIST_ROLE
            data_response.errors = [{Attributes.ERROR_ATTRIBUTE: str(ex.args)}]
            
            return data_response

    
    def service_delete_role(self, role_id:int):
        
        data_response = DataResponse()
        try:        
            role = self.role_querys.get_role_by_id(role_id)
            if not role:
                data_response.status = HTTPStatus.NOT_FOUND
                data_response.message = self.messages.NOT_SEARCH_DATA_ROLE
                return data_response
                    
            self.role_querys.delete_role(role)
            
            data_response.status = HTTPStatus.OK
            data_response.message = self.messages.RETURN_DELETE_ROLE
        
        except Exception as ex:
            data_response.data = []
            data_response.status = HTTPStatus.INTERNAL_SERVER_ERROR
            data_response.message = self.messages.ERROR_DATA_LIST_ROLE
            data_response.errors = [{Attributes.ERROR_ATTRIBUTE: str(ex.args)}]
            
        return data_response



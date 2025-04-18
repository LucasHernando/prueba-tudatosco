from querys.role_permission_query import RolePermissionQuerys
from querys.role_query import RoleQuerys
from querys.permission_query import PermissionQuerys
from serializers.requests.role_permission_request import RolePermissionSchema
from utils.objects_model import DataResponse, MessagesRolePermissionServices, Attributes
from http import HTTPStatus
from marshmallow import ValidationError

class RolePermissionServices():
    
    role_permissions_schema = RolePermissionSchema()
    role_permissions_many = RolePermissionSchema(many=True)
    role_permissions_querys = RolePermissionQuerys()
    messages = MessagesRolePermissionServices()
        
    def service_create_role_permissions(self, data:dict):
        #data = request.get_json()
        
        data_response = DataResponse()
        
        role_query = RoleQuerys()
        
        try:
            #data = request.get_json()
            validated_data = self.role_permissions_schema.load(data)
        except ValidationError as err:
            #return jsonify(err.messages), 400
            data_response.status = HTTPStatus.BAD_REQUEST
            data_response.message = self.messages.ERROR_CREATE_VALIDATE
                 
            return data_response

        role_id = validated_data["role_id"]
        permission_ids = validated_data["permission_ids"]

        # Validar existencia del rol
        role = role_query.get_role_by_id(role_id=role_id)
        if not role:
            #return jsonify({'message': 'Rol no encontrado'}), 404
            data_response.status = HTTPStatus.NOT_FOUND
            data_response.message = self.messages.NOT_SEARCH_DATA_ROLE
                 
            return data_response

        permission_query = PermissionQuerys()
        permissions = permission_query.get_all_list_permissions(permission_ids=permission_ids)
        # Validar existencia de permisos
        #permissions = Permission.query.filter(Permission.id.in_(permission_ids)).all()
        found_ids = [p.id for p in permissions]

        missing = set(permission_ids) - set(found_ids)
        if missing:
            #return jsonify({'message': f'Permisos no encontrados: {list(missing)}'}), 404
            data_response.status = HTTPStatus.NOT_FOUND
            data_response.message = f'{self.messages.NOT_SEARCH_DATA_PERMISSIONS}{list(missing)}'
                 
            return data_response

        created = []
        for perm_id in permission_ids:
            #exists = RolePermission.query.filter_by(role_id=role_id, permission_id=perm_id).first()
            exists = self.role_permissions_querys.get_first_role_permission(role_id=role_id, permission_id=perm_id)
            if not exists:
                #rp = RolePermission(role_id=role_id, permission_id=perm_id)
                rp = self.role_permissions_querys.get_object(role_id=role_id, permission_id=perm_id)
                #db.session.add(rp)
                self.role_permissions_querys.add_values_session(value=rp)
                created.append(perm_id)

        self.role_permissions_querys.add_execute_session()

        #return jsonify({'message': 'Permisos asociados con éxito', 'associated_permissions': created}), 201
        
        data_response.status = HTTPStatus.CREATED
        data_response.message = self.messages.ASSOCIATED_PERMISSIONS
        data_response.data = created
                
        return data_response


        """try:
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
            
            return data_response"""

    
    

    
    def service_delete_role_permissions(self, data:dict):
        
        """data_response = DataResponse()
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
            data_response.errors = [{Attributes.ERROR_ATTRIBUTE: str(ex.args)}]"""
            
        data_response = DataResponse()   
        try:
            #data = request.get_json()
            validated_data = self.role_permissions_schema.load(data)
        except ValidationError as err:
            #return jsonify(err.messages), 400
            data_response.status = HTTPStatus.BAD_REQUEST
            data_response.message = self.messages.ERROR_DELETE_VALIDATE
                
            return data_response

        role_id = validated_data["role_id"]
        permission_ids = validated_data["permission_ids"]

        deleted = []
        for perm_id in permission_ids:
            #rp = RolePermission.query.filter_by(role_id=role_id, permission_id=perm_id).first()
            rp = self.role_permissions_querys.get_first_role_permission(role_id=role_id, permission_id=perm_id)
            if rp:
                #db.session.delete(rp)
                self.role_permissions_querys.delete_values_session(value=rp)
                deleted.append(perm_id)

        #db.session.commit()
        self.role_permissions_querys.add_execute_session()
        
        if not deleted:
            #return jsonify({'message': 'No se encontraron relaciones para eliminar'}), 404
            data_response.status = HTTPStatus.NOT_FOUND
            data_response.message = self.messages.NOT_DELETE_FOUND
                
            return data_response

        #return jsonify({'message': 'Relaciones eliminadas con éxito', 'deleted_permissions': deleted}), 200
        
        
        data_response.status = HTTPStatus.OK
        data_response.message = self.messages.CORRECT_DELETE
        data_response.data = deleted
            
        return data_response



from xtrm_drest import fields as fields
from xtrm_drest import routers as routers
from xtrm_drest import serializers as serializers
from xtrm_drest import viewsets as viewsets

from .models import Group, Permission, User


# DREST

# DREST serializers


class UserSerializer(serializers.DynamicModelSerializer):

    class Meta:
        model = User
        name = 'user'
        fields = ('id', 'name', 'groups')

    groups = fields.DynamicRelationField(
        'GroupSerializer',
        embed=True,
        many=True,
        deferred=True
    )


class GroupSerializer(serializers.DynamicModelSerializer):

    class Meta:
        model = Group
        name = 'group'
        fields = ('id', 'name', 'permissions')

    permissions = fields.DynamicRelationField(
        'PermissionSerializer',
        embed=True,
        many=True,
        deferred=True
    )


class PermissionSerializer(serializers.DynamicModelSerializer):

    class Meta:
        model = Permission
        name = 'permission'
        fields = ('id', 'name')

# DREST views


class UserViewSet(viewsets.DynamicModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# DREST router

router = routers.DynamicRouter()
router.register(r'drest/users', UserViewSet)

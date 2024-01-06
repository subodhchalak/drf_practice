from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User



#---------------------------------------------------------------------------
#                            TokenSerializer
#---------------------------------------------------------------------------

class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = (
            'key',
        )


#-------------------------------------------------------------------------------
#                            UserRegistrationSerialzier
#-------------------------------------------------------------------------------

class UserRegistrationSerialzier(serializers.ModelSerializer):
    password2 = serializers.CharField(
        style = {'input_type': 'password'},
        write_only = True
    )
    
    extras = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'email',
            'password',
            'password2',
            'auth_token',
            'extras'
        )
        extra_kwargs = {
            'password': {'write_only': True},
            'password2': {'write_only': True},
        }
        required_fields = (
            'username',
            'email',
            'password',
            'password2'
        )
        read_only_fields = (
            'id',
            'auth_token',
            'extras'
        )

    def get_extras(self, obj):
        return "This is a extras field"

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        auth_token = instance.auth_token.key if instance.auth_token else None
        representation['auth_token'] = auth_token
        return representation
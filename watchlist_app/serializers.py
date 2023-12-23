from rest_framework import serializers
from watchlist_app.models import Watchlist


#---------------------------------------------------------------------------
#                            SECTION HEADER
#---------------------------------------------------------------------------


class WatchlistSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only = True)
    name = serializers.CharField(required=False)
    description = serializers.CharField(required=False)
    is_active = serializers.BooleanField(required=False)
    created_at = serializers.DateTimeField(required=False, read_only=True)
    updated_at = serializers.DateTimeField(required=False, read_only=True)

    def create(self, validated_data):
        return Watchlist.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.is_active = validated_data.get('is_active', instance.is_active)
        instance.save()
        return instance
    
    def validate(self, data):
        errors = {}
        if 'name' in data and len(data['name']) < 2:
            errors['name'] = "Name must contain at least one character."

        if 'name' in data and 'description' in data:
            if data['name'] == data['description']:
                errors['description'] = "Description should not be equal to name."
        
        if len(errors) > 0:
            raise serializers.ValidationError(detail=errors)
            
        return data
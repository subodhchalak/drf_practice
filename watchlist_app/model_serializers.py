from rest_framework import serializers
from django.utils import timezone

from watchlist_app.models import (
    Platform,
    Watchlist
)




#---------------------------------------------------------------------------
#                            WatchlistSerializer
#---------------------------------------------------------------------------


class WatchlistSerializer(serializers.ModelSerializer):
    days_since_created = serializers.SerializerMethodField()
    class Meta:
        model = Watchlist
        fields = (
            'id',
            'name',
            'description',
            'platform',
            'is_active',
            'created_at',
            'updated_at',
            'days_since_created'
        )

        read_only_fields = (
            'id',
            'created_at',
            'updated_at'
        )

        required_fields = (
            'name',
            'description',
            'is_active'
        )
        extra_kwargs = {}

        for field in required_fields:
            extra_kwargs[field] = {
                'required': True,
                'allow_null': False
            }

    def get_days_since_created(self, object):
        return (timezone.now() - object.created_at).days
    
    # def to_representation(self, instance):
    #     self.fields['platform'] = PlatformSerializer(many=False)
    #     return super(self.__class__, self).to_representation(instance)


#---------------------------------------------------------------------------
#                            PlatformSerializer
#---------------------------------------------------------------------------


class PlatformSerializer(serializers.ModelSerializer):
    watchlist = serializers.PrimaryKeyRelatedField(
        many = True,
        read_only = True
    )
    class Meta:
        model = Platform
        fields = (
            'id',
            'name',
            'description',
            'created_at',
            'updated_at',
            'watchlist',
        )

    # def to_representation(self, instance):
    #     self.fields['watchlist'] = WatchlistSerializer(many=True)
    #     return super(PlatformSerializer, self).to_representation(instance)

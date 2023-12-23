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

        field_map = {
            'name': 'Movie Name'
        }

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
    
    def to_representation(self, instance):
        return super().to_representation(instance)
    
    # def update(self, instance, validated_data):
    #     instance.name = validated_data.get('name', instance.name)
    #     instance.name = validated_data.get('name', instance.description)
    #     instance.active = validated_data.get('is_active', instance.is_active)
    #     instance.save()
    #     return instance


#---------------------------------------------------------------------------
#                            PlatformSerializer
#---------------------------------------------------------------------------


class PlatformSerializer(serializers.ModelSerializer):
    watchlist = WatchlistSerializer(many=True)
        

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
 

    def create(self, validated_data):
        watchlist_data = validated_data.pop('watchlist')

        platform = Platform.objects.create(
            **validated_data
        )

        print(f"create watchlist_data: {watchlist_data}")
        for wl in watchlist_data:
            watch = Watchlist.objects.filter(name = wl['name'])
            if len(watch) > 0:
                continue
            Watchlist.objects.create(
                platform = platform,
                ** wl
            )
        return platform
    
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get(
            'name',
            instance.name
        )
        instance.description = validated_data.get(
            'description',
            instance.description
        )
        instance.save()

        watchlist_data = validated_data.pop('watchlist')
        watchlists = instance.watchlist.all()
        new_watch = []
       
        for wl in watchlist_data:
            try:
                watchlist = Watchlist.objects.filter(
                    platform = instance,
                    name = wl['name']
                )
                if watchlist:
                    for w in watchlist: 
                        w.name = wl.get('name', w.name)
                        w.description = wl.get('description', w.description)
                        w.is_active = wl.get('is_active', w.is_active)
                        w.save()
                        new_watch.append(w.id)
                else:
                    watch = Watchlist.objects.create(
                        name = wl['name'],
                        description = wl['description'],
                        is_active = wl['is_active'],
                        platform = instance
                    )
                    watch.save()
                    new_watch.append(watch.id)
            except Exception as e:
                raise serializers.ValidationError(str(e))

        for item in watchlists:
            if item.id not in new_watch:
                item.delete()

        return instance
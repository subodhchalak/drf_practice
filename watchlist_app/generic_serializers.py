from rest_framework import serializers

from watchlist_app.models import (
    Watchlist,
    Platform,
    Review
)


#---------------------------------------------------------------------------
#                            WatchlistSerializer
#---------------------------------------------------------------------------


class WatchlistSerializer(serializers.ModelSerializer):
    # platform = serializers.HyperlinkedIdentityField(
    #     many = False,
    #     read_only = True,
    #     view_name = 'platform_detail'
    # )

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
            'review'
        )

        read_only_fields = (
            'id',
            'created_at',
            'updated_at',
            'review'
        )

    def create(self, validated_data):
        name = validated_data['name']
        watchlists = Watchlist.objects.filter(name__iexact = name)
        if len(watchlists) > 0:
            raise serializers.ValidationError(
                "Watchlist with the given name already present."
            )
        else:
            watchlist = Watchlist.objects.create(**validated_data)
            return watchlist


#---------------------------------------------------------------------------
#                            PlatformSerializer
#---------------------------------------------------------------------------


class PlatformSerializer(serializers.ModelSerializer):
    watchlist = serializers.HyperlinkedRelatedField(
        many = True,
        read_only = True,
        view_name = 'watchlist_detail'
    )

    class Meta:
        model = Platform
        fields = (
            'id',
            'name',
            'description',
            'created_at',
            'updated_at',
            'watchlist'
        )

    def to_representation(self, instance):
        self.fields['watchlist'] = WatchlistSerializer(
            many = True,
            read_only = True
        )
        return super().to_representation(instance)


#---------------------------------------------------------------------------
#                            ReviewSerializer
#---------------------------------------------------------------------------


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = (
            'id',
            'reviewer',
            'rating',
            'description',
            'is_active',
            'created_at',
            'updated_at',
            'watchlist'
        )

        read_only_fields = (
            'id',
            'watchlist'
        )
    
    def to_representation(self, instance):
        self.fields['watchlist'] = WatchlistSerializer(
            many = False,
            read_only = True
        )
        return super().to_representation(instance)
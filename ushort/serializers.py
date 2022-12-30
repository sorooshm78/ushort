from rest_framework import serializers

from .models import UrlShort


class UrlShortModelSerializer(serializers.ModelSerializer):
    short_url = serializers.HyperlinkedIdentityField(
        view_name="redirect_url",
        lookup_field="hash",
    )

    class Meta:
        model = UrlShort
        fields = [
            "url",
            "short_url",
        ]

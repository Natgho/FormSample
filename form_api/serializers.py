from rest_framework import serializers
from .models import Consent


class ConsentListSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()

    class Meta:
        model = Consent
        fields = ["id", "english_title", "french_title", ]


class ConsentPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consent
        fields = "__all__"

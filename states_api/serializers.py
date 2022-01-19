from rest_framework import serializers

from states_api.models import *


class DeputyGovernorSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeputyGovernor
        fields = "__all__"


class GovernorSerializer(serializers.ModelSerializer):
    deputy_governors = DeputyGovernorSerializer(many=False, required=False, read_only=True)

    class Meta:
        model = Governor
        fields = "__all__"


class NigerianStateSerializer(serializers.ModelSerializer):
    governors = GovernorSerializer(many=False, required=False, read_only=True)

    class Meta:
        model = NigerianState
        fields = "__all__"





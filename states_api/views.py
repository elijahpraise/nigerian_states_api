from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from states_api.serializers import *
from states_api.models import *


class NigerianStateView(generics.CreateAPIView):

    def post(self, request, *args, **kwargs):
        name_of_state = request.data.get("name_of_state")
        for states in NigerianState.objects.all():
            if states.name_of_state == name_of_state:
                print(name_of_state, 'yes this is it................................')
                governor_of_that_state = Governor.objects.get(state_id=states.pk)
                print(governor_of_that_state, "making progress...............................")
                name = GovernorSerializer(governor_of_that_state).data.get('name', None)
                deputy = DeputyGovernorSerializer(DeputyGovernor.objects.get(state_id=states.pk)).data.get('name', None)
                state = NigerianStateSerializer(states).data.get('name_of_state', None)
                return Response({"Name": name, "Name of State": f"{state} State", "Deputy Governor": deputy})
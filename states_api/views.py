from django.urls import include
from rest_framework import generics
from rest_framework.response import Response

from states_api.serializers import *
from states_api.models import *


class NigerianStateView(generics.CreateAPIView):

    def post(self, request, *args, **kwargs):
        name_of_state = request.data.get('name_of_state').capitalize()
        filtered_state = NigerianState.objects.filter(name_of_state=name_of_state)
        if filtered_state:
            state = filtered_state.get(name_of_state=name_of_state)
            name = GovernorSerializer(Governor.objects.get(state_id=state.pk)).data.get('name')
            deputy = DeputyGovernorSerializer(DeputyGovernor.objects.get(state_id=state.pk)).data.get('name')
            return Response({"Governor": name, "Deputy Governor": deputy})
        else:
            return Response({'error': 'state does not exist'})


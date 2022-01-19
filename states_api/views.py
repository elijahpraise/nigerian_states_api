from rest_framework import generics
from rest_framework.response import Response

from states_api.serializers import *
from states_api.models import *


class NigerianStateView(generics.CreateAPIView):

    def post(self, request, *args, **kwargs):
        name_of_state = request.data.get("name_of_state").capitalize()
        for states in NigerianState.objects.all():
            if states.name_of_state == name_of_state:
                governor_of_that_state = Governor.objects.get(state_id=states.pk)
                name = GovernorSerializer(governor_of_that_state).data.get('name', None)
                deputy = DeputyGovernorSerializer(DeputyGovernor.objects.get(state_id=states.pk)).data.get('name',
                                                                                                           None)
                return Response({"Governor": name, "Deputy Governor": deputy})

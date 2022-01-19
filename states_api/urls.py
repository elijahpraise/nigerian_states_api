from django.urls import path

from states_api.views import *

urlpatterns = [
    path('states/', NigerianStateView.as_view(), name='states'),
]
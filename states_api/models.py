from django.db import models


class NigerianState(models.Model):
    name_of_state = models.CharField(max_length=100)
    number_of_local_governments = models.IntegerField()
    range_of_population = models.IntegerField()

    def __str__(self):
        return self.name_of_state


class Governor(models.Model):
    name = models.CharField(max_length=100)
    state = models.OneToOneField(NigerianState, related_name='governors', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class DeputyGovernor(models.Model):
    name = models.CharField(max_length=100)
    state = models.OneToOneField(NigerianState, on_delete=models.CASCADE)
    governor = models.OneToOneField(Governor, related_name='deputy_governors', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

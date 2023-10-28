from django.db import models

class WorkStations(models.Model):
    workstation_cycle_time= models.FloatField(default=0)
    transportation_time= models.FloatField(default=0)
    created_at = models.DateTimeField(
        verbose_name="created at", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="update at", auto_now=True)

    def __str__(self):
        return str(self.worker)










from django.db import models
from user.models import CustomUser
from workstations.models import WorkStations

class ForemanInfo(models.Model):
    user= models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    worker_workstation= models.ForeignKey(WorkStations, on_delete=models.CASCADE)
    worker_name= models.CharField(blank=False, null=True, max_length=100)
    worker_surname= models.CharField(blank=False, null=True, max_length=100)
    worker_tel_no= models.CharField(blank=False, null=True, max_length=100)
    worker_task_time= models.FloatField(default=0)
    created_at = models.DateTimeField(
        verbose_name="created at", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="update at", auto_now=True)
    
    def __str__(self):
        return str(self.user)

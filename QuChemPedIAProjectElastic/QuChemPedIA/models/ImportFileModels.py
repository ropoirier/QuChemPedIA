from django.db import models
from QuChemPedIA.models.UserModel import Utilisateur
from QuChemPedIA.models.SoftwareModel import Software
from QuChemPedIA.models.VersionModel import SoftwareVersion
from QuChemPedIA.models.JobTypeModel import JobType


class ImportFile(models.Model):
    """class that define an object for DB in django, here we define ImportFile table"""
    id_file = models.BigAutoField(primary_key=True)
    id_user = models.ForeignKey(Utilisateur, null=True, default=None, on_delete=models.SET_NULL)  # si null -> anonymous
    path_file = models.FilePathField(default=None, null=False)  # must be fill
    status = models.CharField(max_length=100, default="stand-by", null=False)
    id_software = models.ForeignKey(Software, null=True, default=None, on_delete=models.SET_NULL)
    id_version = models.ForeignKey(SoftwareVersion, null=True, default=None, on_delete=models.SET_NULL)
    id_job_type = models.ForeignKey(JobType, null=True, default=None, on_delete=models.SET_NULL)

    class Meta:
        verbose_name = "imported file"

    def __str__(self):
        return self.id_file

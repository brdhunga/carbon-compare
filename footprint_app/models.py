from django.db import models

# Create your models here.


class FootPrint(models.Model):
    """
    todo: thumbnail, average consumption
    """
    title = models.CharField(max_length=200, default="", blank=False, null=False)
    description = models.CharField(max_length=200, default="", blank=True, null=True)
    footprint = models.FloatField(blank=False, null=False,
                                  help_text="Use kg of CO2 per unit e.g. burger has 3.5 kg CO2 / burger")
    reference = models.TextField(default="", blank=True, null=True,
                                 help_text="Use either academic journal or trusted website")

    def __str__(self):
        return self.title


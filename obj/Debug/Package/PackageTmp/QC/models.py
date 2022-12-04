from django.db import models

class Komarigotolist(models.Model):
    """description of class"""

    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=10, blank=True, null=True)
    name = models.CharField(max_length=1000, db_column='name')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        return super().save(*args, **kwarges)


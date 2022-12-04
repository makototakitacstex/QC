from django.db import models

# Create your models here.

class Eikyo1(models.Model):
    """description of class"""

    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=10, blank=True, null=True)
    eikyo_desc = models.CharField(max_length=1000, db_column='eikyo_desc')

    def __str__(self):
        return self.eikyo_desc

    def save(self, *args, **kwargs):
        return super().save(*args, **kwargs)

class Eikyo2(models.Model):
    """description of class"""

    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=10, blank=True, null=True)
    eikyo_desc = models.CharField(max_length=1000, db_column='eikyo_desc')

    def __str__(self):
        return self.eikyo_desc

    def save(self, *args, **kwargs):
        return super().save(*args, **kwargs)

class Genin1(models.Model):
    """description of class"""

    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=10, blank=True, null=True)
    genin_desc2 = models.CharField(max_length=1000, blank=True, db_column='genin_desc2')

    def __str__(self):
        return self.genin_desc2

    def save(self, *args, **kwargs):
        return super().save(*args, **kwargs)

class Genin2(models.Model):
    """description of class"""

    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=10, blank=True, null=True)
    genin_desc2 = models.CharField(max_length=1000, blank=True, db_column='genin_desc2')

    def __str__(self):
        return self.genin_desc2

    def save(self, *args, **kwargs):
        return super().save(*args, **kwargs)

class Komarigotolist(models.Model):
    """description of class"""

    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=10, blank=True, null=True)

    komarigoto = models.CharField(max_length=1000, db_column='komarigoto')

    eikyo1_code = models.ForeignKey( Eikyo1, on_delete=models.CASCADE, blank=True, null=True )
    eikyo2_code = models.ForeignKey( Eikyo2, on_delete=models.CASCADE, blank=True, null=True )

    genin1_code = models.ForeignKey( Genin1, on_delete=models.CASCADE, blank=True, null=True )
    genin2_code = models.ForeignKey( Genin2, on_delete=models.CASCADE, blank=True, null=True )

    def __str__(self):
        return self.komarigoto

    def save(self, *args, **kwargs):
        return super().save(*args, **kwargs)

class KomarigotoInput(models.Model):
    """description of class"""

    id = models.AutoField(primary_key=True)

    komarigoto = models.CharField(max_length=10, blank=True, null=True)

    eikyo1_code = models.CharField(max_length=1000, blank=True, db_column='eikyo1_code')
    eikyo2_code = models.CharField(max_length=1000, blank=True, db_column='eikyo2_code')

    genin1_code = models.CharField(max_length=1000, blank=True, db_column='genin1_code')
    genin2_code = models.CharField(max_length=1000, blank=True, db_column='genin2_code')

    def save(self, *args, **kwargs):
        return super().save(*args, **kwargs)


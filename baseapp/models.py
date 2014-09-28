from django.db import models

# Create your models here.


class BaseModel(models.Model):
    create_user = models.CharField(max_length=20)

    class Meta:
        abstract = True

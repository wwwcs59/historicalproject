from django.contrib.auth.models import AbstractUser
from django.db import models
from simple_history import register
from baseapp.models import BaseModel

# Create your models here.


class LinkMan(BaseModel):
    user_real_name = models.CharField(max_length=20)

    def __str__(self):
        return str(self.user_real_name)


class MyUser(AbstractUser, LinkMan):
    online_hours = models.IntegerField(default=0)

    def __str__(self):
        return str(self.user_real_name)

register(LinkMan)
register(MyUser)
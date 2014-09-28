# coding=utf-8
from django.db import models
from baseapp.models import BaseModel
from userapp.models import MyUser
from simple_history import register

# system lib

# custom lib


class MyClass(BaseModel):
    class_name = models.CharField(max_length=50)
    class_user = models.ForeignKey(MyUser, related_name="class_user__MyUser")


class MyClassAnother(BaseModel):
    my_class = models.ForeignKey(MyClass, related_name="my_class__MyClass")


'''
if did not register MyClass and MyClassAnother here,
use the app config(webapp.__init__.py).
'''

register(MyClass)
register(MyClassAnother)


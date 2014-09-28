# coding=utf-8
from django.apps import AppConfig
from simple_history import register
from webapp import MyClass, MyClassAnother

# system lib

# custom lib


class WebAppConfig(AppConfig):
    name = "webapp"

    def ready(self):
        register(MyClass)
        register(MyClassAnother)
from django.core.management.commands.runserver import Command as runserver
class Command(runserver):
    default_port = "3000"

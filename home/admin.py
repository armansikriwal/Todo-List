from home.views import tasks
from django.contrib import admin
from django.db.models.query_utils import RegisterLookupMixin
from home.models import Task
# Register your models here.
admin.site.register(Task)

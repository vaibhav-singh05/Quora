from django.contrib import admin
from core.models import Contact
from core.models import Question
from core.models import Profile

# Register your models here.

admin.site.register(Profile)

admin.site.register(Contact)

admin.site.register(Question)
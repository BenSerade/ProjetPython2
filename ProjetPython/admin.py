from django.contrib import admin
from .models import Session, FormSubmission, FormFirstLogin

# Register your models here.
admin.site.register(Session)
admin.site.register(FormSubmission)
admin.site.register(FormFirstLogin)
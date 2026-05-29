from django.contrib import admin
from .models import (
    Organization,
    DataSource,
    ImportBatch,
    ActivityRecord,
    AuditEntry
)

admin.site.register(Organization)
admin.site.register(DataSource)
admin.site.register(ImportBatch)
admin.site.register(ActivityRecord)
admin.site.register(AuditEntry)
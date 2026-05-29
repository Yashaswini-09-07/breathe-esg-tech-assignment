from django.db import models


class Organization(models.Model):
    name = models.CharField(max_length=255)
    industry = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class DataSource(models.Model):
    SOURCE_TYPES = [
        ('SAP', 'SAP'),
        ('UTILITY', 'Utility'),
        ('TRAVEL', 'Travel'),
    ]

    organization = models.ForeignKey(
        Organization,
        on_delete=models.CASCADE
    )

    source_type = models.CharField(
        max_length=20,
        choices=SOURCE_TYPES
    )

    name = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.source_type})"


class ImportBatch(models.Model):
    data_source = models.ForeignKey(
        DataSource,
        on_delete=models.CASCADE
    )

    file_name = models.CharField(max_length=255)

    imported_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file_name


class ActivityRecord(models.Model):

    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('APPROVED', 'Approved'),
        ('FLAGGED', 'Flagged'),
    ]

    SCOPE_CHOICES = [
        ('SCOPE1', 'Scope 1'),
        ('SCOPE2', 'Scope 2'),
        ('SCOPE3', 'Scope 3'),
    ]

    organization = models.ForeignKey(
        Organization,
        on_delete=models.CASCADE
    )

    batch = models.ForeignKey(
        ImportBatch,
        on_delete=models.CASCADE
    )

    activity_type = models.CharField(max_length=100)

    quantity = models.FloatField()

    unit = models.CharField(max_length=50)

    scope = models.CharField(
        max_length=20,
        choices=SCOPE_CHOICES
    )

    activity_date = models.DateField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='PENDING'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.activity_type


class AuditEntry(models.Model):

    activity_record = models.ForeignKey(
        ActivityRecord,
        on_delete=models.CASCADE
    )

    action = models.CharField(max_length=100)

    notes = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.action
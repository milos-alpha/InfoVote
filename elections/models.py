from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator

class ElectionRequirement(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    is_mandatory = models.BooleanField(default=True)
    min_age = models.PositiveIntegerField(validators=[MinValueValidator(18)])
    document_needed = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

# models.py
from django.db import models

class Election(models.Model):
    STATUS_CHOICES = [
        ('UPCOMING', 'Upcoming'),
        ('COMPLETED', 'Completed'),
        ('CANCELLED', 'Cancelled'),
    ]

    ELECTION_TYPES = [
        ('PRESIDENTIAL', 'Presidential'),
        ('PARLIAMENTARY', 'Parliamentary'),
        # Add other types as needed
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    election_type = models.CharField(max_length=20, choices=ELECTION_TYPES)

    def __str__(self):
        return self.title

class Requirement(models.Model):
    election = models.ForeignKey(Election, related_name='requirements', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    required_documents = models.TextField()  # List of required documents
    deadline = models.DateTimeField()

    def __str__(self):
        return self.title

        

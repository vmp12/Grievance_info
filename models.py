from django.db import models
from django.contrib.auth.models import User
import uuid

# Model for Grievance
class Grievance(models.Model):
    GRIEVANCE_TYPES = [
        ('IT', 'IT Issue'),
        ('HR', 'HR Issue'),
        ('Finance', 'Finance Issue'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    grievance_type = models.CharField(max_length=20, choices=GRIEVANCE_TYPES)
    description = models.TextField()
    priority = models.CharField(max_length=10)
    attachment = models.FileField(upload_to='attachments/', null=True, blank=True)
    status = models.CharField(max_length=10, default='Pending')

    def __str__(self):
        return f"{self.grievance_type} - {self.user.username}"

# Model for Password Reset
class PasswordReset(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reset_id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    created_when = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Password reset for {self.user.username} at {self.created_when}"
import uuid
from django.db import models
from django.conf import settings # to link to User model

class Goals(models.Model):
    # use UUID as primary key
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    # link each goal to a user
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='goals'
    )

    # system-generated title & description
    title = models.CharField(max_length=255)
    description = models.CharField(blank=True)

    # smartified input from AI layer
    raw_input = models.TextField(blank=True)

    # optional due date
    due_date = models.DateField(null=True, blank=True)

    # completion status
    completion_status = models.BooleanField(default=False)

    # timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.TimeField(auto_now=True)

    def __str__(self):
        return self.title

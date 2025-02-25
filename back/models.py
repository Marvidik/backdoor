from django.db import models

# Create your models here.
from django.db import models

class ModelStatus(models.Model):
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"Model is {'active' if self.is_active else 'inactive'}"
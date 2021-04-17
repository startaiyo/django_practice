from django.db import models

# Create your models here.
class Memo(models.Model):
    skill_name=models.CharField(max_length=100)
    content=models.TextField()
    status=models.CharField(default='NG',max_length=100)
    def __str__(self):
        """A string of the model."""
        return self.skill_name
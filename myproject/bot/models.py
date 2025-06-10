from django.db import models

class TelegramUser(models.Model):
    user_id = models.PositiveIntegerField(unique=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} ({self.user_id})"

from django.db import models


class Analysis(models.Model):
    text = models.TextField()
    label = models.CharField(max_length=20)
    score = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.label} ({self.score}%): {self.text[:40]}"
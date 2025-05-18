from django.db import models

class Post(models.Model):
    platform = models.CharField(max_length=20)
    post_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.platform}: {self.post_text[:30]}"

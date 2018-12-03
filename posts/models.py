from django.conf import settings
from django.urls import reverse
from django.db import models

import mistune

from Groups.models import Group

from django.contrib.auth import get_user_model
User = get_user_model()


class Post(models.Model):
    user = models.ForeignKey(User, related_name="posts",on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    message = models.TextField()
    message_html = models.TextField(editable=False)
    group = models.ForeignKey(Group, related_name="posts",null=True, blank=True,on_delete=models.CASCADE)

    def __str__(self):
        return self.message

    def save(self, *args, **kwargs):
        renderer = mistune.Renderer(escape=True, hard_wrap=True)
        # use this renderer instance
        markdown = mistune.Markdown(renderer=renderer)
        self.message_html = markdown(self.message)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse(
            "posts:single",
            kwargs={
                "username": self.user.username,
                "pk": self.pk
            }
        )

    class Meta:
        ordering = ["-created_at"]
        unique_together = ["user", "message"]

from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Candidate(models.Model):
    photo = models.ImageField(upload_to='candidate_photos/', default='candidate_photos/user.png')
    name = models.CharField(max_length=100)
    post = models.ForeignKey(Post, related_name='candidates', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} for {self.post.name}'

class Vote(models.Model):
    voter = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('voter', 'candidate')

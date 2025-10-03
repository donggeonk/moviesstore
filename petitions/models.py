from django.db import models
from django.contrib.auth.models import User

class Petition(models.Model):
    title = models.CharField(max_length=255)
    reason = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    # This field tracks all users who have voted for this petition
    votes = models.ManyToManyField(User, related_name='voted_petitions', blank=True)

    def __str__(self):
        return self.title

    # A helper function to easily get the vote count
    def get_vote_count(self):
        return self.votes.count()
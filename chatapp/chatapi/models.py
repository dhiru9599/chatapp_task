from django.db import models
class User(models.Model):
    username = models.CharField(max_length=50, primary_key=True)
  
    # Add other user fields as needed

class Group(models.Model):
    name = models.CharField(max_length=50, primary_key=True)
    members = models.ManyToManyField(User)

class Message(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

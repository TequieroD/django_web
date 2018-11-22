from django.db import models
import uuid

# Create your models here.
class auth(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    account = models.CharField(max_length=256)
    password = models.CharField(max_length=256)
    enable = models.BooleanField(default=False)
    name = models.CharField(max_length=256)
    line_id = models.CharField(max_length=256)

    def __str__(self):
        return 'account=%s, password=%s, name=%s, line_id=%s' % (self.account, self.password, self.name, self.line_id)

class action(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    action_name = models.CharField(max_length=256)
    action_detail = models.TextField()
    action_datetime = models.DateTimeField(auto_now=True)
    enable = models.BooleanField(default=False)

class signup(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    user_id = models.CharField(max_length=256)
    class_id = models.CharField(max_length=256)
    sign_datetime = models.DateTimeField(auto_now_add=True)

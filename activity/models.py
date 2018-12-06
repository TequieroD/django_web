from django.db import models
import uuid

# Create your models here.
class classSummaryModel(models.Model):
	id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
	action_name = models.CharField(max_length=200, null=False)
	action_detail = models.TextField()
	action_datetime = models.DateTimeField(auto_now=True, null=False)
	enable = models.BooleanField(default=False)

	class Meta:
		db_table = 'class_summary'

	def __str__(self):
		return self.action_name

class signUpModel(models.Model):
	id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
	user_id = models.CharField(max_length=200, null=False)
	class_id = models.CharField(max_length=200, null=False)
	signup_datetime = models.DateTimeField(auto_now=True, null=False)

	class Meta:
		db_table = 'sign_up'

	def __str__(self):
		return self.user_id
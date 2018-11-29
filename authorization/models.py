from django.db import models
import uuid

# Create your models here.
class authorizationModel(models.Model):
	id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
	account = models.CharField(max_length=10, null=False)
	password = models.CharField(max_length=50, null=False)
	name = models.CharField(max_length=10, null=False)
	line_id = models.CharField(max_length=50, null=True)
	enable = models.BooleanField(default=False)

	class Meta:
		db_table = 'authorization'

	def __str__(self):
		return self.account
		#return 'account=%s, password=%s, name=%s, line_id=%s' % (self.account, self.password, self.name, self.line_id)
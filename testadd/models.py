from django.db import models

class address(models.Model):
	name = models.CharField(max_length=150)
	address = models.CharField(max_length=250)
	city = models.CharField(max_length=50)
	state = models.CharField(max_length=5)
	zipcode = models.CharField(max_length=12)
	received = models.BooleanField(default=False)
	
	class Meta:		
		verbose_name_plural = "addresses"	

	def __str__(self):
		return self.name + " | " + self.address + " | " + self.city + " | " + self.state + " | " + self.zipcode + " | " + str(self.received)

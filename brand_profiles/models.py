from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)

    def __unicode__(self):
        return self.name

class Page(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=128)
    url = models.URLField()
    view = models.IntegerField(default=0)

    def __unicode__(self):
        return self.title

class Brand_Identities(models.Model):
	name = models.CharField(max_length=256)
	city = models.CharField(max_length=256, null=True)
	country = models.CharField(max_length=256, null=True)
	website = models.CharField(max_length=256, null=True)
	email = models.CharField(max_length=256, null=True)
	contact_number = models.CharField(max_length=256, null=True)
	address = models.CharField(max_length=256, null=True)

	def __unicode__(self):
		return self.name

class Reviews(models.Model):
	brand = models.ForeignKey(Brand_Identities, null=True)
	review = models.TextField()
	sentiment_score = models.NullBooleanField()
	subjectivity = models.NullBooleanField()
	objectivity = models.NullBooleanField()
	classification_tag = models.CharField(max_length=256, null=True)

	def __unicode__(self):
		return self.review[:15]

class Tours(models.Model):
	brand = models.ForeignKey(Brand_Identities, null=True)
	name = models.CharField(max_length=256, null=True)
	classification_tag = models.CharField(max_length=256, null=True)
	opening_time = models.DateTimeField()
	cloasing_time = models.DateTimeField()
	average_duration = models.CharField(max_length=256, null=True)
	pricing =  models.CharField(max_length=256, null=True)
	description = models.CharField(max_length=256, null=True)
	availabile_spots = models.IntegerField(default=0)
	booking_capacity = models.IntegerField(default=0)
	filled_capacity = models.IntegerField(default=0)

	def __unicode__(self):
		return self.name

class Promotions(models.Model):
	brand = models.ForeignKey(Brand_Identities, null=True)
	tour = models.ForeignKey(Tours, null=True)
	promotion = models.CharField(max_length=256, null=True)
	duration = models.DateTimeField()

	def __unicode__(self):
		return self.promotion

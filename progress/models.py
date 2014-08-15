from django.db import models

# Create your models here.
class Child(models.Model):
	name = models.CharField(max_length = 256)
	dob = models.DateField('Date of Birth')
	address = models.CharField(max_length = 2048)
	caretaker = models.CharField(max_length = 256)

	def __unicode__(self):
		return self.name
	
class Curriculum(models.Model):
	name = models.CharField(max_length=128)

class Section(models.Model):
	name = models.CharField(max_length = 256)
	cirruculum = models.ForeignKey(Curriculum)

	def __unicode__(self):
		return self.name


class SubSection(models.Model):
	name = models.CharField(max_length=256)
	section = models.ForeignKey(Section)

	def __unicode__(self):
		return self.name

class AgeRange(models.Model):
	name = models.CharField(max_length=256)
	range = models.CharField(max_length=8)

	def __unicode__(self):
		return str(self.name) + "|" + str(self.range)

class Question(models.Model):
	name = models.CharField(max_length = 256)
	#section = models.ForeignKey(Section) --yet to see if this is needed.
	subSection = models.ForeignKey(SubSection)
	age_range = models.ForeignKey(AgeRange)
	text = models.CharField(max_length = 2048)

	def __unicode__(self):
		return str(self.name) + "|" + str(self.text)

class Assessment(models.Model):
	child = models.ForeignKey(Child)
	date = models.DateField('Date of Assessment')

	def __unicode__(self):
		return str(self.child)+" | "+str(self.date)

class Response(models.Model):
	question = models.ForeignKey(Question)
	value = models.CharField(max_length = 2048)
	notes = models.CharField(max_length = 2048)
	assessment = models.ForeignKey(Assessment)

	def __unicode__(self):
		return str(self.question) + " | " + str(self.value) + " | " + str(self.assessment.child)


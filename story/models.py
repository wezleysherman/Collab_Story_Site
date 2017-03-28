from __future__ import unicode_literals
from datetime import datetime
from django.db import models



class StoryLine(models.Model):
	line_text = models.CharField(max_length = 1024)
	contributer = models.CharField(max_length = 128)
	date_published = models.DateTimeField(default = datetime.now()) 

	def __str__(self):
		return self.line_text


class Story(models.Model):
	story_title = models.CharField(max_length = 256)
	sentences = models.ManyToManyField(StoryLine)
	created = models.DateTimeField(default = datetime.now())

	def __str__(self):
		rtnStr = self.story_title + ": ".join(sen.line_text for sen in self.sentences.all()) 
		return rtnStr

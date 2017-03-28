from django import forms

class SentenceForm(forms.Form):
	user_name = forms.CharField(label = 'name', max_length = 128)
	user_input = forms.CharField(label = 'sentence', max_length = 1024)

class StoryForm(forms.Form):
	story_title = forms.CharField(label = 'title', max_length = 256)

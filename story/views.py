from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.template import loader
from django.urls import reverse
from .models import Story, StoryLine
from .forms import SentenceForm, StoryForm

def index(request):
	stories_list = Story.objects.order_by('created')
	page_out = loader.get_template('story/index.html')
	storyForm = StoryForm(request.POST)
	if(request.POST):
		if(storyForm.is_valid()):
			new_story = Story()
			new_story.story_title = storyForm.cleaned_data['story_title']
			new_story.save()

	context = {
		'stories_list' : stories_list,
		'storyForm' : storyForm,
	}
	return HttpResponse(page_out.render(context, request))

def story(request, story_id):
	sentenceForm = SentenceForm(request.POST)
	if(request.POST):
		main_story = get_object_or_404(Story, pk = story_id)
		sentence = StoryLine()
		if(sentenceForm.is_valid()):
			user_name = sentenceForm.cleaned_data['user_name']
			user_sentence = sentenceForm.cleaned_data['user_input']
			sentence.contributer = user_name
			sentence.line_text = user_sentence
			sentence.save()
			main_story.sentences.add(sentence)
			main_story.save()

	story = get_object_or_404(Story, pk = story_id)
	page_out = loader.get_template('story/story.html')
	context = {
		'story_sentences' : story,
		'sentenceForm' : sentenceForm,
	}
	return HttpResponse(page_out.render(context, request))


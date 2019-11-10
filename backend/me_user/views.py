import json

from .models import MeUser, MeLink, MePost

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def create_post(request):
	title = request.POST.get('title')
	author = request.POST.get('username')
	links = request.POST.getlist('links[]')

	author = MeUser.objects.try_fetch(username=author)
	if not author:
		return HttpResponse('User doesnt exist', status=400)

	post = MePost.objects.create(title=title, author=author)
	for link in links:
		post.links.add(MeLink.objects.create(link=link))
	return HttpResponse('Created post')

def fetch_posts(request):
	posts = MePost.objects.all().order_by('-date_created')
	return HttpResponse(json.dumps([post.get_json() for post in posts]), content_type='application/json')
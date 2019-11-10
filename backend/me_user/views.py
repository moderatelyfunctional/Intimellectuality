import json

import me_user.ml as ml
from me_user.models import MeUser, MeLink, MePost

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def create_post(request):
	# body_unicode = request.body.decode('utf-8')
	# body = json.loads(json.loads(body_unicode))

	# title = body['title']
	# author = body['username']
	# links = body['links']

	title =  request.POST.get('title')
	author = request.POST.get('username')
	links =  request.POST.getlist('links')

	author = MeUser.objects.try_fetch(username=author)
	if not author:
		return HttpResponse('User doesnt exist', status=400)

	post = MePost.objects.create(title=title, author=author)
	for link in links:
		post.links.add(MeLink.objects.create(link=link))
	return HttpResponse('Created post')

def fetch_posts(request):
	posts = MePost.objects.all().order_by('-date_created')
	user = MeUser.objects.try_fetch(username='jing')

	ordered_posts = ml.order_docs(user.description, posts)

	return HttpResponse(json.dumps(ordered_posts), content_type='application/json')

def fetch_profile(request):
	username = request.GET.get('username')

	user = MeUser.objects.try_fetch(username=username)
	if not user:
		return HttpResponse('User doesnt exist', status=400)

	return HttpResponse(json.dumps({'description': user.description}), content_type='application/json')

def update_profile(request):
	body_unicode = request.body.decode('utf-8')
	body = json.loads(body_unicode)

	username = body['username']
	description = body['description']

	user = MeUser.objects.try_fetch(username=username)
	if not user:
		return HttpResponse('User doesnt exist', status=400)

	user.description = description
	user.save()
	return HttpResponse('Success')




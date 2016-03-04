from django.http import HttpResponse
import json, pdb
from django.core.serializers.json import DjangoJSONEncoder
from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.template import RequestContext
from django.shortcuts import render_to_response
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import viewsets
from models import Reviews, Brand_Identities
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from serializers import Brand_IdentitiesSerializers, ReviewsSerializers
from django.contrib.auth.models import User, Group

from profile import Profile


class Brand_IdentitiesViewSet(viewsets.ModelViewSet):
	queryset = Brand_Identities.objects.all()
	serializer_class = Brand_IdentitiesSerializers

class ReviewsViewSet(viewsets.ModelViewSet):
	queryset = Reviews.objects.all()
	serializer_class = ReviewsSerializers

def api_view(request):
	context = RequestContext(request)
	context_dict = {}
	
	return render_to_response('brand_profiles/api_view.html', context_dict, context)

def work_view(request):
	context = RequestContext(request)
	context_dict = {}
	
	return render_to_response('brand_profiles/work.html', context_dict, context)

def education_view(request):
	context = RequestContext(request)
	context_dict = {}
	
	return render_to_response('brand_profiles/education.html', context_dict, context)

def contact_view(request):
	context = RequestContext(request)
	context_dict = {}
	
	return render_to_response('brand_profiles/contact.html', context_dict, context)


def index(request):
	context = RequestContext(request)
	context_dict = {}

	return render_to_response('brand_profiles/index.html', context_dict, context)

@csrf_exempt
def sample(request):
	if request.method == "POST":
		print "In sample"
		jsonstr = request.POST.get('json')
		print jsonstr[:20]
		if jsonstr:
			try:
				params = json.loads(jsonstr)
				
				analyser = Profile(params)
				text_analysis = analyser.analysis()
				print text_analysis

				map = {'frequent_words':text_analysis['freq_words'], 'pos_tags':text_analysis['pos_tags'], 'sentiments':text_analysis['sentiments']}
				data = json.dumps(map, cls = DjangoJSONEncoder)
				# pdb.set_trace()
				return HttpResponse(data, content_type="application/json")
			except KeyError:
				return HttpResponse(json.dumps({'error':'error in query string'}), content_type = "application/json")
			except:
				return HttpResponse(json.dumps({'error':'internal error in Django'}), content_type = "application/json")
				
		return HttpResponse(json.dumps({'error':'no POST json parameter received'}), content_type = "application/json")
	else:
		return "Please send a POST request"		

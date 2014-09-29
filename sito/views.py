from django.shortcuts import render
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse
from django.template import RequestContext
from django.views.generic import ListView, DetailView
from sito.models import *
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

##contact 
from sito.contact import ContactForm
from django import forms
from django.core.mail import send_mail, BadHeaderError
from django.core.context_processors import csrf


# Create your views here.

def IndexView(request):
	post_list = Post.objects.all().order_by('-pub_date')
	gallery_list = Post.objects.filter(revhome = '1').order_by('-pub_date')[:6]
	context = {'post_list':post_list,
				'gallery_list': gallery_list}
	return render(request, 'index.html', context)


def FreezerView(request):
	post_list = Post.objects.all().order_by('-pub_date')
	context = {'post_list':post_list}
	return render(request, 'freezer.html', context)
	

def DettaglioView(request, post_id):
	post = Post.objects.get(pk=post_id)
	post_list = Post.objects.all().order_by('-pub_date')
	context = {
				'post': post,
				'post_list':post_list
				}
	return render_to_response('dettaglio.html', context, context_instance=RequestContext(request))


###ContactForm

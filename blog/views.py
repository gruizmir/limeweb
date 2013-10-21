# -*- coding: utf-8 -*-
import os
import logging
import uuid
from blog.forms import ArticleForm
from datetime import datetime
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core import mail
from django.core.context_processors import csrf
from django.core.exceptions import ObjectDoesNotExist, PermissionDenied, SuspiciousOperation
from django.db.models import Max
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.utils import simplejson

@login_required
def newArticle(request):
    form = ArticleForm()
    return render_to_response("new_article.html", {'form':form}, context_instance=RequestContext(request))

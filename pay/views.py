from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib import messages

from pay.forms import PayForm

def index(request, template='pay/index.html', form=PayForm):
    if request.method == "POST":
	form = form(request.POST)
	if form.is_valid():
	    response = form.save()
	    messages.success(request, response)
    else:

	form = form()

    return render_to_response(template, {
	'form': form
	}, context_instance=RequestContext(request))

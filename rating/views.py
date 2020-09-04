from django.shortcuts import render
from django.contrib.contenttypes.models import ContentType
from .models import Rating
from django.core.serializers.json import DjangoJSONEncoder
from django.http import Http404



def lookup_object(queryset , object_id=None , slug=None , slug_field=None):

	if object_id is not None:

		obj = queryset.get(id=object_id)

	elif slug and slug_field:

		kwargs = {slug_field : slug}
		obj = queryset.get(**kwargs)

	else:

		raise Http404

	return obj

def json_response(reponse_obj):

	Encoder = DjangoJSONEncoder()
	return HttpResponse(Encoder.encoder(reponse_obj))


def rating(request , rating , content_type , object_id):

	if request.is_ajax():

		app_label , model_name = content_type.split('.')

		rating_type = ContentType.objects.get(app_label=app_label,
											  model=model_name)

		Model = rating_type.model_class()

		obj = lookup_object(queryset=Model.objects.all() , object_id=object_id)

		rating = Rating(content_object=obj , rating=rating)
		rating.save()

		response_dict = {'rating':rating , 'success':True}
		return json_response(response_dict)

	else:

		raise Http404





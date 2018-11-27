from django.conf.urls import url

from .views.GreetUser import GreetView
from .views.swagger_api_view import SwaggerSchemaView

urlpatterns = [
    url(r'^$', SwaggerSchemaView.as_view()),
    url(r'^PostProcessing/Greet/(?P<name>[-\w]+)/',
        GreetView.as_view(), name="name"),

    # url(r'^PostProcessing/FieldName/(?P<fieldname>[-\w]+)/PredictedField/(?P<inputstring>[-\w]+)/',
    #     RoundoffView.as_view(), name="2")
]

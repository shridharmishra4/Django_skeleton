from django.conf.urls import url

from .views.greet_view import GreetView
from .views.swagger_api_view import SwaggerSchemaView
from .views.transcodified_view import TranscodifiedView
from .views.match_values_view import MatchValuesView

urlpatterns = [
    url(r'^$', SwaggerSchemaView.as_view()),
    url(r'^PostProcessing/Greet/(?P<name>[-\w]+)/',
        GreetView.as_view(), name="name"),




    url(r'^PostProcessing/FieldName/(?P<fieldname>[^\n]+)'
        r'/PredictedField/(?P<predictedvalue>[^\n]+)'
        r'/XoneField/(?P<xonefield>[^\n]+)/$',
        MatchValuesView.as_view(), name="hello"),

    url(r'^PostProcessing/FieldName/(?P<fieldname>[^\n]+)'
        r'/PredictedField/(?P<predictedvalue>[^\n]+)/$',
        TranscodifiedView.as_view(), name="trans"),
    # url(r'^PostProcessing/FieldName/(?P<fieldname>[-\w]+)/PredictedField/(?P<inputstring>[-\w]+)/',
    #     RoundoffView.as_view(), name="2")
]

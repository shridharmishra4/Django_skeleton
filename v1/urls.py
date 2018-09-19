from django.conf.urls import url

from .views.roundoff_view import RoundoffView
from .views.swagger_api_view import SwaggerSchemaView
from .views.transcodified_view import TranscodifiedView

urlpatterns = [
    url(r'^$', SwaggerSchemaView.as_view()),
    url(r'^PostProcessing/FieldName/(?P<fieldname>[-\w]+)/PredictedField/(?P<inputstring>[-\w]+)/',
        TranscodifiedView.as_view(), name="1"),
    url(r'^PostProcessing/FieldName/(?P<fieldname>[-\w]+)/PredictedField/(?P<inputstring>[-\w]+)/',
        RoundoffView.as_view(), name="2")

]

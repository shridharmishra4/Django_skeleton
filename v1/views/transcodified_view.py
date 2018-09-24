import datetime

from rest_framework.response import Response
from rest_framework.views import APIView
from ..core.get_root import GetRoot
from django.conf import settings

class TranscodifiedView(APIView):
    def get(self, request, fieldname, predictedvalue):
        """
        Returns transcodified value for request string.

        **Example Response**

                {
                    "InputString": "string",
                    "TranscodifiedString": "string",
                    "GeneratedAt":"Datetime",
                    "Version": "string"
                }

        """
        root_obj = GetRoot()
        root_value = root_obj.get_root_word(fieldname,predictedvalue)
        return Response({
            "InputString": predictedvalue,
            "GeneratedAt": datetime.datetime.now(),
            "TranscodifiedString": root_value,
            "Version": "2"
        })

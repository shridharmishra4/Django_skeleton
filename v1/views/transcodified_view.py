import datetime

from rest_framework.response import Response
from rest_framework.views import APIView


class TranscodifiedView(APIView):
    def get(self, request, fieldname, inputstring):
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

        return Response({
            "InputString": inputstring,
            "GeneratedAt": datetime.datetime.now(),
            "TranscodifiedString": [],
            "Version": "1"
        })

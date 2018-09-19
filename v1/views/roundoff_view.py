import datetime

from rest_framework.response import Response
from rest_framework.views import APIView


class RoundoffView(APIView):
    def get(self, request, InputFloat):
        """
        Returns transcodified value for request string.

        **Example Response**

                {
                    "InputFloat": "Float",
                    "OutputFloat": "Float",
                    "GeneratedAt":"Datetime",
                    "Version": "string"
                }

        """

        return Response({
            "InputFloat": InputFloat,
            "OutputFloat": 0.0,
            "GeneratedAt": datetime.datetime.now(),
            "Version": "1"
        })

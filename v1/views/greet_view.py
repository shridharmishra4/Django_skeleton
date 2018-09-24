from rest_framework.response import Response
from rest_framework.views import APIView

from ..core.get_root import GetRoot




class GreetView(APIView):
    def get(self, request):
        """
        Greets you :)

        **Example Response**

                {
                    "Greetings": "string",

                }

        """
        greet = GetRoot()
        return Response({
            "Greetings": ""

        })

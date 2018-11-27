from rest_framework.response import Response
from rest_framework.views import APIView
from ..core.helloworld import Greet




class GreetView(APIView):
    def get(self, request,name):
        """
        Greets you :)

        **Example Response**

                {
                    "Greetings": "string"

                }

        """
        return Response({
            "Greetings": Greet.hello(name)

        })

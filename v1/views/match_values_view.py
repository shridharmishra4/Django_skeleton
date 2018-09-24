import datetime

from rest_framework.response import Response
from rest_framework.views import APIView
from ..core.get_root import GetRoot


class MatchValuesView(APIView):
    def get(self, request, fieldname, predictedvalue, xonefield):
        """
        Returns transcodified value for request string.

        **Example Response**

        {
            "PredictedValue": string,
            "XoneValue": string,
            "Result":bool,
            "GeneratedAt": datetime,
            "Version": ""
        }

        """
        root_obj = GetRoot()
        match_result = root_obj.match_records(fieldname, predictedvalue, xonefield)

        return Response({
            "PredictedValue": predictedvalue,
            "XoneValue": xonefield,
            "Result": match_result,
            "GeneratedAt": datetime.datetime.now(),
            "Version": "2"
        })

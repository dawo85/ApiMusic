from rest_framework.response import Response
from rest_framework.views import APIView

class AlbumsView(APIView):

	def get(self, request):
		result = {}
		return Response(result)
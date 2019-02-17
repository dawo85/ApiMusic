from rest_framework.response import Response
from rest_framework.views import APIView
from albums.connection.connector import ConnectorMusic
from albums.serializers import AlbumSerializer

class AlbumsView(APIView):

	def get(self, request):
		params = {
			'artist_id': request.GET['id']
		}
		if 'limit' in request.GET:
			params['limit'] = request.GET['limit']
		if 'offset' in request.GET:
			params['offset'] = request.GET['offset']
		result = ConnectorMusic().get_albums(**params)
		data = result['release-group-list']
		albums = AlbumSerializer(data, many=True)
		result = { 'albums': albums.data}
		return Response(result)
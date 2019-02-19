from rest_framework import serializers
from albums.connection.connector import ConnectorMusic

class AlbumSerializer(serializers.Serializer):
	id = serializers.CharField(max_length=50)
	title = serializers.CharField(max_length=500)
	year = serializers.SerializerMethodField()
	release_count = serializers.SerializerMethodField()

	def get_year(self, obj):
		year = obj['first-release-date'].split('-')[0]
		return year

	def get_release_count(self, obj):
		release_count = ConnectorMusic().count_release(obj['id'])
		return release_count
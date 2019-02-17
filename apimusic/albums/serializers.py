from rest_framework import serializers

class AlbumSerializer(serializers.Serializer):
	id = serializers.CharField(max_length=50)
	title = serializers.CharField(max_length=500)
	year = serializers.SerializerMethodField()
	release_count = serializers.SerializerMethodField()

	def get_year(self, obj):
		year = obj['first-release-date'].split('-')[0]
		return year

	def get_release_count(self, obj):
		release_count = 0
		if 'release_group-relation-list' in obj:
			release_count = len(obj['release_group-relation-list'])
		return release_count
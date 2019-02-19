from apimusic.settings import PASSWORD_MUSIC, USER_MUSIC
import musicbrainzngs

class Singleton(object):
    _instance = None
    def __new__(class_, *args, **kwargs):
        if not isinstance(class_._instance, class_):
            class_._instance = object.__new__(class_, *args, **kwargs)
        return class_._instance

class ConnectorMusic(Singleton):

    def __init__(self):
        self.user = USER_MUSIC
        self.password = PASSWORD_MUSIC
        self.app = 'Apimusic'
        self.version = '0.1'
        self.email = ''
        musicbrainzngs.auth(self.user, self.password)
        musicbrainzngs.set_useragent(self.app, self.version, self.email)

    def get_albums(self, artist_id, limit=50, offset=0):
        result = musicbrainzngs.browse_release_groups(artist=artist_id,
                                                includes=[],
                                                release_type=["album"],
                                                limit=limit,
                                                offset=offset)
        return result

    def count_release(self, release_group_id):
        result = musicbrainzngs.browse_releases(release_group=release_group_id)
        return result['release-count']
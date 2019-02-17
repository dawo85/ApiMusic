from apimusic.settings import PASSWORD_MUSIC, USER_MUSIC
import musicbrainzngs


class ConnectorMusic(object):

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
                                                includes=["release-group-rels"],
                                                release_type=["album"],
                                                limit=limit,
                                                offset=offset)
        return result
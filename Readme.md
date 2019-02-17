# ApiMusic


#### How to ejecute the application with docker?

1. Open terminal.
2. Situate in project path.
3. Build docker with the command:
`$: docker-compose build`
4. Up docker with the command:
`$: docker-compose up`

#### How to ejecute the application without docker (Linux)?

1. Open terminal.
2. Situate in project path.
3. Ejecute:
`$:pip install -r requirements.txt`
4. Run django in apimusic:
`$:python -u manage.py runserver 0.0.0.0:8000`


#### Configuration password and username

1. Write user and password of MusicBrainz in params USER_MUSIC and PASSWORD_MUSIC of settings:

apimusic/apimusic/settings.py

#### APIS:
- Given an artist MusicBrainz Id the service returns a
list of release-groups of type Album and how many releases have each release-group.

http://localhost:8000/albums/?id={id artist}&limit={number limit}&offset={number offset}
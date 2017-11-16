TITLE = 'FuzionRadio.FM'
PREFIX = '/music/fuzionradio'
ICON = 'icon-default.jpg'
ART = 'art-default.jpg'
STREAM_URL = 'http://live.fuzionradio.fm:8000/'

####################################################################################################
def Start():

	ObjectContainer.art = R(ART)
	ObjectContainer.title1 = TITLE
	TrackObject.thumb = R(ICON)

####################################################################################################
@handler(PREFIX, TITLE, thumb=ICON, art=ART)
def MainMenu():

	oc = ObjectContainer()

	oc.add(CreateTrackObject(
		title = 'FuzionRadio.FM',
		url = STREAM_URL
	))

	return oc

####################################################################################################
@route(PREFIX + '/createtrackobject', include_container=bool)
def CreateTrackObject(title, url, include_container=False, **kwargs):

	track_object = TrackObject(
		key = Callback(CreateTrackObject, title=title, url=url, include_container=True),
		rating_key = url,
		title = title,
		items = [
			MediaObject(
				parts = [
					PartObject(key=Callback(PlayAudio, url=url, ext='mp3'))
				],
				container = Container.MP3,
				bitrate = 192,
				audio_codec = AudioCodec.MP3,
				audio_channels = 2
			)
		]
	)

	if include_container:
		return ObjectContainer(objects=[track_object])
	else:
		return track_object

####################################################################################################
def PlayAudio(url):

	return Redirect(url)

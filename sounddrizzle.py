'''
Sounddrizzle - a tiny Soundcloud downloader.

Usage:
	sounddrizzle.py [options] <url>

--output <FILE> 			The output file (defaults to artist/title)
--verbose					More output!
'''

from urlparse import urlparse
import logging

from docopt import docopt
import requests
import soundcloud

logging.basicConfig(format='%(asctime)s [%(levelname)s] %(msg)s')
log = logging.getLogger('SoundDrizzle')


def main(args):
	set_loglevel(args)
	client = soundcloud.Client(client_id='7b4b979cb9f47830a7bb2441f6d784c3')
	track = get_track_by_url(client, args['<url>'])
	stream = client.get(track.stream_url, allow_redirects=False)
	output = get_filename_for_track(args, client, track)

	log.info('Downloading %s to %s' % (track.title, output))
	
	r = requests.get(stream.location)
	log.debug('Response is %d bytes long', int(r.headers['Content-Length']))

	with open(output, 'w+') as f:
		f.write(r.content)

def get_track_by_url(client, url):
	'''
		Gets a track by the given Soundcloud URL.

		Example URL https://soundcloud.com/ovey/duck-sauce-barba-streisand-ovey-remix-clip
	'''
	try:
		path = urlparse(url).path
		tracks = client.get('/tracks', q=path)

		if tracks:
			if len(tracks) > 1:
				return tracks
			else:
				return tracks[0]
		else:
			raise ValueError('Track not found for URL %s' % url)
	except Exception as e:
		raise ValueError('Error obtaining track by url: %s' % str(e))

def get_filename_for_track(args, client, track):
	if not args['--output']:
		title = track.title.lower().replace(' ', '_')
		artist = track.user['permalink'].lower().replace(' ', '_')

		return '%s-%s.mp3' % (artist, title)
	else:
		return args['--output']

def set_loglevel(args):
	level = logging.INFO
	if args.get('--verbose', None):
		level = logging.DEBUG

	log.setLevel(level)

if __name__ == '__main__':
	args = docopt(__doc__)
	main(args)

import logging
import urlparse
import click
import termcolor
import mutagen.id3
import mutagen.mp3
import requests
import soundcloud

client = soundcloud.Client(client_id='7b4b979cb9f47830a7bb2441f6d784c3')
log = logging.getLogger('SoundDrizzle')


def _bold(text):
    return termcolor.colored(text, attrs=['bold'])


@click.command()
@click.argument('track_url')
@click.argument('destination', required=False)
def pour(track_url, destination=None):
    try:
        track = resolve(track_url)
        destination = destination or filename_for_track(track)
        track_details = client.get(track.stream_url, allow_redirects=False)
        click.echo('Resolved link to {} by {}'.format(_bold(track.title), _bold(track.user['username'])))

        stream_url = track_details.location

        download(stream_url, destination)
        click.echo('Successfully downloaded track to {}'.format(_bold(destination)))
        add_metadata(destination, track)
        click.echo('Done! Enjoy listening offline!')
    except Exception as e:
        click.echo('Problem downloading track: {}'.format(e))


def resolve(track_url):
    """
    Resolves the URL to an actual track from the SoundCloud API.

    If the track resolves to more than one possible track, it takes the first search result.

    :returns: The track dictionary from the SoundCloud API
    """
    try:
        path = urlparse.urlparse(track_url).path
        tracks = client.get('/tracks', q=path)

        if tracks:
            return tracks[0]
        else:
            raise ValueError('Track not found for URL {}'.format(track_url))
    except Exception as e:
        raise ValueError('Error obtaining track by url: {}'.format(str(e)))


def filename_for_track(track):
    """
    :return: A safe filename for the given track
    """
    artist = track.user['permalink']
    title = track.title

    return '{}-{}.mp3'.format(artist, title).lower().replace(' ', '_').replace('/', '_')


def download(url, target_file, chunk_size=4096):
    """
    Simple requests downloader
    """
    r = requests.get(url, stream=True)

    with open(target_file, 'w+') as out:
        # And this is why I love Armin Ronacher:
        with click.progressbar(r.iter_content(chunk_size=chunk_size),
                               int(r.headers['Content-Length'])/chunk_size,
                               label='Downloading...') as chunks:
            for chunk in chunks:
                out.write(chunk)


def add_metadata(track_file, track_data):
    """
    Adds artist and title from the track data, and downloads the cover and embeds it in the MP3 tags.
    """
    # This needs some exception handling!
    # We don't always know what type the cover is!
    mp3 = mutagen.mp3.MP3(track_file)

    mp3['TPE1'] = mutagen.id3.TPE1(encoding=3, text=track_data.user['username'])
    mp3['TIT2'] = mutagen.id3.TIT2(encoding=3, text=track_data.title)

    cover_bytes = requests.get(track_data.artwork_url, stream=True).raw.read()
    mp3.tags.add(mutagen.id3.APIC(encoding=3, mime='image/jpeg', type=3, desc='Front cover', data=cover_bytes))

    mp3.save()
# In serializer_demo.py

import json
import xml.etree.ElementTree as et


class Song:
    def __init__(self, song_id, title, artist):
        self.song_id = song_id
        self.title = title
        self.artist = artist


class SongSerializer:
    # the client component of the pattern
    def serialize(self, song, format):
        serializer = _get_serializer(format)
        return serializer(song)


# the product component
def _get_serializer(format):
    if format == 'JSON':
        return _serialize_to_json
    elif format == 'XML':
        return _serialize_to_xml
    else:
        raise ValueError(format)


def _serialize_to_json(song):
    # concrete implementations of the product
    payload = {
        'id': song.song_id,
        'title': song.title,
        'artist': song.artist
    }
    return json.dumps(payload)


def _serialize_to_xml(song):
    song_element = et.Element(
        "song", attrib={"id": song.song_id}
    )
    title = et.SubElement(song_element, "title")
    title.text = song.title
    artist = et.SubElement(song_element, "artist")
    artist.text = song.artist
    return et.tostring(song_element, encoding="unicode")

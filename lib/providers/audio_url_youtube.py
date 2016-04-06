# -*- coding: utf-8 -*-
from third import youtube_dl


def run(hash,ump,referer=""):
	ydl = youtube_dl.YoutubeDL({'format': 'bestaudio/best',"quiet":True})

	with ydl:
		result = ydl.extract_info(
			'http://www.youtube.com/watch?v=%s'%hash,
			download=False # We just want to extract the info
		)

	if 'entries' in result:
		# Can be a playlist or a list of videos
		audio = result['entries'][0]
	else:
		# Just a video
		audio = result

	return {"audio":audio["url"]}
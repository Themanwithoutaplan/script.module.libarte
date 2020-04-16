# -*- coding: utf-8 -*-
import libartehbbtvjsonparser as libArteJsonParser
from libmediathek4 import lm4


import libartewebjsonparser

baseApi = 'http://www.arte.tv/hbbtvv2/services/web/index.php'


class libarte(lm4):
	def __init__(self):
		self.parser = libartewebjsonparser.APIParser()
		self.defaultMode = 'libArteListMain'

		self.modes = {
			'libArteListMain': self.libArteListMain,
			'libArteListDataCode': self.libArteListDataCode,
			'libArteListDataVideoType': self.libArteListDataVideoType,
			'libArteListCollection': self.libArteListCollection,
			'libArteListShows': self.libArteListShows,
			'libArteListVideos': self.libArteListVideos,
			
			'libArteThemes': self.libArteThemes,
			'libArteListDate': self.libArteListDate,
			'libArteListDateVideos': self.libArteListDateVideos,
			'libArteSearch': self.libArteSearch,
			'libArteListSearch': self.libArteListSearch,
		}
		self.playbackModes = {
			'libArtePlay':self.libArtePlay,
			'libArtePlayWeb':self.libArtePlayWeb,
		}
		
	def libArteListMain(self):
		#return self.parser.parseHome()
		l = []
		l.append({'metadata':{'name':self.translation(32032)}, 'params':{'mode':'libArteListDataVideoType', 'data':'VIDEO_LISTING', 'videoType':'MOST_RECENT'}, 'type':'dir'})
		l.append({'metadata':{'name':self.translation(32031)}, 'params':{'mode':'libArteListDataVideoType', 'data':'VIDEO_LISTING', 'videoType':'MOST_VIEWED'}, 'type':'dir'})
		l.append({'metadata':{'name':self.translation(32132)}, 'params':{'mode':'libArteListShows','uri':'magazines'}, 'type':'dir'})
		#l.append({'metadata':{'name':'shows'}, 'params':{'mode':'libArteListCode', 'code':'listing_MAGAZINES'}, 'type':'dir'})
		l.append({'metadata':{'name':self.translation(32133)}, 'params':{'mode':'libArteListDate', 'code':'listing_MAGAZINES'}, 'type':'dir'})
		l.append({'metadata':{'name':self.translation(32033)}, 'params':{'mode':'libArteListDataVideoType', 'data':'VIDEO_LISTING', 'videoType':'LAST_CHANCE'}, 'type':'dir'})
		#l.append({'metadata':{'name':self.translation(32033)}, 'params':{'mode':'libArteListVideos', 'uri':'highlights_category'}, 'type':'dir'})
		return {'items':l,'name':'root'}
		

	def libArteListShows(self):
		return self.parser.parsePagesShows(self.params['uri'])

	def libArteListVideos(self):
		return self.parser.parsePagesVideos(self.params['uri'])

	def libArteListDataCode(self):
		return self.parser.parseDataCode(self.params['code'])

	def libArteListDataVideoType(self):
		return self.parser.parseDataVideoType(self.params['data'],self.params['videoType'])

	def libArteListCollection(self):
		return self.parser.parseCollection(self.params['collectionId'])

	def libArteListDate(self):
		return self.populateDirDate('libArteListDateVideos')

	def libArteListDateVideos(self):
		return self.parser.parseDate(self.params['yyyymmdd'])

	def libArtePlayWeb(self):
		import libarteplayerjsonparser
		player = libarteplayerjsonparser.PlayerParser()
		return player.parseVideo(self.params['programId'])



	def libArteThemes(self):
		return self.parser.getPlaylists()
			
	#def libArteListDateVideos(self):
	#	return self.parser.getDateNew(self.params['yyyymmdd'])
		
	def libArteSearch(self):
		#search_string = libMediathek.getSearchString()
		return self.parser.getSearch(search_string)

	def libArteListSearch(self,searchString=False):
		if not searchString:
			searchString = self.params['searchString']
		return search(searchString)
			
	def libArtePlay(self):
		#return libArteJsonParser.getVideoUrl(self.params['url'])
		return self.parser.getVideoUrlWeb(self.params['url'])

		
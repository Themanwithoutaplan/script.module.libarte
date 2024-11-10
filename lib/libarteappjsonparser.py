import requests

class AppParser:
    def __init__(self):
        self.result = {'items':[],'pagination':{'currentPage':0}}
        self.lang = 'de'
        self.langGuide = 'de'

        self.baseURLApp = 'https://api-cdn.arte.tv/api/emac/v3/'
        self.token = 'YTEwZWE3M2UxMTVmYmRjZmE0YTdmNjA4ZTI2NDczZDU3YjdjYmVmMmRmNGFjOTM3M2RhNTM5ZjIxYmI3NTc1Zg'
        self.baseURLAppPreprod = 'https://api-preprod.arte.tv/api/emac/v3/'
        self.tokenPreprod = 'MWZmZjk5NjE1ODgxM2E0MTI2NzY4MzQ5MTZkOWVkYTA1M2U4YjM3NDM2MjEwMDllODRhMjIzZjQwNjBiNGYxYw'
        self.baseURLAppDev= 'https://emac-dev.arte.tv/api/emac/v3'
        self.tokenDev = ''


    def parseCollection(self,collectionId):
        #https://api-cdn.arte.tv/api/emac/v3/pl/app/zones/collection_videos?id=RC-014296&page=2
        #print(f'{self.basebaseURLAppURL}/{self.lang}/app/zones/collection_videos?id={collectionId}&page=1&limit=100')
        print(f'{self.baseURLApp}/{self.lang}/app/zones/collection_videos?id={collectionId}&page=1&limit=100')
        j = requests.get(f'{self.baseURLApp}/{self.lang}/app/zones/collection_videos?id={collectionId}&page=1&limit=100', headers=headers)
        print(j.text)

        j = j.json()

        for item in j['data']:
            d = {'type':'dir', 'params':{'mode':'libArtePlayWeb'}, 'metadata':{'art':{}}, 'type': 'video'}

            d['metadata']['name'] = item['title']
            d['metadata']['duration'] = item['duration']
            d['metadata']['mpaa'] = item['ageRating']
            d['metadata']['art']['thumb'] = item['images']['landscape']['resolutions'][2]['url']

            d['params']['programId'] = item['programId']
            self.result['items'].append(d)
        return self.result

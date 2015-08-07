import urllib
import json

class user_analyze:
    def get_user_id(self, api, user_id):
        raw_data = urllib.urlopen(api + 'users.get?user_ids=%s&v=5.26' % user_id)
        data = json.load(raw_data)
        return data['response'][0]['id'], data['response'][0]['first_name'], data['response'][0]['last_name']

    def get_user_friends(self, api, user_id):
            raw_data = urllib.urlopen(api + 'friends.get?user_id=%s&v=5.26' % user_id)
            data = json.load(raw_data)
            return data['response']['items']
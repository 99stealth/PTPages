#!/usr/bin/env python2.7

import urllib
import json

API = "https://api.vk.com/method/"
default_id = "dm"

def get_user_id(uid=default_id):
    raw_data = urllib.urlopen(API + 'users.get?user_ids=%s&v=5.26' % uid)
    data = json.load(raw_data)
    print data['response'][0]['first_name'], data['response'][0]['last_name']
    return data['response'][0]['id']

uid = get_user_id()

def get_user_friends(uid):
    raw_data = urllib.urlopen(API + 'friends.get?user_id=%s&v=5.26' % uid)
    data = json.load(raw_data)
    return data['response']['items']

friends = get_user_friends(uid)

print friends

# with open('friends_of_%s.json' %uid, 'w+') as fp:
#     json.dump(friends, fp)
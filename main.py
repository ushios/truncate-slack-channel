#coding: utf-8

import urllib
import urllib2
import json
import time
import os

delete_url = "https://slack.com/api/chat.delete"
hist_url = "https://slack.com/api/channels.history"
token = os.getenv("SLACK_TOKEN", "empty")
channel = os.getenv("CHANNEL_ID", "empty")

delete_params = {'token':token,
          'channel':channel
}
hist_params = {'token':token,
          'channel':channel,
          'count' : '1000',
}

hist_params = urllib.urlencode(hist_params)

req = urllib2.Request(hist_url)
req.add_header('Content-Type', 'application/x-www-form-urlencoded')
req.add_data(hist_params)

res = urllib2.urlopen(req)

body = res.read()
data = json.loads(body)


for m in data["messages"]:
  delete_params['ts'] = m["ts"]
  enc_params = urllib.urlencode(delete_params)

  req = urllib2.Request(delete_url)
  req.add_header('Content-Type', 'application/x-www-form-urlencoded')
  req.add_data(enc_params)


  res = urllib2.urlopen(req)

  body = res.read()
  print(body)
  #連続で送りすぎるとエラーになるので1秒待機
  time.sleep(1)

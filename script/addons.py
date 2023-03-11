from mitmproxy import http
from mitmproxy.script import concurrent
import time, requests, logging

class Foo123: # https://docs.mitmproxy.org/stable/addons-examples/
    #@concurrent
    def __init__(self):
        self.id=time.time()
    def response(self, flow: http.HTTPFlow) -> None:
        if flow.request.host == 'api.vistopia.com.cn' and 'play_list' in flow.request.path_components:
            logging.error('[Info] Send response from %s to endpoint /play_list', flow.request.host)
            requests.post('http://127.0.0.1:5000/play_list'     , json=flow.response.json())
        elif flow.request.host == 'vod.volcengineapi.com':
            logging.error('[Info] Send response from %s to endpoint /audio_file_url', flow.request.host)
            requests.post('http://127.0.0.1:5000/audio_file_url', json=flow.response.json())

addons = [Foo123()]
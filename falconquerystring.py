import json
import falcon

class AboutResource(object):
    def on_get(self, req, resp):
        n1=req.get_param('no1')
        n2=req.get_param('no2')
        answer=int(n1)+int(n2)
        about = {
            'Author':answer
        }
        
        resp.body = json.dumps(about)

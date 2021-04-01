import json
import falcon

class AboutResource(object):
    def on_get(self, req, resp):
        about = {
            'Author':'Madusudhanan'
        }
        
        resp.body = json.dumps(about)

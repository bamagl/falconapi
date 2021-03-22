import json
import falcon

class AboutResource(object):
    def on_get(self, req, resp):
        about = {
            'Author':'Madusudhanan'
        }
        print(type(about))
        # Create a JSON representation of the resource
        resp.body = json.dumps(about)
import json
import falcon
from .fourcolourcode import findResistance

class ResistanceResource(object):
    def on_get(self, req, resp):
        c1=req.get_param('colour1')
        c2=req.get_param('colour2')
        c3=req.get_param('colour3')
        c4=req.get_param('colour4')
        answer=findResistance(c1,c2,c3,c4)
        add = {
            'Resistance':answer
        }
        
        resp.body = json.dumps(add)

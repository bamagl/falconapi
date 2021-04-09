import falcon

from .resistance import ResistanceResource

api = application = falcon.API()

api.add_route('/resistance', ResistanceResource())

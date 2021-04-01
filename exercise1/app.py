import falcon

from .about import AboutResource

api = application = falcon.API()
about = AboutResource()
api.add_route('/about', about)
import ckan.lib.base as base
import ckan.lib.helpers as h
import ckan.plugins as p
import ckan.plugins.toolkit as tk
from ckan.lib.base import BaseController, config
import jinja2
from ckan.common import _, c, g, request
from validate_email import validate_email

abort = base.abort
render = base.render

class VdsController(BaseController):
    def faq(self, context=None):
        print h.lang()
        #error_summary = errors
        #vars = {'data': data, 'errors': errors, 'error_summary': error_summary}
        return render('ckanext/vds/faq.html')
    

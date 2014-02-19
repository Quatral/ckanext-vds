import ckan.plugins as p
import ckan.plugins.toolkit as toolkit

class VdsPlugin(p.SingletonPlugin):
    # Declare that this class implements IConfigurer.

    p.implements(p.IRoutes, inherit=True)
    p.implements(p.IConfigurer, inherit=True)
    
    def update_config(self, config):

        # Add this plugin's templates dir to CKAN's extra_template_paths, so
        # that CKAN will use this plugin's custom templates.
        # 'templates' is the path to the templates dir, relative to this
        # plugin.py file.
        toolkit.add_template_directory(config, 'templates')
        toolkit.add_public_directory(config, 'public')
        
    def after_map(self, map):
        map.connect('faq', '/faq',
            controller='ckanext.vds.controller:VdsController',
            action='faq')
        map.connect('faq', '/foire-aux-questions.html',
            controller='ckanext.vds.controller:VdsController',
            action='faq')
        map.connect('licence', '/licence',
            controller='ckanext.vds.controller:VdsController',
            action='licence')
        map.connect('licence', '/licence.html',
            controller='ckanext.vds.controller:VdsController',
            action='licence')
        
        '''translated maps'''
        map.connect('nous-joindre', '/nous-joindre.html',
            controller='ckanext.contact_us.controller:ContactUsController',
            action='index')
        map.connect('nous-joindre', '/nous-joindre',
            controller='ckanext.contact_us.controller:ContactUsController',
            action='index')
        return map  

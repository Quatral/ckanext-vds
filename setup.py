from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(
	name='ckanext-vds',
	version=version,
	description="Theme and pages for the city of Sherbrooke",
	long_description="""\
	""",
	classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
	keywords='',
	author='Kenny Dorman',
	author_email='kdorman@quatral.com',
	url='http://quatral.com',
	license='',
	packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
	namespace_packages=['ckanext', 'ckanext.vds'],
	include_package_data=True,
	zip_safe=False,
	install_requires=[
		# -*- Extra requirements: -*-
	],
	entry_points={
    	'babel.extractors': [
    		'ckan = ckan.lib.extract:extract_ckan',
		],
		'ckan.plugins' : [
			'vds=ckanext.vds.plugin:VdsPlugin',
		]
	}
)

import os
from distutils.core import setup

def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

setup(
    name="pcf_storyscapes",
    version="0.1",
    author="",
    author_email="",
    description="pcf_storyscapes, based on GeoNode",
    long_description=(read('README.rst')),
    # Full list of classifiers can be found at:
    # http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 1 - Planning',
    ],
    license="BSD",
    keywords="pcf_storyscapes geonode django",
    url='https://github.com/MapStory/pcf_storyscapes',
    packages=['pcf_storyscapes',],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'gunicorn==19.4.5',
        'whitenoise==2.0.6'
    ],
)

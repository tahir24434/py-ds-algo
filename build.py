from pybuilder.core import use_plugin, init, Author

use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.install_dependencies")
use_plugin("python.flake8")
use_plugin("python.distutils")

name = "pdsa"
url = 'https://github.com/tahir24434/py-ds-algo'
information = "Please visit {url}".format(url=url)
authors = [Author('Tahir Rauf', 'tahir.rauf1@gmail.com')]
license = 'Apache 2.0'
summary = "Python data structure library for coding interviews"
version = '0.1.0'
default_task = "publish"


@init
def set_properties(project):
    project.set_property('flake8_break_build', True)
    project.set_property('flake8_include_scripts', True)
    project.set_property('flake8_include_test_sources', True)
    project.set_property('flake8_max_line_length', 120)
    project.set_property('flake8_verbose_output', True)
    project.set_property('distutils_classifiers', [
        'Development Status:: 5 - Production',
        'Intended Audience :: Developers'
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6.0',
        'Topic :: Software Development :: Kubernetes',
        'Topic :: Software Development :: Python library',
    ])
    project.set_property("distutils_upload_repository", "pdsa")
    # project.build_depends_on('kubernetes', '2.0.0a1')
    project.build_depends_on('nose')

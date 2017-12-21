#!/usr/bin/env python

from setuptools import setup
from setuptools.command.install import install as _install


class install(_install):
    def pre_install_script(self):
        pass

    def post_install_script(self):
        pass

    def run(self):
        self.pre_install_script()

        _install.run(self)

        self.post_install_script()

if __name__ == '__main__':
    setup(
        name='pdsa',
        version='0.1.0',
        description='''Python DataStructures library''',
        long_description='''''',
        author="Tahir Rahif",
        author_email="tahir.rauf1@gmail.com",
        license='Apache 2.0',
        url='https://github.com/tahir24434/py-ds-alog',
        scripts=[],
        packages=[
            'pdsa',
            'pdsa.lib'
        ],
        py_modules=[],
        classifiers=[
            'Development Status:: 5 - Production',
            'Intended Audience :: DevelopersLicense :: OSI Approved :: '
            'MIT License',
            'Programming Language :: Python',
            'Programming Language :: Python :: 3.6.0',
            'Topic :: Software Development :: Data Structures',
        ],
        entry_points={},
        data_files=[],
        package_data={},
        install_requires=[],
        dependency_links=[],
        zip_safe=True,
        cmdclass={'install': install},
    )
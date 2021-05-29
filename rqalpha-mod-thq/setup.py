# from pip.req import parse_requirements 这样的话如果pip版本较高会报错
try: # for pip >= 10
    from pip._internal.req import parse_requirements
except ImportError: # for pip <= 9.0.3
    from pip.req import parse_requirements

from setuptools import (
    find_packages,
    setup,
)

setup(
    name='rqalpha-mod-thq',     # mod名
    version="0.1.0",
    description='RQAlpha Mod to say hello',
    packages=find_packages(exclude=[]),
    author='Chengrui Gu',
    author_email='cg487@cornell.edu',
    license='Apache License v2',
    package_data={'': ['*.*']},
    url='https://github.com/ChengruiGu/THQ_highfreq.git',
    install_requires=[str(ir.requirement) for ir in parse_requirements("requirements.txt", session=False)],
    zip_safe=False,
    classifiers=[
        'Programming Language :: Python',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: Unix',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)

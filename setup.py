from setuptools import setup, find_packages

setup(
    name='pox',
    version='0.0.0',
    author='Murphy McCauley',
    author_email='murphy.mccauley@gmail.com',
    packages=find_packages(exclude='test'),
    scripts=['pox.sh'],
    url='http://www.noxrepo.org/pox/about-pox/',
    license='IDUNNO',
    description='pox controller',
    long_description=open('README').read(),
    install_requires=[
        'distribute'
    ],
    classifiers=[
        'OpenFlow :: Controller',
    ],
    keywords='OpenFlow controller networking SDN'
)

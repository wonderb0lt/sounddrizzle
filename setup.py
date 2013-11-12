from distutils.core import setup

setup(
    name='SoundDrizzle',
    version='0.0.1',
    description='An easy client to add SoundCloud tracks to your offline collection',
    long_description=open('README.rst').read(),
    license='LICENSE',
    author='Patrick Stegmann (aka. @wonderb0lt)',
    author_email='code@patrick-stegmann.de',
    url='https://github.com/wonderb0lt/sounddrizzle',
    packages=['sounddrizzle'],
    requires=['mutagen', 'docopt'],
    scripts=['scripts/drizzle']
)
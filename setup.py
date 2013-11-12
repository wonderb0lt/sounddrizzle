from distutils.core import setup

setup(
    name='SoundDrizzle',
    version='0.0.2',
    description='An easy client to add SoundCloud tracks to your offline collection',
    long_description=open('README.rst').read(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent'
    ],
    license='LICENSE',
    author='Patrick Stegmann (aka. @wonderb0lt)',
    author_email='code@patrick-stegmann.de',
    url='https://github.com/wonderb0lt/sounddrizzle',
    packages=['sounddrizzle'],
    requires=['mutagen', 'docopt'],
    scripts=['scripts/drizzle']
)
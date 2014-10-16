from setuptools import setup

setup(
    name='SoundDrizzle',
    version='1.0.1',
    description='An easy client to add SoundCloud tracks to your offline collection',
    long_description=open('README.md').read(),
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
    install_requires=[
        'mutagen',
        'Click',
        'requests',
        'termcolor',
    ],
    py_modules=['sounddrizzle'],
    entry_points='''
        [console_scripts]
        drizzle=sounddrizzle:pour
    ''',
)
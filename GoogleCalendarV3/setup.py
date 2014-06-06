from distutils.core import setup

setup(
    name='GoogleCalendarV3',
    version='0.1.0',
    author='Ashutosh Priyadarshy',
    author_email='static@siftcal.com',
    packages=['google_calendar_v3', 'google_calendar_v3.test'],
    scripts=['bin/example.py'],
    url='http://pypi.python.org/pypi/GoogleCalendarV3/',
    license='LICENSE.txt',
    description='Python Client for Google Calendar API V3.',
    long_description=open('README.txt').read(),
    install_requires=[
        "requests-oauthlib >= 0.4.0",
    ],
)

from distutils.core import setup

setup(
    name='GoogleCalendarV3',
    version='0.1.2',
    author='Ashutosh Priyadarshy',
    author_email='static@siftcal.com',
    packages=['google_calendar_v3', 'google_calendar_v3.test'],
    scripts=['bin/example.py'],
    url='http://www.github.com/priyadarshy/google-calendar-v3/',
    license='LICENSE.txt',
    description='Python Client for Google Calendar API V3.',
    long_description=open('README.txt').read(),
    install_requires=[
        "requests >= 2.3.0",
        "requests-oauthlib >= 0.4.0"
    ],
)

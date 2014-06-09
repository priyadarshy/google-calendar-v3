from distutils.core import setup

setup(
    name='GoogleCalendarV3',
    version='0.1.7',
    author='Ashutosh Priyadarshy',
    author_email='static@siftcal.com',
    packages=['google_calendar_v3'],
    url='http://www.github.com/priyadarshy/google-calendar-v3/',
    license='LICENSE.txt',
    description='Python Client for Google Calendar API V3.',
    long_description=open('README.txt').read(),
    install_requires=[
        "requests >= 2.3.0",
        "requests-oauthlib >= 0.4.0"
    ],
)

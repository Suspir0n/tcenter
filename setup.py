from setuptools import setup
from settings import NAME, VERSION, DESCRIPTION, LINCENSE, PACKAGES, AUTHOR, INSTALL_REQUIRES, SETUP_REQUIRES, TESTS_REQUIRES, TESTS_SUITE, AUTHOR_EMAIL, DOWNLOAD_URL, URL

setup(
    name=NAME,
    packages=PACKAGES,
    version=VERSION,
    description=DESCRIPTION,
    author=AUTHOR,
    license=LINCENSE,
    install_requires=INSTALL_REQUIRES,
    setup_requires=SETUP_REQUIRES,
    tests_requires=TESTS_REQUIRES,
    tests_suite=TESTS_SUITE,
    author_email=AUTHOR_EMAIL,
    url=URL,
    download_url=DOWNLOAD_URL,
)
from setuptools import find_packages, setup


setup(
    name='tcenter',
    packages=find_packages(include=['tcenter']),
    version='0.1.4.2',
    description='A library for center titles',
    author='Evandro Silva',
    license='MIT',
    install_requires=[],
    setup_requires=[],
    tests_requires=['pytest==6.2.3'],
    tests_suite=['tests'],
    author_email='evandrojunior1615@gmail.com',
    url='https://github.com/Suspir0n/tcenter',
    download_url='https://github.com/Suspir0n/tcenter/archive/refs/tags/0.1.4.2.tar.gz',
    python_requires='>=3.6',
    maintainer='Evandro Silva',
    maintainer_email='evandrojunior1615@gmail.com',
)
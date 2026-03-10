from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='hvac_intelligence',
    version='0.1.0',
    description='AI-powered HVAC optimization platform',
    author='HVAC Intelligence Contributors',
    license='MIT',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=requirements,
    python_requires='>=3.8',
)

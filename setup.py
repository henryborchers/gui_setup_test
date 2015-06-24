from setuptools import setup, find_packages

setup(
    name='testgui',
    version='0.1.5',
    packages=['tester'],
    url='',
    license='',
    author='California Audio Visual Preservation Project',
    author_email='hborcher@berkeley.edu',
    description='',
    zip_safe=False,
    entry_points={"console_scripts": ["guiTest = tester.testGui:main"]}
)

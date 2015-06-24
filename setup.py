from setuptools import setup, find_packages

setup(
    name='gui_setup_test',
    version='0.1.4',
    packages=['tester'],
    url='',
    license='',
    author='California Audio Visual Preservation Project',
    author_email='hborcher@berkeley.edu',
    description='',
    zip_safe=False,
    entry_points={"gui_scripts": ["guiTest = tester.testGui:main"]}
)

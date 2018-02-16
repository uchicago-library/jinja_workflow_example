from setuptools import setup, find_packages


def readme():
    with open("README.md", 'r') as f:
        return f.read()


setup(
    name="jinja_workflow_example",
    description="A repository for testing jinja focused workflows with a dedicated front end team",
    version="0.0.1",
    long_description=readme(),
    author="Brian Balsamo",
    author_email="brian@brianbalsamo.com",
    packages=find_packages(
        exclude=[
        ]
    ),
    include_package_data=True,
    url='https://github.com/bnbalsamo/jinja_workflow_example',
    install_requires=[
    ],
    tests_require=[
        'pytest'
    ],
    test_suite='tests'
)

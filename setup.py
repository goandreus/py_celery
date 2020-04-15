try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup

    def find_packages():
        return ['redisbeat']

install_requires = [
    "celery == 4.1.0",
    "redis == 2.10.6",
    "tenacity >= 5.0.3",
    "mock >= 2.0.0"
]

setup(
    version="1.0.0",
    packages=find_packages(),
    install_requires=install_requires,
    include_package_data=True,
)

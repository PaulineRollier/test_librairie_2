from setuptools import setup
import os
import mathematique

setup(
    name="pkg_test_mathematique_testpi_2",
    version=mathematique.__version__,
    packages=["mathematique"],
    install_requires=["pytest", "sphinx", "sphinx_rtd_theme", "ghp-import"],
)

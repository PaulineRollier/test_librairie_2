from setuptools import setup
import os
import mathematique

setup(
    name="pkg_test_mathematique_testpi_2",
    version=mathematique.__version__,
    packages=["mathematique"],
    description="demonstration de creation d'un package Python",
    long_description=open(os.path.join(os.path.dirname(__file__), "README.txt")).read(),
    install_requires=["pytest", "sphinx", "sphinx_rtd_theme", "ghp-import"],
)

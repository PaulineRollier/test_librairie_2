from setuptools import setup
import os
import mathematique

setup(
    name="pkg_test_mathematique_testpi_2",
    version=mathematique.__version__,
    packages=["mathematique"],
    description="A User Parameter-free Bayesian Framework for Uplift Modeling",
    long_description=open(os.path.join(os.path.dirname(__file__), "README.md")).read(),
    install_requires=["pytest", "sphinx", "sphinx_rtd_theme", "ghp-import"],
)

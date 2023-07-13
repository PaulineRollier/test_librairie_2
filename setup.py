from setuptools import setup
import mathematique

setup(
    name="pkg_test_mathematique_testpi_2",
    version=mathematique.__version__,
    packages=["mathematique"],
    description="A User Parameter-free Bayesian Framework for Uplift Modeling",
    long_description=open('README.md').read(),
    install_requires=["pytest", "sphinx", "sphinx_rtd_theme", "ghp-import"],
)

from setuptools import setup
import mathematique

try:
    import pypandoc
    long_description = pypandoc.convert_file('README.md', 'rst')
except(IOError, ImportError):
    long_description = open('README.md').read()
        
setup(
    name="pkg_test_mathematique_testpi_2",
    version=mathematique.__version__,
    packages=["mathematique"],
    description="A User Parameter-free Bayesian Framework for Uplift Modeling",
    long_description=long_description,
    install_requires=["pytest", "sphinx", "sphinx_rtd_theme", "ghp-import"],
)

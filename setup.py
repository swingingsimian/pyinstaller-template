from setuptools import find_packages, setup

setup(
    name="pyinstaller-template",
    description="Pyinstaller Template",
    packages=find_packages(exclude=["tests"]),
    #install_requires=[],
    use_scm_version=True,
    setup_requires=["setuptools_scm"],
)

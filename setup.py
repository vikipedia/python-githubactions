from distutils.core import setup


def requirements():
    with open("requirements.txt") as f:
        return [line.strip() for line in f]


setup(
    name="python_pkg",
    version="1.0.1",
    description="test for github actions",
    long_description="README.md",
    long_description_content_type="text/markdown",
    url="https://test.site.in",
    maintainer="Vikrant Patil",
    maintainer_email="vikrant.patil@gmail.com",
    license="MIT LICENSE",
    classifiers=[
        "License :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
    ],
    packages=["python_pkg"],
    include_package_data=True,
    package_data={'': ['data/*.txt']},
    install_requires=requirements(),
    entry_points={"console_scripts": ["say_hello=python_pkg.hello:app"]}
)

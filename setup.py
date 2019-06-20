import setuptools

with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name="s_aes",
    version="0.0.1",
    author="Larissa Lopes",
    author_email="lopes.larissalopes@gmail.com",
    description="Simplified AES implementation in Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://bitbucket.org/lopeslarissa/simple-aes/",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        # "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        'console_scripts': ['encrypt=s_aes.encrypt:main'],
    },
)

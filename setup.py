import setuptools

with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name="saeslib",
    version="1.0.0",
    author="Larissa Lopes",
    author_email="lopes.larissalopes@gmail.com",
    description="Simplified AES implementation in Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lopeslarissa/saeslib",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    install_requires=['numpy', 'pyfinite'],
    python_requires='>=3',
    entry_points={
        'console_scripts': [
            'encrypt=s_aes.encrypt:main',
            'decrypt=s_aes.decrypt:main',
            'tests=tests.tests:main'
        ],
    },
)

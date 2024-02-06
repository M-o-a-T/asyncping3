import setuptools

with open('README.md') as f:
    long_desc = f.read()

setuptools.setup(
    name='asyncping3',
    use_scm_version={"version_scheme": "guess-next-dev", "local_scheme": "dirty-tag"},
    setup_requires=["setuptools_scm"],
    description='A pure python3 version of ICMP ping implementation using raw socket.',
    long_description=long_desc,
    long_description_content_type='text/markdown',
    url='https://github.com/M-o-a-T/ping3',
    author='Matthias Urlichs',
    author_email='matthias@urlichs.de',
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'Topic :: System :: Networking',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
    keywords='python3 ping icmp socket tool',
    packages=["asyncping3"],
    python_requires='>=3',
    install_requires=["anyio >= 3"],
    extras_require={
        'dev': ['build', 'twine', 'pycodestyle'],
    },
    package_data={},
    data_files=[],
    entry_points={
        'console_scripts': ['pping=asyncping3._main:main'],
    },
)

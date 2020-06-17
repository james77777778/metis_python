from setuptools import setup

setup(
    name='metis-python',
    version='0.1',
    description='Wrapper for metis to support lastest networkx.',
    url='https://github.com/james77777778/python_metis',
    author="Hong-Yu Chiu",
    author_email="james77777778@gmail.com",
    install_requires=["networkx"],
    license='MIT',
    packages=['metispy'],
    zip_safe=False,
    keywords=['metis', "graph", "partition"],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ]
)

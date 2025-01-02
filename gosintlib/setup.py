from setuptools import setup, find_packages

with open("README.md", "r") as f:
    description = f.read()

setup(
    name='gosintlib',
    version='3.0',
    packages=find_packages(),
    install_requires=[
        'requests==2.32.3',
        'phonenumbers==8.13.52',
        'dnspython==2.7.0',
    ],
    long_description=description,
    long_description_content_type="text/markdown",
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)

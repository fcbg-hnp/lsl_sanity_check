from setuptools import find_packages, setup

setup(
    name='lsl_sanity_check',
    version='0.9dev',
    author='Arnaud Desvachez',
    author_email='arnaud.desvachez@gmail.com',
    license='The GNU General Public License',
    url='https://github.com/fcbg-hnp/lsl_sanity_check',
    description='Check the recorded LSL streams sanity.',
    long_description=open('README.md').read(),
    python_requires='>=3.6',
    packages=find_packages(),
    install_requires=[
        'pyxdf',
        'numpy'
    ]
)

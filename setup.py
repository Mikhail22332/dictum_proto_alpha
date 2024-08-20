from setuptools import setup, find_packages

setup(
    name='dictum-proto',
    version='0.4.0',
    packages=find_packages(),
    install_requires=[
        'protobuf',
        'grpcio',
        'grpcio-tools',
    ],
    url='https://github.com/Mikhail22332/dictum_proto_alpha',
    author='loopnyapy,skyfet',
    author_email='da.eto.deniska@gmail.com',
    description='Protobuf api for Dictum'
)
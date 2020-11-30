from setuptools import setup

setup(
    name='TankRemote',
    version='1.0',
    description='Remote controller application for a WiFi tank',
    author='Michael Cooper, Hunter Allen',
    author_email='mic159@gmail.com, allenhm@gmail.com',
    packages=['tank'],
    python_requires='>=3.6',
    install_requires=[
    #    'pygtk'
    ],
    entry_points={
        'gui_scripts': [
            'tank_remote = tank.main:main'
        ]
    }
)
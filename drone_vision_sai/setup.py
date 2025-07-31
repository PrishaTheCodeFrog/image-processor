from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'image_processor_setup'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob(os.path.join('launch', '*launch.[pxy][yma]*')))
    ],
    install_requires=[
        'setuptools',
        'opencv-python', # Dependency for OpenCV
        'numpy', # Dependency for NumPy
        'scipy', # Dependency for SciPy
    ],
    zip_safe=True,
    maintainer='Prisha Kansal',
    maintainer_email='prishask45@gmail.com',
    description='ROS 2 node for image-based line following.',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'line_follower_node = line_follower.line_follower_node:main',
        ],
    },
)
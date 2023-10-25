import os
from setuptools import setup
from setuptools import setup, find_packages

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
   README = readme.read()

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='yolo_data_vis',
    version='1.0a0',
    packages=find_packages(),

    download_url='',

    entry_points={'console_scripts': [
        'yolo_data_vis=yolo_data_vis.vis_opencv:main',
         'yolo_data_vis_jupyter=yolo_data_vis.vis_display:main',
        ]},
    

    install_requires=[ 
                     'docopt',
                     'numpy', 
    ],

    include_package_data=True,
    #license='MIT License',
    description="",
    zip_safe=False,

    long_description=README,
    long_description_content_type='text/markdown',

    python_requires='>=3.8',

)
from setuptools import setup

setup(name='subsync',
      version='0.1.0',
      description='Synchronize your subtitles with mahcine learning',
      classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Topic :: Multimedia :: Sound/Audio :: Analysis',
        'Topic :: Multimedia :: Sound/Audio :: Speech',
      ],
      keywords='subtitle synchronize machine learning',
      platforms=["Independent"],
      scripts=['bin/subsync'],
      include_package_data=True,
      url='https://github.com/tympanix/subsync',
      author='tympanix',
      author_email='tympanix@gmail.com',
      license='MIT',
      packages=['subsync'],
      install_requires=[
          'tensorflow==1.5.1',
      ],
      zip_safe=False)

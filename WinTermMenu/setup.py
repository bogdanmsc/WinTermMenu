import setuptools

setuptools.setup(
      include_package_data=True,
      name='WinTermMenu',
      version='1.0.dev0',
      description='A simple menu for cmd',
      url="https://github.com/bogdanmsc/WinTermMenu",
      author='Bogdan',
      author_email='bogdan.valery.msc@gmail.com',
      install_requires=['keyboard', 'colorama'],
      long_description='Allows you to create simple menus in the Windows command line with keyboard control.',
      long_description_content_type="text/markdown",
      classifiers=[
            "Programming Language :: Python :: 3",
            "Operating System :: OS Independent",
      ],
)

# NOTE: See the README file for a list of dependencies to install.
from setuptools import setup, Extension

zigbee_crypt = Extension('zigbee_crypt',
                         sources = ['zigbee_crypt/zigbee_crypt.c'],
                         libraries = ['gcrypt'],
                         include_dirs = ['/usr/local/include', '/usr/include', '/sw/include/', 'zigbee_crypt'],
                         library_dirs = ['/usr/local/lib', '/usr/lib','/sw/var/lib/']
                         )

setup(scripts = ['tools/zbdump', 'tools/zbgoodfind', 'tools/zbid', 'tools/zbreplay',
                 'tools/zbconvert', 'tools/zbdsniff', 'tools/zbstumbler', 'tools/zbassocflood',
                 'tools/zbscapy', 'tools/zbwireshark', 'tools/zbkey',
                 'tools/zbwardrive', 'tools/zbopenear', 'tools/zbfakebeacon',
                 'tools/zborphannotify', 'tools/zbpanidconflictflood', 'tools/zbrealign', 'tools/zbcat',
                 'tools/zbjammer', 'tools/kbbootloader'],
      ext_modules = [zigbee_crypt])

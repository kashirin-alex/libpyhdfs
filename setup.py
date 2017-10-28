from distutils.core import setup, Extension
import sys

include_dirs=['/usr/java/openjdk/include',
              '/usr/java/openjdk/include/linux/',
              '/usr/java/apache-hadoop/include/']
if 'PyPy' in sys.version:
  include_dirs.append('/opt/pypy2/include/')
  
pyhdfs = Extension('pyhdfs',
                   sources = ['src/pyhdfs.c'],
                   include_dirs = include_dirs,
                   libraries = ['hdfs'],
                   library_dirs = ['/usr/java/apache-hadoop/lib/native', '/usr/java/openjdk/jre/lib/amd64/server'],		
                   #runtime_library_dirs = ['/usr/java/apache-hadoop/lib/native', '/usr/java/openjdk/jre/lib/amd64/server'],
                   )
setup(name = 'PyHdfs',
      version = '0.1',
      author = 'Deng Zhiping',
      author_email = 'kofreestyler@gmail.com',
      description = "Python wrapper for libhdfs",
      long_description = """libpyhdfs is a Python extension module which wraps
                             the C API in libhdfs to access Hadoop file system""",
      url = "http://code.google.com/p/libpyhdfs",
      license = "Apache License 2.0", 
      platforms = ["GNU/Linux"],
      ext_modules = [pyhdfs])

from distutils.core import setup, Extension
import sys

include_dirs=['/usr/java/openjdk/include',
              '/usr/java/openjdk/include/linux/',
              '/usr/java/apache-hadoop/include/']
runtime_library_dirs = []
if 'PyPy' in sys.version:
  include_dirs.append('/opt/pypy'+str(sys.version_info.major)+'/include/')
  if sys.version_info.major < 3:
    runtime_library_dirs += ['/usr/java/apache-hadoop/lib/native', '/usr/java/openjdk/lib/server']
else:
  include_dirs.append('/usr/local/include/python'+str(sys.version_info.major)+'.'+str(sys.version_info.minor))

pyhdfs = Extension('pyhdfs',
                   sources = ['src/pyhdfs.c'],
                   include_dirs = include_dirs,
                   libraries = ['hdfs'],
                   library_dirs = ['/usr/java/apache-hadoop/lib/native', '/usr/java/openjdk/lib/server'],		
                   runtime_library_dirs = runtime_library_dirs,
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

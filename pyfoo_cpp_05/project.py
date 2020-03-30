import os
import subprocess

from sipbuild import Project


class FooProject(Project):
    """ A project that adds an additional configuration options to specify
    the locations of the foo header file and library.
    """

    def _build_foo(self):
        cwd = os.path.abspath('foo')
        subprocess.run(['make'], cwd=cwd, capture_output=True, check=True)

    def build(self):
        self._build_foo()
        super().build()

    def build_sdist(self, sdist_directory):
        self._build_foo()
        return super().build_sdist(sdist_directory)

    def build_wheel(self, wheel_directory):
        self._build_foo()
        return super().build_wheel(wheel_directory)

    def install(self):
        self._build_foo()
        super().install()

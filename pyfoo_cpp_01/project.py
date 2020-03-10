import os
import subprocess

from sipbuild import Option, Project


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
        super().build_sdist(sdist_directory)

    def build_wheel(self, wheel_directory):
        self._build_foo()
        super().build_wheel(wheel_directory)

    def install(self):
        self._build_foo()
        super().install()

    def get_options(self):
        """ Return the sequence of configurable options. """

        # Get the standard options.
        options = super().get_options()

        # Add our new options.
        inc_dir_option = Option('foo_include_dir',
                                help="the directory containing foo.h", metavar="DIR")
        options.append(inc_dir_option)

        lib_dir_option = Option('foo_library_dir',
                                help="the directory containing the foo library",
                                metavar="DIR")
        options.append(lib_dir_option)

        return options

    def apply_user_defaults(self, tool):
        """ Apply any user defaults. """

        # Ensure any user supplied include directory is an absolute path.
        if self.foo_include_dir is not None:
            self.foo_include_dir = os.path.abspath(self.foo_include_dir)
        else:
            self.foo_include_dir = os.path.abspath('foo')

        # Ensure any user supplied library directory is an absolute path.
        if self.foo_library_dir is not None:
            self.foo_library_dir = os.path.abspath(self.foo_library_dir)
        else:
            self.foo_library_dir = os.path.abspath('foo/bin')

        # Apply the defaults for the standard options.
        super().apply_user_defaults(tool)

    def update(self, tool):
        """ Update the project configuration. """

        # Get the foo bindings object.
        foo_bindings = self.bindings['pyfoocpp']

        # Use any user supplied include directory.
        if self.foo_include_dir is not None:
            foo_bindings.include_dirs = [self.foo_include_dir]

        # Use any user supplied library directory.
        if self.foo_library_dir is not None:
            foo_bindings.library_dirs = [self.foo_library_dir]

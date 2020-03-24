import os

from sipbuild import Option, Project


class FooProject(Project):
    """ A project that adds an additional configuration options to specify
    the locations of the foo header file and library.
    """

    def get_options(self):
        """ Return the sequence of configurable options. """

        tools = ['build', 'install', 'sdist', 'wheel']

        # Get the standard options.
        options = super().get_options()

        # Add our new options.
        inc_dir_option = Option('foo_include_dir',
                                help="the directory containing foo.h",
                                metavar="DIR",
                                default=os.path.abspath('foo'),
                                tools=tools)
        options.append(inc_dir_option)

        lib_dir_option = Option('foo_library_dir',
                                help="the directory containing the foo library",
                                metavar="DIR",
                                default=os.path.abspath('foo/bin'),
                                tools=tools)
        options.append(lib_dir_option)

        return options

    def apply_user_defaults(self, tool):
        """ Apply any user defaults. """

        # Apply the defaults for the standard options.
        super().apply_user_defaults(tool)

        # Ensure any user supplied include directory is an absolute path.
        self.foo_include_dir = os.path.abspath(self.foo_include_dir)

        # Ensure any user supplied library directory is an absolute path.
        self.foo_library_dir = os.path.abspath(self.foo_library_dir)

    def update(self, tool):
        """ Update the project configuration. """

        # Get the pyfoo bindings object.
        foo_bindings = self.bindings['pyfoo']

        # Use any user supplied include directory.
        if self.foo_include_dir is not None:
            foo_bindings.include_dirs = [self.foo_include_dir]

        # Use any user supplied library directory.
        if self.foo_library_dir is not None:
            foo_bindings.library_dirs = [self.foo_library_dir]

        super().update(tool)

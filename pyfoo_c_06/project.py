from sipbuild import Project


class FooProject(Project):
    def get_options(self):
        print('get_options()')
        options = super().get_options()
        return options

    def apply_user_defaults(self, tool):
        print('apply_user_defaults()')
        super().apply_user_defaults(tool)

    def apply_nonuser_defaults(self, tool):
        print('apply_nonuser_defaults()')
        super().apply_nonuser_defaults(tool)

    def update(self, tool):
        print('update()')
        super().update(tool)

    def build(self):
        print('build()')
        super().build()

    def build_sdist(self, sdist_directory):
        print('build_sdist()')
        return super().build_sdist(sdist_directory)

    def build_wheel(self, wheel_directory):
        print('build_wheel()')
        return super().build_wheel(wheel_directory)

    def install(self):
        print('install()')
        super().install()

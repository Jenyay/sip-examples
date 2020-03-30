%Module(name=foocpp, language="C++")
%DefaultEncoding "UTF-8"

class Foo {
%Docstring
Class example from C++ library
%End

    %TypeHeaderCode
    #include <foo.h>
    %End

    public:
        Foo(int, const char*);

        void set_int_val(int);
        %Docstring(format="deindented", signature="prepended")
            Set integer value
        %End

        int get_int_val();
        %Docstring(format="deindented", signature="prepended")
            Return integer value
        %End

        %Property(name=int_val, get=get_int_val, set=set_int_val)
        {
            %Docstring "deindented"
                The property for integer value
            %End
        };

        void set_string_val(const char*);
        %Docstring(format="deindented", signature="appended")
            Set string value
        %End

        char* get_string_val();
        %Docstring(format="deindented", signature="appended")
            Return string value
        %End

        %Property(name=string_val, get=get_string_val, set=set_string_val)
        {
            %Docstring "deindented"
                The property for string value
            %End
        };
};

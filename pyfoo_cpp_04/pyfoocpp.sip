%Module(name=foocpp, language="C++")
%DefaultEncoding "UTF-8"
%DefaultDocstringFormat "deindented"
%DefaultDocstringSignature "prepended"

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
        %Docstring
            Set integer value
        %End

        int get_int_val();
        %Docstring
            Return integer value
        %End

        %Property(name=int_val, get=get_int_val, set=set_int_val)
        {
            %Docstring
                The property for integer value
            %End
        };

        void set_string_val(const char*);
        %Docstring
            Set string value
        %End

        char* get_string_val();
        %Docstring
            Return string value
        %End

        %Property(name=string_val, get=get_string_val, set=set_string_val)
        {
            %Docstring
                The property for string value
            %End
        };
};

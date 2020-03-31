%Module(name=foocpp, language="C++")
%DefaultEncoding "UTF-8"
%DefaultDocstringFormat "deindented"
%DefaultDocstringSignature "prepended"

class Foo /PyName=Bar/ {
	%Docstring
	Class example from C++ library
	%End

    %TypeHeaderCode
    #include <foo.h>
    %End

    public:
        Foo(int, const char*);

        void set_int_val(int) /PyName=set_integer_value/;
        %Docstring
            Set integer value
        %End

        int get_int_val() /PyName=get_integer_value/;
        %Docstring
            Return integer value
        %End

        %Property(name=int_val, get=get_integer_value, set=set_integer_value)
        {
            %Docstring
                The property for integer value
            %End
        };

        void set_string_val(const char*) /PyName=set_string_value/;
        %Docstring
            Set string value
        %End

        char* get_string_val() /PyName=get_string_value/;
        %Docstring
            Return string value
        %End

        %Property(name=string_val, get=get_string_value, set=set_string_value)
        {
            %Docstring
                The property for string value
            %End
        };
};

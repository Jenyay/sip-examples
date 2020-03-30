%Module(name=foocpp, language="C++")
%DefaultEncoding "UTF-8"

class Foo {
    %TypeHeaderCode
    #include <foo.h>
    %End

    public:
        Foo(int, std::wstring);

        void set_int_val(int);
        int get_int_val();
        %Property(name=int_val, get=get_int_val, set=set_int_val)

        void set_string_val(std::wstring);
        std::wstring get_string_val();
        %Property(name=string_val, get=get_string_val, set=set_string_val)
};


%MappedType std::wstring
{
%TypeHeaderCode
#include <string>
%End

%ConvertFromTypeCode
    // Convert an std::wstring to a Python (Unicode) string
    PyObject* newstring;
    newstring = PyUnicode_FromWideChar(sipCpp->data(), -1);
    return newstring;
%End

%ConvertToTypeCode
    // Convert a Python (Unicode) string to an std::wstring
    if (sipIsErr == NULL) {
        return PyUnicode_Check(sipPy);
    }
    if (PyUnicode_Check(sipPy)) {
        *sipCppPtr = new std::wstring(PyUnicode_AS_UNICODE(sipPy));
        return 1;
    }
    return 0;
%End
};

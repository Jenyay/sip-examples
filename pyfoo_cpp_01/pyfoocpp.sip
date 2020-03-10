%Module(name=foocpp, language="C++")
%DefaultEncoding "UTF-8"
%Platforms {Linux macOS Windows}

class Foo {
	%TypeHeaderCode
	#include <foo.h>
	%End

	public:
		Foo(int int_val, const char* string_val);

		void set_int_val(int val);
		int get_int_val();

		void set_string_val(const char* val);
		char* get_string_val();
};

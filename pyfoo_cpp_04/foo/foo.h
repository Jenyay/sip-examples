#ifndef FOO_LIB
#define FOO_LIB

#include <string>

using std::wstring;


class Foo {
	private:
		int _int_val;
		wstring _string_val;
	public:
		Foo(int int_val, wstring string_val);

		void set_int_val(int val);
		int get_int_val();

		void set_string_val(wstring val);
		wstring get_string_val();
};

#endif

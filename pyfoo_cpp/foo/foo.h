#ifndef FOO_LIB
#define FOO_LIB

#include <string>

using std::string;


class Foo {
	private:
		int _int_val;
		string _string_val;
	public:
		Foo(int int_val, string string_val);

		void set_int_val(int val);
		int get_int_val();

		void set_string_val(string val);
		string get_string_val();
};

#endif

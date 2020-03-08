#include "foo.h"

using std::string;


Foo::Foo(int int_val, string string_val):
	_int_val(int_val), _string_val(string_val){}


void Foo::set_int_val(int val) {
	_int_val = val;
}


int Foo::get_int_val() {
	return _int_val;
}


void Foo::set_string_val(string val) {
	_string_val = val;
}


string Foo::get_string_val() {
	return _string_val;
}

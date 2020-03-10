#include <string.h>

#include "foo.h"


Foo::Foo(int int_val, const char* string_val): _int_val(int_val) {
	_string_val = nullptr;
	set_string_val(string_val);
}


Foo::~Foo(){
	delete[] _string_val;
	_string_val = nullptr;
}


void Foo::set_int_val(int val) {
	_int_val = val;
}


int Foo::get_int_val() {
	return _int_val;
}


void Foo::set_string_val(const char* val) {
	if (_string_val != nullptr) {
		delete[] _string_val;
	}

	auto count = strlen(val) + 1;
	_string_val = new char[count];
	strcpy(_string_val, val);
}


char* Foo::get_string_val() {
	return _string_val;
}

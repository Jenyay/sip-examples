#include <iostream>

#include "foo.h"

using std::cout;
using std::endl;


int main(int argc, char* argv[]) {
	auto foo = Foo(10, L"Hello");
	cout << L"int_val: " << foo.get_int_val() << endl;
	cout << L"string_val: " << foo.get_string_val().c_str() << endl;

	foo.set_int_val(0);
	foo.set_string_val(L"Hello world!");

	cout << L"int_val: " << foo.get_int_val() << endl;
	cout << L"string_val: " << foo.get_string_val().c_str() << endl;
}

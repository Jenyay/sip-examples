#include <string>
#include <iostream>

#include "foo.h"

using std::string;
using std::cout;
using std::endl;


int main(int argc, char* argv[]) {
	auto foo = Foo(10, "Hello");
	cout << "int_val: " << foo.get_int_val() << endl;
	cout << "string_val: " << foo.get_string_val() << endl;

	foo.set_int_val(0);
	foo.set_string_val("Hello world!");

	cout << "int_val: " << foo.get_int_val() << endl;
	cout << "string_val: " << foo.get_string_val() << endl;
}

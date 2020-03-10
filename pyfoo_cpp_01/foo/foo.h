#ifndef FOO_LIB
#define FOO_LIB


class Foo {
	private:
		int _int_val;
		char* _string_val;
	public:
		Foo(int int_val, const char* string_val);
		virtual ~Foo();

		void set_int_val(int val);
		int get_int_val();

		void set_string_val(const char* val);
		char* get_string_val();
};

#endif

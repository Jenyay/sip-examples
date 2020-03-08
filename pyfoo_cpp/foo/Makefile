CC=g++
CFLAGS=-c
DIR_OUT=bin

all: main

main: main.o libfoo.a
	$(CC) $(DIR_OUT)/main.o -L$(DIR_OUT) -lfoo -o $(DIR_OUT)/main

main.o: makedir main.cpp
	$(CC) $(CFLAGS) main.cpp -o $(DIR_OUT)/main.o

libfoo.a: makedir foo.cpp
	$(CC) $(CFLAGS) foo.cpp -o $(DIR_OUT)/foo.o
	ar rcs $(DIR_OUT)/libfoo.a $(DIR_OUT)/foo.o

makedir:
	mkdir -p $(DIR_OUT)

clean:
	rm -rf $(DIR_OUT)/*

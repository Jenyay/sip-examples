CC=gcc
CFLAGS=-c
DIR_OUT=bin

all: main

main: main.o libfoo.a
	$(CC) $(DIR_OUT)/main.o -L$(DIR_OUT) -lfoo -o $(DIR_OUT)/main

main.o: makedir main.c
	$(CC) $(CFLAGS) main.c -o $(DIR_OUT)/main.o

libfoo.a: makedir foo.c
	$(CC) $(CFLAGS) foo.c -o $(DIR_OUT)/foo.o
	ar rcs $(DIR_OUT)/libfoo.a $(DIR_OUT)/foo.o

makedir:
	mkdir -p $(DIR_OUT)

clean:
	rm -rf $(DIR_OUT)/*

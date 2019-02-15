CC = g++
CFLAGS = -Wall -Wextra -O2
LDLIBS = -lm

build: algo.o exec

algo.o: algo.cpp
	g++ algo.cpp -c $(CFLAGS)

main.o: main.cpp
	g++ main.cpp -c $(CFLAGS)

exec: algo.o main.o
	g++ algo.o main.o $(CFLAGS) -o exec

.PHONY: clean
clean:
	rm -rf *.o
	rm exec

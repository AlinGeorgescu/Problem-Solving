CC = g++
CFLAGS = -Wall -Wextra -O2
LDLIBS = -lm

build: InputGenerator.out ClassicPrimalityTest.out

InputGenerator.o: InputGenerator.cpp
	g++ InputGenerator.cpp -c $(CFLAGS)

InputGenerator.out: InputGenerator.o
	g++ InputGenerator.o $(CFLAGS) -o InputGenerator.out

ClassicPrimalityTest.o: ClassicPrimalityTest.cpp
	g++ ClassicPrimalityTest.cpp -c $(CFLAGS)

ClassicPrimalityTest.out: ClassicPrimalityTest.o
	g++ ClassicPrimalityTest.o $(CFLAGS) -o ClassicPrimalityTest.out

.PHONY: clean
clean:
	rm -rf InputGenerator.out ClassicPrimalityTest.out *.o

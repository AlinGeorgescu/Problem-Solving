#!/bin/bash

numTests=10
executable=exec

make

if test ! -x $executable; then
    echo "Executable file missing."
    exit 1
fi

mkdir -p ../out

echo "-------------Rulez Algoritmul-------------"
for i in $(seq 0 $numTests); do
    echo "Rulez testul: test$i"
	./$executable <../in/test$i.in >../out/test$i\_mr.out
    diff -Z ../out/test$i\_mr.out ../ref/test$i.ref > /dev/null
    if [ $? -eq 0 ]; then
		echo "Test $i ......................... perfect"
		sum=$(($sum + 1))
	else
		echo "Test $i ......................... difera"
	fi
done
echo "Rulez testul: bonus"
./$executable <../in/bonus.in >../out/bonus_mr.out
diff -Z ../out/bonus\_mr.out ../ref/bonus.ref > /dev/null
if [ $? -eq 0 ]; then
	echo "Test Bonus ...................... perfect"
	sum=$(($sum + 1))
else
	echo "Test Bonus ...................... difera"
fi

echo "------------Algoritm finalizat------------"
echo ""
echo "TOTAL: $sum/12 teste perfecte"
echo ""

make clean

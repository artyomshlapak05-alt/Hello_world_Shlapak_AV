#!/bin/bash
for i in {1..10}; do
    touch "test${i}.txt"
    echo "Создан: test${i}.txt"
done
sleep 1
i=10
while [ $i -ge 1 ]; do
    rm "test${i}.txt"
    echo "Удалён: test${i}.txt"
    i=$((i-1))
done

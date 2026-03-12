#!/bin/bash
read -p "Введите ваш вес(кг):    " weight
read -p "Введите ваш рост(м):    " height
bmi=$(echo "scale=0; $weight / ($height * $height)" | bc -l)
echo "ИНДЕКС МАССЫ ТЕЛА: $bmi"

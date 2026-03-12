#!/bin/bash
awk '$2 > 80' students.txt
awk '$2 < 70' students.txt
awk 'NR==1' students.txt

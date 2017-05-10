#!/bin/bash
echo "TEST Sample 1"
echo ""
valgrind --leak-check=yes ./sample_1
echo "TEST Sample 2"
echo ""
valgrind --leak-check=yes ./sample_2

#

import sys
import io

INPUT = """6
10 20 10 30 20 50"""
sys.stdin = io.StringIO(INPUT)

read = sys.stdin.readlines()

print(read)
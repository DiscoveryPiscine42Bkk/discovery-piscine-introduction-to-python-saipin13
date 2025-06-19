
import sys


if len(sys.argv) != 2:
    print("none")
    sys.exit()

input_str = sys.argv[1]


count_z = input_str.count('z')

if count_z == 0:
    print("none")
else:
  
    print("z" * count_z)
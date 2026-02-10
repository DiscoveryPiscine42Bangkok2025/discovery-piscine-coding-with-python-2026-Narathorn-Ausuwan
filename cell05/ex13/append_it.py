import sys

if len(sys.argv) == 1:
    print("none")
else:
    for param in sys.argv[1:]:
        print(param.rstrip("ism") + "ism")

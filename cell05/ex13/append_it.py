import sys

def modify_strings(args):
    if not args:
        print("none")
    else:
        for arg in args:
            if not arg.endswith("ism"):
                print(arg + "ism")

if __name__ == "__main__":
    modify_strings(sys.argv[1:])
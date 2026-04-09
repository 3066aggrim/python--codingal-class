class employee:

    def __init__(self):
        print("employe created")

    def __del__(self):
        print("employe terminated")


def create_object():
    print("making employee")
    obj = employee()
    print("function end")
    return obj


print("calling create function ........")
odj = create_object()
print("END!")

# Object Will Call the init method of a Super Class When the Particular Class Doesn't have It's own init Method
# We Can Access Methods of Super Class Using super().method_name() functionality in Sub Class.
# Constructor Follows Method Resolution Order (MRO) --> Left to Right


class A:
    def __init__(self):
        print("In A init")

    def feature1(self):
        print("Feature 1 is in Class A Working")

    def feature2(self):
        print("Feature 2 is in Class A Working")


class B:
    def __init__(self):
        print("In B init")

    def feature3(self):
        print("Feature 3 in Class B is Working")

    def feature4(self):
        print("Feature 4 in Class B is Working")


class C(A, B):
    def __init__(self):
        super().__init__()
        print("In C init")


a1 = C()

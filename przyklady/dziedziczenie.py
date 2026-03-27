#


class A:
    atr1 = 123

    def m1(self):
        """
        Metoda A.m1 jest super !!!
        Returns:

        """
        print('jestem A.m1')


class B(A):
    atr2 = 456

    def m1(self):
        """
        Metoda B.m1 jest super !!!
        Returns:

        """
        super().m1()
        print('jestem B.m1')

    def m2(self):
        print('jestem B.m2')


b = B()
b.m1()
b.m2()
print(b.atr1)
print(b.atr2)

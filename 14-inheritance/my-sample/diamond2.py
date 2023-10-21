# tag::DIAMOND_CLASSES[]
from diamond import A  # <1>

class U():  # <2>
    def ping(self):
        print(f'{self}.ping() in U')
        super().ping()  # <3>

class LeafUA(U, A):  # <4>
    def ping(self):
        print(f'{self}.ping() in LeafUA')
        super().ping()
# end::DIAMOND_CLASSES[]

class LeafAU(A, U):
    def ping(self):
        print(f'{self}.ping() in LeafAU')
        super().ping()
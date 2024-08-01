class Mart:
    def __init__(self, name, code):
        self.name = name
        self.code = code

mart1 = Mart("codetree", '50')
a, b = map(str, input().split())
mart2 = Mart(a, b)
print("product " + mart1.code + " is " + mart1.name)
print("product " + mart2.code + " is " + mart2.name)
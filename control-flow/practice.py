
x = 3

def test(z):
    global x 
    x = 'local x'
    print(x)
    def testy(y):
        x = "inner y"
        print(x)
    testy("7")
test("3")
print(x)

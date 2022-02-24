def check_value(func):
    def verify_value(a, t):
        if a < 5:
            print("[Alas dibawah 5, maka alas menjadi 5]")
            a = 5
        if t < 5:
            print("[Tinggi dibawah 5, maka tinggi menjadi 5]")
            t = 5
        return func(a, t)
    return verify_value

@check_value
def luas_segitiga(a, t):
    luas = 0.5 * a * t
    print("Luas segitiga:", luas)

alas = int(input("Alas segitiga: "))
tinggi = int(input("Tinggi segitiga: "))
luas_segitiga(alas, tinggi)
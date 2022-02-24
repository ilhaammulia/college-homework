def check_student(func):
    def verify_student(nim, name):
        if nim == 1:
            print("[Siswa Kelas 1]")
        elif nim == 2:
            print("[Siswa Kelas 2]")
        else:
            print("[Bukan Siswa]")
        return func(nim, name)
    return verify_student

@check_student
def student(nim, name):
    print("Nim: {} Name: {}".format(nim, name))

nim = int(input("Nim: "))
name = input("Name: ")
student(nim, name)
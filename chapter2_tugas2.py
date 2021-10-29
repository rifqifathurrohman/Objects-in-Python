
def odd(n):
    x = n % 2
    if x != 0:
        y = True
    else:
        y = False
    return y


def ikan(jenis):
    print(f'Salah satu jenis ikan adalah {jenis}')


class mangga():
    def __init__(self):
        print("aku suka arum manis, mangga madu")
show = mangga()



class Kelulusan():
 
    def __init__(self, masukan_nama):
        self.nama = masukan_nama
 
    def nilai(self, nilai):
        if nilai >= 70:
            print(self.nama,'Selamat anda lulus dengan nilai',nilai)
        else:
            print(self.nama,'Maaf anda tidak lulus dengan nilai',nilai)
            
mhs=Kelulusan("RIFQI FTR")
print(mhs.nama)
mhs.nilai(70)
print(ikan (jenis="tuna"))

print(odd(1))
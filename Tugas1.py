class student :
    """ A class representing a student """
    def __init__(self,n,a,i,p,c):
        self.full_name=n
        self.age=a
        self.nim=i
        self.prodi=p
        self.city=c
    def get_age(self):
        return self.age
    def get_nim(self):
        return self.nim
    def get_prodi(self):
        return self.prodi
    def get_city(self):
        return self.city
f = student("Adisty laili",21,1904347,"Sistem Telekomunikasi","Bogor")
print(f.full_name)
print(f.get_age())
print(f.get_nim())
print(f.get_prodi())
print(f.get_city())
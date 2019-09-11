class lingkaran(object):
   def __init__(self, p, r):
      self.phi = p
      self.jarijari = r
   def hitungkeliling(self):
      return 2* self.phi * self.jarijari 

def main():
   lingkaran1 = lingkaran(3.14, 25)

   print('Objek lingkaran1')
   print('phi        :', lingkaran1.phi)
   print('jari-jari  :', lingkaran1.jarijari)
   print('Keliling lingkaran =', lingkaran1.hitungkeliling())

   lingkaran2 = lingkaran(3.14, 5)

   print("\nObjek lingkaran2")
   print('phi        :', lingkaran2.phi)
   print('jari-jari  :', lingkaran2.jarijari)
   print("Keliling lingkaran =", lingkaran2.hitungkeliling())

if __name__ == "__main__":
   main()

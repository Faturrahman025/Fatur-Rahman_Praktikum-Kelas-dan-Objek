class lingkaran(object):
   def __init__(self, p, r):
      self.phi = p
      self.jarijari = r
   def hitungluas(self):
      return self.phi * self.jarijari * self.jarijari

def main():
   lingkaran1 = lingkaran(3.14, 25)

   print('Objek lingkaran 1')
   print('phi       : ', lingkaran1.phi)
   print('jari-jari : ', lingkaran1.jarijari)
   print('Luas lingkaran  = ', lingkaran1.hitungluas())

   lingkaran2 = lingkaran(3.14, 5)

   print("\nObjek lingkaran 2")
   print('phi       : ', lingkaran2.phi)
   print('jari-jari : ', lingkaran2.jarijari)
   print("Luas lingkaran  = ", lingkaran2.hitungluas())

if __name__ == "__main__":
   main()

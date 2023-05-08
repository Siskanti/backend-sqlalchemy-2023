from database import sessionLoc 
from model import Product
from model import Kategori
from model import KategoriProduct

# From class Product
sesi =sessionLoc()
# data1 = Product(nama="baju", deskripsi="baju lengan serut", stok="100", fileimage="baju.jpg")
# sesi.add(data1)
# data2 = Product(nama="celana", deskripsi="celana bahan levis", stok="10", fileimage="celana.jpg")
# sesi.add(data2)
# data3 = Product(nama="sepatu", deskripsi="sepatu ballet", stok="15", fileimage="sepatu.jpg")
# sesi.add(data3)
# data4 = Product(nama="tas", deskripsi="tas selempang", stok="50", fileimage="tas.jpg")
# sesi.add(data4)
# data5 = Product(nama="pasmina", deskripsi="pasminarajut", stok="45", fileimage="pasmina.jpg")
# sesi.add(data5)

# From class Kategori
# data_k1 = Kategori(nama="pakaian")
# sesi.add(data_k1)
# data_k2 = Kategori(nama="pakaian")
# sesi.add(data_k2)
# data_k3 = Kategori(nama="barang")
# sesi.add(data_k3)
# data_k4 = Kategori(nama="barang")
# sesi.add(data_k4)
# data_k5 = Kategori(nama="pakaian")
# sesi.add(data_k5)

data_kp1 = KategoriProduct("1", "1")
sesi.add(data_kp1)
data_kp2 = KategoriProduct("2", "2")
sesi.add(data_kp2)
data_kp3 = KategoriProduct("3", "3")
sesi.add(data_kp3)
data_kp4 = KategoriProduct("4", "4")
sesi.add(data_kp4)
data_kp5 = KategoriProduct("5", "5")
sesi.add(data_kp5)

sesi.commit()
sesi.close()
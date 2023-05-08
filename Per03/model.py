from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, func
from sqlalchemy.orm import relationship
from database import Base, engine
from datetime import datetime

class Product(Base):
    __tablename__ = "product"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nama = Column(String(100), nullable=False)
    deskripsi = Column(String(256), nullable=False)
    stok = Column(Integer, nullable=False)
    fileimage = Column(String(256), nullable=False)


class Kategori(Base):
    __tablename__ = "kategori"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nama = Column(String(50), nullable=False)
    
class KategoriProduct(Base):
    __tablename__ = "kategoriproduct"
    id = Column(Integer, primary_key=True, autoincrement=True)
    idproduct = Column(Integer, ForeignKey("product.id", ondelete="cascade"), nullable=False)
    idkategori = Column(Integer, ForeignKey("kategori.id", ondelete="cascade"), nullable=False)
    
    def __init__(self, idproduct, idkategori):
         self.idproduct = idproduct
         self.idkategori = idkategori
   

if __name__ == "__main__":
    Base.metadata.create_all(engine)
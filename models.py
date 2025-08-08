from sqlalchemy import (Column, Integer, String, Text, ForeignKey, Float, 
                        DateTime, Enum as SQLAlchemyEnum)
from sqlalchemy.orm import relationship
from database import Base
import enum

class Role(str, enum.Enum):
    USER = "USER"; ADMIN = "ADMIN"; MUSEUM = "MUSEUM"; CREATOR = "CREATOR"; EDITOR = "EDITOR"; AUTHOR = "AUTHOR"; EXHIBITION = "EXHIBITION"
class PostStatus(str, enum.Enum):
    PENDING = "PENDING"; APPROVED = "APPROVED"; REJECTED = "REJECTED"
class ProductStatus(str, enum.Enum):
    PENDING = "PENDING"; APPROVED = "APPROVED"; REJECTED = "REJECTED"

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True)
    password = Column(String)
    role = Column(SQLAlchemyEnum(Role))
    title = Column(String, nullable=True)
    bio = Column(String, nullable=True)
    images = Column(Text, nullable=True)
    resetToken = Column(String, unique=True, nullable=True)
    resetTokenExpiry = Column(DateTime, nullable=True)
    createdAt = Column("created_at", DateTime)
    updatedAt = Column("updated_at", DateTime)
    country = Column(String, nullable=True)
    houseNumber = Column("house_number", String, nullable=True)
    lat = Column(Float, nullable=True)
    lon = Column(Float, nullable=True)
    postcode = Column(String, nullable=True)
    state = Column(String, nullable=True)
    street = Column(String, nullable=True)
    city = Column(String, nullable=True)

class Product(Base):
    __tablename__ = "Product"
    id = Column(Integer, primary_key=True)
    authorId = Column(Integer, ForeignKey("users.id"))
    # ... інші поля ...
    images = relationship("ProductImage", back_populates="product")

class ArtTerm(Base):
    __tablename__ = "ArtTerm"
    id = Column(Integer, primary_key=True)
    title_en = Column(String)
    description_en = Column(String)
    authorId = Column("author_id", Integer, ForeignKey("users.id"))
    highlightedProductId = Column("highlighted_product_id", Integer, ForeignKey("Product.id"))
    product = relationship("Product")

class ProductImage(Base):
    __tablename__ = "ProductImage"
    id = Column(Integer, primary_key=True)
    imageUrl = Column(String)
    productId = Column(Integer, ForeignKey("Product.id"))
    product = relationship("Product", back_populates="images")

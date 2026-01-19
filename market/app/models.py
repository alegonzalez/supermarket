from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from .database import Base


# ---------- CUSTOMERS ----------
class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String, unique=True)
    phone = Column(String)
    address = Column(String)

    sales = relationship("Sale", back_populates="customer")


# ---------- SUPPLIERS ----------
class Supplier(Base):
    __tablename__ = "suppliers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    contact_name = Column(String)
    phone = Column(String)
    email = Column(String)
    address = Column(String)

    products = relationship("Product", back_populates="supplier")


# ---------- CATEGORIES ----------
class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)

    products = relationship("Product", back_populates="category")


# ---------- PRODUCTS ----------
class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    price = Column(Float)
    stock = Column(Integer)

    category_id = Column(Integer, ForeignKey("categories.id"))
    supplier_id = Column(Integer, ForeignKey("suppliers.id"))

    category = relationship("Category", back_populates="products")
    supplier = relationship("Supplier", back_populates="products")


# ---------- SALES ----------
class Sale(Base):
    __tablename__ = "sales"

    id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer, ForeignKey("customers.id"))
    date = Column(DateTime, default=datetime.utcnow)
    total = Column(Float)

    customer = relationship("Customer", back_populates="sales")
    details = relationship("SaleDetail", back_populates="sale")
    payments = relationship("Payment", back_populates="sale")


# ---------- SALE DETAILS ----------
class SaleDetail(Base):
    __tablename__ = "sale_details"

    id = Column(Integer, primary_key=True, index=True)
    sale_id = Column(Integer, ForeignKey("sales.id"))
    product_id = Column(Integer, ForeignKey("products.id"))

    quantity = Column(Integer)
    unit_price = Column(Float)

    sale = relationship("Sale", back_populates="details")
    product = relationship("Product")


# ---------- PAYMENTS ----------
class Payment(Base):
    __tablename__ = "payments"

    id = Column(Integer, primary_key=True, index=True)
    sale_id = Column(Integer, ForeignKey("sales.id"))

    amount = Column(Float)
    payment_method = Column(String)
    payment_date = Column(DateTime, default=datetime.utcnow)

    sale = relationship("Sale", back_populates="payments")


# ---------- INVENTORY ----------
class Inventory(Base):
    __tablename__ = "inventory"

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("products.id"))

    date = Column(DateTime, default=datetime.utcnow)
    quantity_in = Column(Integer)
    quantity_out = Column(Integer)
    current_balance = Column(Integer)


# ---------- USERS ----------
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True)
    password = Column(String)
    full_name = Column(String)
    email = Column(String)
    phone = Column(String)
    role = Column(String)

    created_at = Column(DateTime, default=datetime.utcnow)
    last_login = Column(DateTime)
    is_active = Column(Boolean, default=True)

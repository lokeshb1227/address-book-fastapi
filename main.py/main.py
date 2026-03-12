from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel, Field
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import sessionmaker, declarative_base, Session
import math

app = FastAPI(title="Address Book API")

# Database configuration
DATABASE_URL = "sqlite:///./address_book.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


# Database Model
class Address(Base):
    __tablename__ = "addresses"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)


Base.metadata.create_all(bind=engine)


# Request Schema
class AddressRequest(BaseModel):
    name: str = Field(..., example="Home")
    latitude: float = Field(..., example=12.9716)
    longitude: float = Field(..., example=77.5946)


# Dependency for DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Utility function for distance calculation
def calculate_distance(lat1, lon1, lat2, lon2):
    return math.sqrt((lat1 - lat2) ** 2 + (lon1 - lon2) ** 2)


# Create Address
@app.post("/addresses")
def create_address(address: AddressRequest, db: Session = Depends(get_db)):
    new_address = Address(**address.dict())
    db.add(new_address)
    db.commit()
    db.refresh(new_address)
    return new_address


# Get All Addresses
@app.get("/addresses")
def get_addresses(db: Session = Depends(get_db)):
    return db.query(Address).all()


# Update Address
@app.put("/addresses/{address_id}")
def update_address(address_id: int, address: AddressRequest, db: Session = Depends(get_db)):
    existing_address = db.query(Address).filter(Address.id == address_id).first()

    if not existing_address:
        raise HTTPException(status_code=404, detail="Address not found")

    existing_address.name = address.name
    existing_address.latitude = address.latitude
    existing_address.longitude = address.longitude

    db.commit()
    db.refresh(existing_address)

    return existing_address


# Delete Address
@app.delete("/addresses/{address_id}")
def delete_address(address_id: int, db: Session = Depends(get_db)):
    address = db.query(Address).filter(Address.id == address_id).first()

    if not address:
        raise HTTPException(status_code=404, detail="Address not found")

    db.delete(address)
    db.commit()

    return {"message": "Address deleted successfully"}


# Find Nearby Addresses
@app.get("/addresses/nearby")
def get_nearby_addresses(lat: float, lon: float, distance: float, db: Session = Depends(get_db)):
    addresses = db.query(Address).all()
    nearby = []

    for addr in addresses:
        dist = calculate_distance(lat, lon, addr.latitude, addr.longitude)
        if dist <= distance:
            nearby.append(addr)

    return nearby
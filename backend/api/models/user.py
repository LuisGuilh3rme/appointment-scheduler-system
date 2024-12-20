from datetime import datetime
import uuid
from sqlalchemy import Column, UUID, SmallInteger, String, DateTime
from database.database import Base

class User(Base):
    __tablename__ = 'user'

    id = Column(UUID, default=uuid.uuid4, primary_key=True, index=True)
    email = Column(String(100), nullable=False, unique=True)
    username = Column(String(100), nullable=False, unique=True)
    password = Column(String(30), nullable=False)
    created_at = Column(DateTime, default=datetime.now(), nullable=False)
    updated_at = Column(DateTime, default=datetime.now(), nullable=False)
    status = Column(SmallInteger, default=0, nullable=False)
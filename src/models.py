from sqlalchemy import Integer, String, Column
from database import Base


class Employee(Base):
    __tablename__ = "Employee"

    emp_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
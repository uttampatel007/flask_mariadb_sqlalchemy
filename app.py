"""
Referance : https://docs.sqlalchemy.org/en/14/orm/tutorial.html

"""
import sqlalchemy
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base

engine = sqlalchemy.create_engine("mariadb+mariadbconnector://root:smart@127.0.0.1:3306/flask_mariadb_sqlalchemy")
# Engines are used to manage two crucial factors: Pools and Dialects. 

Base = declarative_base()

class Employee(Base):
    __tablename__ = 'employeesK'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    first_name = sqlalchemy.Column(sqlalchemy.String(length=100))
    last_name = sqlalchemy.Column(sqlalchemy.String(length=100))
    active = sqlalchemy.Column(sqlalchemy.Boolean, default=True)
    created_at = sqlalchemy.Column(sqlalchemy.DateTime, server_default=func.now())

class EmployeeTable(Base):
    __tablename__ = 'employee_table'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    first_name = sqlalchemy.Column(sqlalchemy.String(length=100))
    address = sqlalchemy.Column(sqlalchemy.String(length=100))
    active = sqlalchemy.Column(sqlalchemy.Boolean, default=True)

class EmployeeData(Base):
    __tablename__ = 'employee_data'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    first_name = sqlalchemy.Column(sqlalchemy.String(length=100))
    data = sqlalchemy.Column(sqlalchemy.String(length=100))
    active = sqlalchemy.Column(sqlalchemy.Boolean, default=True)



Base.metadata.create_all(engine)
Session = sqlalchemy.orm.sessionmaker()
Session.configure(bind=engine)
session = Session()



'''
# adding one employee
'''

newEmployee = Employee(first_name="sdsRob", last_name="Hsddb", active=False)
session.add(newEmployee)
session.commit()


'''
# adding multiple 
newEmployees = session.add_all([
    Employee(first_name="sdsRob", last_name="Hsddb", active=False),
    Employee(first_name="sdsRob", last_name="Hsddb", active=False)
])
'''

all_employess = session.query(Employee).all()
print(all_employess)
"""
Referance : https://docs.sqlalchemy.org/en/14/orm/tutorial.html

"""
import sqlalchemy
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Table, MetaData, Text


# Engines are used to manage two crucial factors: Pools and Dialects. 
engine = sqlalchemy.create_engine("mariadb+mariadbconnector://root:smart@127.0.0.1:3306/flask_mariadb_sqlalchemy")


Base = declarative_base()


class Employee(Base):
    __tablename__ = 'employeesK'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    first_name = sqlalchemy.Column(sqlalchemy.String(length=100))
    last_name = sqlalchemy.Column(sqlalchemy.String(length=100))
    active = sqlalchemy.Column(sqlalchemy.Boolean, default=True)
    created_at = sqlalchemy.Column(sqlalchemy.DateTime, server_default=func.now())


class EmployeeAddress(Base):
    __tablename__ = 'employee_address_2'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    employee_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('employeesK.id'))
    address = sqlalchemy.Column(sqlalchemy.String(length=100))


class EmployeeInteger(Base):
    __tablename__ = 'employee_integer'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    des = sqlalchemy.Column(sqlalchemy.Integer)


class EmployeeText(Base):
    __tablename__ = 'employee_text'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    des = sqlalchemy.Column(Text)


Base.metadata.create_all(engine)
Session = sqlalchemy.orm.sessionmaker()
Session.configure(bind=engine)
session = Session()



'''
# adding one employee
newEmployee = Employee(first_name="sdsRob", last_name="Hsddb", active=False)
session.add(newEmployee)
session.commit()

NewEmployeeAddress = EmployeeAddress(employee_id=newEmployee.id, address='dekkdjkjdejk')
session.add(NewEmployeeAddress)
session.commit()

'''

'''
# adding multiple 
newEmployees = session.add_all([
    Employee(first_name="sdsRob", last_name="Hsddb", active=False),
    Employee(first_name="sdsRob", last_name="Hsddb", active=False)
])
'''

all_employess = session.query(Employee).all()
print(all_employess)
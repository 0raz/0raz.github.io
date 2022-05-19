from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
class Parent(Base):
    __tablename__ = 'parents'
    id = Column(Integer, primary_key=True)
    children = relationship("Child", backref="parent")
    def __repr__(self):
        return f'parent with id {self.id}'

class Child(Base):
    __tablename__ = 'children'
    id = Column(Integer, primary_key=True)
    parent_id = Column(Integer, ForeignKey('parents.id'))
    def __repr__(self):
        return f'child with id {self.id}'

from sqlalchemy import create_engine
engine = create_engine("sqlite+pysqlite:///:memory:", echo=True)
print('1Begin---------------------------')
Base.metadata.create_all(engine)
print('1End-----------------------------')

from sqlalchemy.orm import Session

with Session(bind=engine) as session:
    
    parent1 = Parent()
    print('2Begin---------------------------')
    session.add(parent1)
    session.commit()
    print('2End------------------------------')
    
    child1 = Child()
    print('3Begin------------------------------')
    parent1.children.append(child1)
    session.commit()
    print('3End------------------------------')
    print('4Begin------------------------')
    print(parent1.children)
    print(child1.parent)
    print('4End----------------------------------')
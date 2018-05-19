from peewee import *

db=SqliteDatabase('students.db')
"""hola solo verguenzas"""
class Student(Model):
    username=CharField(max_length=255,unique=True)
    points=IntegerField(default=0)

    class Meta:
        database=db
students=[
    {'username':'Aldo',
     'points':7},
    {'username':'Rogger',
     'points':1},
    {'username':'Pablo',
     'points':9},
    {'username':'Diego',
     'points':8},
    {'username':'Richard',
     'points':10},
]
#metodo que agrega estudiantes
def add_students():
    for information in students:
        try:
            Student.create(username=information['username'],
                           points=information['points'])
        except IntegrityError:# error registro existe
            student_exist= Student.get(username=information['username'])
            student_exist.points=information['points']
            student_exist.save()


if __name__ == '__main__':
    db.connect() #permite conectar a la base de datos
    db.create_tables([Student],safe=True)
    add_students()

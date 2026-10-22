class Student(object):
    __slots__ = ('name', 'age') # 用tuple定义允许绑定的属性名称


class StudentZ(Student):
     __slots__ = ('score') # 用tuple定义允许绑定的属性名称

student = StudentZ() # 创建新的实例
student.score = 'Michael' # 绑定属性'name'
student.age = 25 # 绑定属性'age'





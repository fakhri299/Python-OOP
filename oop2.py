class Student:
    def __init__(self,name,surname,group_number,gpa,course):
        self._name=name
        self._surname=surname
        self._group=group_number
        self._gpa=gpa
        self._course=course

    @property
    def info(self):
        return f'{self._name}, {self._surname}, {self._group}, {self._gpa} ,{self._course} '

        

student1=Student('Fakhri','Mammadov','691.20',88,3)
student2=Student('Ravan','Mammadov','293.20',85,1)
student3=Student('Vilayat','Safarov','695.20',79,3)

print(student3.info)



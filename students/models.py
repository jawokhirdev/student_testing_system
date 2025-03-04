from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name

class Test(models.Model):
    name = models.CharField(max_length=100)
    max_score = models.IntegerField()

    def __str__(self):
        return self.name

class TestResult(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    score = models.IntegerField()

    def __str__(self):
        return f"{self.student.name} - {self.test.name}: {self.score}"
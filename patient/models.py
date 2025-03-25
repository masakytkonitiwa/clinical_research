from django.db import models

class Patient(models.Model):
    id = models.AutoField(primary_key=True)
    patient_id = models.IntegerField()  # `name` から `patient_id` に変更（数値型）

    age = models.IntegerField()
    gender = models.CharField(max_length=10, choices=[("male", "男性"), ("female", "女性")])
    diagnosis = models.TextField()
    #項目ふやすときは以下
    koumoku1 = models.TextField()
    
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.id} - {self.patient_id}"
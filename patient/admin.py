from django.contrib import admin
from .models import Patient

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('id', 'patient_id', 'age', 'gender', 'created_at')  # ここに `created_at` を追加
    list_filter = ('created_at',)  # フィルタを追加（任意）
    search_fields = ('patient_id', 'diagnosis')  # 検索機能（任意）
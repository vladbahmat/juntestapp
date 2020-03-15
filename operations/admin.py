from django.contrib import admin

# Register your models here.
from .models import Sort,Operation
 
class SortModelAdmin(admin.ModelAdmin):
    list_display = ["name", "updated", "timestamp","sort_type"]
    list_display_links = ["name", "updated"]
    list_filter = ["updated", "timestamp","sort_type"]
    search_fields = ["name", "content","sort_type"]
    class Meta:
        model = Sort
 
admin.site.register(Sort, SortModelAdmin)

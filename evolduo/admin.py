from django.contrib import admin

# Register your models here.

from .models import Evolution, Iteration, Chromosome, Invitation, Rating

admin.site.register(Evolution, admin.ModelAdmin)
admin.site.register(Iteration, admin.ModelAdmin)
admin.site.register(Chromosome, admin.ModelAdmin)
admin.site.register(Invitation, admin.ModelAdmin)
admin.site.register(Rating, admin.ModelAdmin)

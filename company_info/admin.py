from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Gallery, SourceReview, Review, Partner, Address, Phone, Contact, Worker

class WorkerAdmin(SummernoteModelAdmin):
    summernote_fields = (
        'about',
        )

class ReviewAdmin(SummernoteModelAdmin):
    summernote_fields = (
        'content',
        )

admin.site.register(Gallery)
admin.site.register(SourceReview)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Partner)
admin.site.register(Address)
admin.site.register(Phone)
admin.site.register(Contact)
admin.site.register(Worker, WorkerAdmin)
from django.contrib import admin

from text.models import Subject, Obj, Verb, Gerund, Image, Meme


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('text', )


@admin.register(Verb)
class VerbAdmin(admin.ModelAdmin):
    list_display = ('text',)


@admin.register(Obj)
class ObjAdmin(admin.ModelAdmin):
    list_display = ('text',)


@admin.register(Gerund)
class GerundAdmin(admin.ModelAdmin):
    list_display = ('text',)


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('url',)


@admin.register(Meme)
class MemeAdmin(admin.ModelAdmin):
    pass

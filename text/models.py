from django.db import models


class Subject(models.Model):
    text = models.CharField(max_length=200)
    weight = models.DecimalField(max_digits=8, decimal_places=8, default=.5)
    ratings = models.IntegerField(default=1)
    is_plural = models.BooleanField(default=False)


class Verb(models.Model):
    text = models.CharField(max_length=200)
    plural = models.CharField(max_length=200)
    weight = models.DecimalField(max_digits=8, decimal_places=8, default=.5)
    ratings = models.IntegerField(default=1)
    is_regular = models.BooleanField(default=True)

    def conjugate(self, subject):
        if self.is_regular:
            if subject.is_plural:
                return self.text
            else:
                return self.plural
        else:
            if self.text == 'be':
                if subject.text == 'I':
                    return 'am'
                if subject.text.is_plural:
                    return 'are'
                else:
                    return 'is'


class Object(models.Model):
    text = models.CharField(max_length=200)
    weight = models.DecimalField(max_digits=8, decimal_places=8, default=.5)
    ratings = models.IntegerField(default=1)


class Gerund(models.Model):
    text = models.CharField(max_length=200)
    weight = models.DecimalField(max_digits=8, decimal_places=8, default=.5)
    ratings = models.IntegerField(default=1)


class Image(models.Model):
    url = models.URLField(max_length=200)
    weight = models.DecimalField(max_digits=8, decimal_places=8, default=.5)
    ratings = models.IntegerField(default=1)


class SubjectVerb(models.Model):
    weight = models.DecimalField(max_digits=8, decimal_places=8, default=.5)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    verb = models.ForeignKey(Verb, on_delete=models.CASCADE)
    ratings = models.IntegerField(default=1)


class SubjectObject(models.Model):
    weight = models.DecimalField(max_digits=8, decimal_places=8, default=.5)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    object = models.ForeignKey(Object, on_delete=models.CASCADE)
    ratings = models.IntegerField(default=1)


class SubjectGerund(models.Model):
    weight = models.DecimalField(max_digits=8, decimal_places=8, default=.5)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    gerund = models.ForeignKey(Gerund, on_delete=models.CASCADE)
    ratings = models.IntegerField(default=1)


class SubjectImage(models.Model):
    weight = models.DecimalField(max_digits=8, decimal_places=8, default=.5)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    ratings = models.IntegerField(default=1)


class VerbObject(models.Model):
    weight = models.DecimalField(max_digits=8, decimal_places=8, default=.5)
    verb = models.ForeignKey(Verb, on_delete=models.CASCADE)
    object = models.ForeignKey(Object, on_delete=models.CASCADE)
    ratings = models.IntegerField(default=1)


class VerbGerund(models.Model):
    weight = models.DecimalField(max_digits=8, decimal_places=8, default=.5)
    verb = models.ForeignKey(Verb, on_delete=models.CASCADE)
    gerund = models.ForeignKey(Gerund, on_delete=models.CASCADE)
    ratings = models.IntegerField(default=1)


class VerbImage(models.Model):
    weight = models.DecimalField(max_digits=8, decimal_places=8, default=.5)
    verb = models.ForeignKey(Verb, on_delete=models.CASCADE)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    ratings = models.IntegerField(default=1)


class ObjectGerund(models.Model):
    weight = models.DecimalField(max_digits=8, decimal_places=8, default=.5)
    object = models.ForeignKey(Object, on_delete=models.CASCADE)
    gerund = models.ForeignKey(Gerund, on_delete=models.CASCADE)
    ratings = models.IntegerField(default=1)


class ObjectImage(models.Model):
    weight = models.DecimalField(max_digits=8, decimal_places=8, default=.5)
    object = models.ForeignKey(Object, on_delete=models.CASCADE)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    ratings = models.IntegerField(default=1)


class GerundImage(models.Model):
    weight = models.DecimalField(max_digits=8, decimal_places=8, default=.5)
    gerund = models.ForeignKey(Gerund, on_delete=models.CASCADE)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    ratings = models.IntegerField(default=1)

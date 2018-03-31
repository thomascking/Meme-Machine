from django.db import models


class Subject(models.Model):
    text = models.CharField(max_length=200)
    weight = models.DecimalField(max_digits=8, decimal_places=8, default=.5)
    ratings = models.IntegerField(default=1)

    def calculate_weighting(self, subject, verb, obj, gerund, image):
        self.calc_weight = float(self.weight)
        if verb:
            self.calc_weight *= float(SubjectVerb.objects.get_or_create(subject=self, verb=verb)[0].weight)
        if obj:
            self.calc_weight *= float(SubjectObject.objects.get_or_create(subject=self, object=obj)[0].weight)
        if gerund:
            self.calc_weight *= float(SubjectGerund.objects.get_or_create(subject=self, gerund=gerund)[0].weight)
        if image:
            self.calc_weight *= float(SubjectImage.objects.get_or_create(subject=self, image=image)[0].weight)


class Verb(models.Model):
    text = models.CharField(max_length=200)
    weight = models.DecimalField(max_digits=8, decimal_places=8, default=.5)
    ratings = models.IntegerField(default=1)

    def calculate_weighting(self, subject, verb, obj, gerund, image):
        self.calc_weight = float(self.weight)
        if subject:
            self.calc_weight *= float(SubjectVerb.objects.get_or_create(verb=self, subject=subject)[0].weight)
        if obj:
            self.calc_weight *= float(VerbObject.objects.get_or_create(verb=self, object=obj)[0].weight)
        if gerund:
            self.calc_weight *= float(VerbGerund.objects.get_or_create(verb=self, gerund=gerund)[0].weight)
        if image:
            self.calc_weight *= float(VerbImage.objects.get_or_create(verb=self, image=image)[0].weight)


class Obj(models.Model):
    text = models.CharField(max_length=200)
    weight = models.DecimalField(max_digits=8, decimal_places=8, default=.5)
    ratings = models.IntegerField(default=1)

    def calculate_weighting(self, subject, verb, obj, gerund, image):
        self.calc_weight = float(self.weight)
        if verb:
            self.calc_weight *= float(VerbObject.objects.get_or_create(object=self, verb=verb)[0].weight)
        if subject:
            self.calc_weight *= float(SubjectObject.objects.get_or_create(object=self, subject=subject)[0].weight)
        if gerund:
            self.calc_weight *= float(ObjectGerund.objects.get_or_create(object=self, gerund=gerund)[0].weight)
        if image:
            self.calc_weight *= float(ObjectImage.objects.get_or_create(object=self, image=image)[0].weight)


class Gerund(models.Model):
    text = models.CharField(max_length=200)
    weight = models.DecimalField(max_digits=8, decimal_places=8, default=.5)
    ratings = models.IntegerField(default=1)

    def calculate_weighting(self, subject, verb, obj, gerund, image):
        self.calc_weight = float(self.weight)
        if verb:
            self.calc_weight *= float(VerbGerund.objects.get_or_create(gerund=self, verb=verb)[0].weight)
        if subject:
            self.calc_weight *= float(SubjectGerund.objects.get_or_create(gerund=self, subject=subject)[0].weight)
        if obj:
            self.calc_weight *= float(ObjectGerund.objects.get_or_create(gerund=self, object=obj)[0].weight)
        if image:
            self.calc_weight *= float(GerundImage.objects.get_or_create(gerund=self, image=image)[0].weight)


class Image(models.Model):
    url = models.URLField(max_length=200)
    weight = models.DecimalField(max_digits=8, decimal_places=8, default=.5)
    ratings = models.IntegerField(default=1)

    def calculate_weighting(self, subject, verb, obj, gerund, image):
        self.calc_weight = float(self.weight)
        if verb:
            self.calc_weight *= float(VerbImage.objects.get_or_create(image=self, verb=verb)[0].weight)
        if subject:
            self.calc_weight *= float(SubjectImage.objects.get_or_create(image=self, subject=subject)[0].weight)
        if obj:
            self.calc_weight *= float(ObjectImage.objects.get_or_create(image=self, object=obj)[0].weight)
        if gerund:
            self.calc_weight *= float(GerundImage.objects.get_or_create(image=self, gerund=gerund)[0].weight)


class SubjectVerb(models.Model):
    weight = models.DecimalField(max_digits=8, decimal_places=8, default=.5)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    verb = models.ForeignKey(Verb, on_delete=models.CASCADE)
    ratings = models.IntegerField(default=1)


class SubjectObject(models.Model):
    weight = models.DecimalField(max_digits=8, decimal_places=8, default=.5)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    object = models.ForeignKey(Obj, on_delete=models.CASCADE)
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
    object = models.ForeignKey(Obj, on_delete=models.CASCADE)
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
    object = models.ForeignKey(Obj, on_delete=models.CASCADE)
    gerund = models.ForeignKey(Gerund, on_delete=models.CASCADE)
    ratings = models.IntegerField(default=1)


class ObjectImage(models.Model):
    weight = models.DecimalField(max_digits=8, decimal_places=8, default=.5)
    object = models.ForeignKey(Obj, on_delete=models.CASCADE)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    ratings = models.IntegerField(default=1)


class GerundImage(models.Model):
    weight = models.DecimalField(max_digits=8, decimal_places=8, default=.5)
    gerund = models.ForeignKey(Gerund, on_delete=models.CASCADE)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    ratings = models.IntegerField(default=1)

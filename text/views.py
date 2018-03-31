from django.shortcuts import render
import random

from text.models import Subject, Verb, Obj, Gerund, Image


def create_meme(request):
    # select a random order to choose items in
    items = [Subject, Obj, Verb, Gerund, Image]
    random.shuffle(items)
    print(items)
    # select first item favoring higher rated items
    sub = None
    obj = None
    verb = None
    gerund = None
    image = None
    for item in items:
        qs = item.objects.all()
        maxi = 0
        sub_list = []
        for subject in qs:
            subject.calculate_weighting(sub, verb, obj, gerund, image)
            maxi += float(subject.calc_weight)
            sub_list.append(subject)
        value = random.random() * maxi
        for subject in sub_list:
            if value < subject.calc_weight:
                if item == Subject:
                    sub = subject
                if item == Obj:
                    obj = subject
                if item == Verb:
                    verb = subject
                if item == Gerund:
                    gerund = subject
                if item == Image:
                    image = subject
                break
            value -= float(subject.calc_weight)
    print(image)
    return render(request, 'test.html', {
        'subject': sub,
        'verb': verb,
        'object': obj,
        'gerund': gerund,
        'image': image
    })

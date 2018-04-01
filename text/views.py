from django.shortcuts import render
import random

from text.models import Subject, Verb, Obj, Gerund, Image, SubjectVerb, SubjectObject, SubjectGerund, SubjectImage, \
    VerbObject, VerbGerund, VerbImage, ObjectGerund, ObjectImage, GerundImage, Meme


def create_meme(request):
    if request.POST:
        rating = int(request.POST['rating'])
        rv = (rating - 1) / 4.0
        print(rv)
        sub = Subject.objects.get(id=int(request.POST['subject']))
        obj = Obj.objects.get(id=int(request.POST['object']))
        verb = Verb.objects.get(id=int(request.POST['verb']))
        gerund = Gerund.objects.get(id=int(request.POST['gerund']))
        image = Image.objects.get(id=int(request.POST['image']))
        if rating == 5:
            Meme.objects.get_or_create(subject=sub, object=obj, verb=verb, gerund=gerund, image=image)
        sub.ratings += 1
        sub.weight = (float(sub.weight) + rv) / sub.ratings
        sub.save()
        obj.ratings += 1
        obj.weight = (float(obj.weight) + rv) / obj.ratings
        obj.save()
        verb.ratings += 1
        verb.weight = (float(verb.weight) + rv) / verb.ratings
        verb.save()
        gerund.ratings += 1
        gerund.weight = (float(gerund.weight) + rv) / gerund.ratings
        gerund.save()
        image.ratings += 1
        image.weight = (float(image.weight) + rv) / image.ratings
        image.save()
        sv = SubjectVerb.objects.get(subject=sub, verb=verb)
        sv.ratings += 1
        sv.weight = (float(sv.weight) + rv) / sv.ratings
        sv.save()
        so = SubjectObject.objects.get(subject=sub, object=obj)
        so.ratings += 1
        so.weight = (float(so.weight) + rv) / so.ratings
        so.save()
        sg = SubjectGerund.objects.get(subject=sub, gerund=gerund)
        sg.ratings += 1
        sg.weight = (float(sg.weight) + rv) / sg.ratings
        sg.save()
        si = SubjectImage.objects.get(subject=sub, image=image)
        si.ratings += 1
        si.weight = (float(si.weight) + rv) / si.ratings
        si.save()
        vo = VerbObject.objects.get(verb=verb, object=obj)
        vo.ratings += 1
        vo.weight = (float(vo.weight) + rv) / vo.ratings
        vo.save()
        vg = VerbGerund.objects.get(verb=verb, gerund=gerund)
        vg.ratings += 1
        vg.weight = (float(vg.weight) + rv) / vg.ratings
        vg.save()
        vi = VerbImage.objects.get(verb=verb, image=image)
        vi.ratings += 1
        vi.weight = (float(vi.weight) + rv) / vi.ratings
        vi.save()
        og = ObjectGerund.objects.get(object=obj, gerund=gerund)
        og.ratings += 1
        og.weight = (float(og.weight) + rv) / og.ratings
        og.save()
        oi = ObjectImage.objects.get(object=obj, image=image)
        oi.ratings += 1
        oi.weight = (float(oi.weight) + rv) / oi.ratings
        oi.save()
        gi = GerundImage.objects.get(gerund=gerund, image=image)
        gi.ratings += 1
        gi.weight = (float(gi.weight) + rv) / gi.ratings
        gi.save()

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


def perfect(request):
    memes = Meme.objects.all()
    return render(request, 'gallery.html', {'memes': memes, })
import os, django
from django.shortcuts import render, get_object_or_404


def add_review(review, brand):
    r = Reviews.objects.get_or_create(review = review, brand = brand)[0].save
    return r

def add_brand():
    Brands.objects.get_or_create(brand = "Duck Tours")[0].save
    Brands.objects.get_or_create(brand = "Skyline Luge")[0].save
    Brands.objects.get_or_create(brand = "Kenko Wellness")[0].save
    Brands.objects.get_or_create(brand = "Wave House Sentosa")[0].save

def populate():
    f = open('brand_profiles/newcorpus/DuckTours.txt', 'r')
    input_text = f.read().split('\n')
    input_text = [x for x in input_text if x!='']
    input_text = [x.split('\t\t') for x in input_text]
    temp = []
    for x in input_text:
        if len(x) == 2:
            temp.append(x[1])
        else:
            temp.append(x[0])

    input_text = temp
    duck_brand = Brands.objects.get(brand="Duck Tours")
    for review in input_text:
        add_review(review = review, brand = duck_brand)
    # add_brand()


if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'text_analysis_api.settings')
    django.setup()
    from brand_profiles.models import Reviews, Brands
    # populate()
    # print get_object_or_404(Reviews, pk=1)
    b = Reviews.objects.all()
    for a in b:
        print a.brand, a.review

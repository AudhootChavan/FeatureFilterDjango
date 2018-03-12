import os
# Configure settings for project
# Need to run this before calling models from application!
os.environ.setdefault('DJANGO_SETTINGS_MODULE','filter.settings')

import django
# Import settings
django.setup()

import random
from filter_app.models import Data


# Script to populate model with fake data



def populate(N = 5):
    name_num_1 = 0
    type_num = 0
    obj_num = 0
    sent_num = 0
    seg_num = 0
    img_num = 1
    for i in range(N):

        # letters and numbers for random naming
        name_num_1 = random.randint(0,4)
        name_string = 'ABCDE'
        name_num_2 = random.randint(0,20)
        name_fake = name_string[name_num_1] + str(name_num_2)

        # Type
        type_num = random.randint(0,2)
        type_list = ['pdf', 'ppt', 'docx']
        type_fake = type_list[type_num]


        # Objective
        obj_num = random.randint(0,2)
        obj_list = ['Awareness', 'Engagement', 'Trials']
        obj_fake = obj_list[obj_num]

        # Sentiment
        sent_num = random.randint(0,4)
        sent_list = ['Youth', 'Action', 'Happiness', 'Motherhood', 'Care']
        sent_fake = sent_list[sent_num]

        # Segment
        seg_num = random.randint(0,5)
        seg_list = ['AA', 'BB', 'AB', 'CC', 'AC', 'BC']
        seg_fake = seg_list[seg_num]

        # Images
        img_num = random.randint(1,16)
        image_link =  '/img/1.jpg'
        image_link = image_link.replace('1', str(img_num))

        # Save to model
        data = Data.objects.get_or_create(name= name_fake,
                                            type_of = type_fake,
                                            brand_obj = obj_fake,
                                            brand_sent = sent_fake,
                                            seg = seg_fake,
                                            image = image_link)[0]

        # print(name_fake, type_fake, obj_fake, sent_fake, seg_fake, image_link)



if __name__ == '__main__':
    print("Populating the databases...Please Wait")
    populate(10)
    print('Populating Complete')

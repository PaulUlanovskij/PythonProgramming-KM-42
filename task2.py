import json

with open("image_info_test-dev2017.json", 'r') as file:
    contents = json.load(file)
    images = contents['images']
    categories = contents['categories']

    biggest_number = 0
    biggest_name = ''
    img_1 = None

    for image in images:
        name = image['file_name']
        number = int(name[:len(name)-4])

        if number == 1:
            img_1 = image

        if number > biggest_number:
            biggest_number = number
            biggest_name = name

    print("Images count:", len(images))
    print("Categories count:", len(categories))
    print(f"""
Image: {img_1['file_name']}
URL: {img_1['coco_url']}
Height: {img_1['height']}
Width {img_1['width']}
ID: {img_1['id']}
""")
    print("Name of image with biggest number:", biggest_name)

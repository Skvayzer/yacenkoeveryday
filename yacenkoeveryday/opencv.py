# import cv2
#
# # Load the cascade
# face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# # Read the input image
# img = cv2.imread('tester.jpg')
# # Convert into grayscale
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# # Detect faces
# faces = face_cascade.detectMultiScale(gray, 1.1, 4)
# # Draw rectangle around the faces
# for (x, y, w, h) in faces:
#     cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
# # Display the output
# cv2.imshow('img', img)
# cv2.waitKey()

import face_recognition
from PIL import Image, ImageDraw
import numpy as np
import urllib.request

picture = face_recognition.load_image_file("tester.jpg")
yacenko_face_encoding = face_recognition.face_encodings(picture)[0]

# my_face_encoding now contains a universal 'encoding' of my facial features that can be compared to any other picture of a face!

k=3
for i in range(10,92):

    print(i)

    urllib.request.urlretrieve("paste_image_url_here" + str(i) + ".JPG", "original/" + str(i) + ".JPG")
    unknown_image = face_recognition.load_image_file("original/" + str(i) +".JPG")
    # unknown_face_encoding = face_recognition.face_encodings(unknown_image)[0]

    face_locations = face_recognition.face_locations(unknown_image)
    face_encodings = face_recognition.face_encodings(unknown_image, face_locations)

    known_face_encodings = [
        yacenko_face_encoding
    ]
    known_face_names = [
        "Yacenko"
    ]

    # Now we can see the two face encodings are of the same person with `compare_faces`!

    # results = face_recognition.compare_faces([face_encoding], unknown_face_encoding)

    # if results[0] == True:
    #     print("It's the same person!")
    # else:
    #     print("It's not the same person!")

    # pil_image = Image.fromarray(unknown_image)
    # Create a Pillow ImageDraw Draw instance to draw with
    # draw = ImageDraw.Draw(pil_image)

    im=Image.open("original/" + str(i) +".JPG")

    # Loop through each face found in the unknown image
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        # See if the face is a match for the known face(s)
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

        name = "Unknown"

        # If a match was found in known_face_encodings, just use the first one.
        # if True in matches:
        #     first_match_index = matches.index(True)
        #     name = known_face_names[first_match_index]

        # Or instead, use the known face with the smallest distance to the yacenkoeveryday face
        face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
        best_match_index = np.argmin(face_distances)
        if matches[best_match_index]:
            name = known_face_names[best_match_index]
            if left<=200: left=200
            if top<=200: top=200
            width, height = im.size
            if right+200>=width: right=width-200
            if bottom+400>=height: bottom=height-400
            im1=im.crop((left-200,top-200,right+200,bottom+400))
            im1.save("found/" + str(k) +".jpg")
            k=k+1
            break





        # # Draw a box around the face using the Pillow module
        # draw.rectangle(((left, top), (right, bottom)), outline=(0, 0, 255))
        #
        # # Draw a label with a name below the face
        # text_width, text_height = draw.textsize(name)
        # draw.rectangle(((left, bottom - text_height - 10), (right, bottom)), fill=(0, 0, 255), outline=(0, 0, 255))
        # draw.text((left + 6, bottom - text_height - 5), name, fill=(255, 255, 255, 255))


    # Remove the drawing library from memory as per the Pillow docs
    # del draw

    # Display the resulting image
    # pil_image.show()

#im1.show()
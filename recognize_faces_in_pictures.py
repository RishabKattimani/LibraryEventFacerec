import face_recognition


#
# # Load the jpg files into numpy arrays
elon_image = face_recognition.load_image_file("elon.jpeg")
elon_face_encoding = face_recognition.face_encodings(elon_image)[0]

known_face_encodings = [elon_face_encoding]

unknown_image = face_recognition.load_image_file("elon-people.jpeg")

face_locations = face_recognition.face_locations(unknown_image)
face_encodings = face_recognition.face_encodings(unknown_image, face_locations)

for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
    matches = face_recognition.compare_faces(known_face_encodings, face_encoding)


    print(matches)

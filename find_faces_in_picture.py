import face_recognition

# Load the image
image = face_recognition.load_image_file('elon-people.jpeg')

# Find all the faces in the image
face_locations = face_recognition.face_locations(image)

# Print the location of each face in the image
for face_location in face_locations:
    top, right, bottom, left = face_location
    print("A face is located at pixel location Top: {}, Left: {}, Bottom: {}, Right: {}".format(top, left, bottom, right))

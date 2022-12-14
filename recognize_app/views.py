import face_recognition
from rest_framework.response import Response
from rest_framework.decorators import api_view

from PIL import Image
import numpy as np


@api_view(['POST'])
def faceID(request):    
    # image being sent from Frontend

    print(request.FILES.get('file1'))
    print(request.FILES.get('file2'))

    camera_img = Image.open(request.FILES.get('file1'))
    camera_img_encode = np.asarray(camera_img)


    original_img= Image.open(request.FILES.get('file2'))
    original_img_encode = np.asarray(original_img)




    face_locations = face_recognition.face_locations(camera_img_encode)
    face_encodings = face_recognition.face_encodings(camera_img_encode, face_locations)


    original_img_locations = face_recognition.face_locations(original_img_encode)
    original_img_encodings = face_recognition.face_encodings(original_img_encode, original_img_locations)[0]

    result = face_recognition.compare_faces(original_img_encodings, face_encodings)
    data = {'Reponse': result[0]}

    return Response(data)

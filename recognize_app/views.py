import face_recognition
from rest_framework.decorators import api_view
from rest_framework.response import Response

from PIL import Image
import numpy as np


@api_view(['POST'])
def faceID(request):    
    # image being sent from Frontend

    print(request.FILES.get('file1'))
    print(request.FILES.get('file2'))

    if request.FILES.get('file1') == None or request.FILES.get('file2') == None:
        return Response({'Error': 'Missing file'})


    try:
        camera_img = Image.open(request.FILES.get('file1')).convert('RGB')
        camera_img_encode = np.asarray(camera_img)


        original_img = Image.open(request.FILES.get('file2')).convert('RGB')
        original_img_encode = np.asarray(original_img)


        face_locations = face_recognition.face_locations(camera_img_encode, model='cnn')
        face_encodings = face_recognition.face_encodings(camera_img_encode, face_locations)[0]


        original_img_locations = face_recognition.face_locations(original_img_encode, model='cnn')
        original_img_encodings = face_recognition.face_encodings(original_img_encode, original_img_locations)


        result = face_recognition.compare_faces(original_img_encodings, face_encodings, tolerance=0.5)
        data = {'Reponse': result[0]}

    except Exception as error:
        data = {'Response': 'Error occured'}

    return Response(data)



import face_recognition
from rest_framework.response import Response
from rest_framework.decorators import api_view
from users_app.models import User

from PIL import Image
import numpy as np
from django.shortcuts import get_object_or_404


@api_view(['POST'])
def faceID(request):
    user = get_object_or_404(User, email=request.data['email'])
    
    # image being sent from Frontend

    print(request.FILES.get('file'))
    camera_img = Image.open(request.FILES.get('file'))

    camera_img_encode = np.asarray(camera_img)


    # image from DB
    original_image = user.image


    face_locations = face_recognition.face_locations(camera_img_encode)
    face_encodings = face_recognition.face_encodings(camera_img_encode, face_locations)

    old_image_load = face_recognition.load_image_file(original_image)
    old_image_encoding = face_recognition.face_encodings(old_image_load)[0]

    result = face_recognition.compare_faces(old_image_encoding, face_encodings)
    data = {'Reponse': result[0]}

    return Response(data)

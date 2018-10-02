# FacialRecognitionAPI

This is an API which expands upon functionality the ageitgey face_recognition library.
https://github.com/ageitgey/face_recognition.

Project is a proof of concept for using facial recognition for patient identification in impoverished areas, without suitable form
of unique identification. 

Functions:
(POST /register) 
Add new face. Submit as web form with 'name' and 'image'. Supported image types are JPEG and PNG. Facial vector data is stored
instead of images, allows for faster identificaion, and scalability (vector data is only about 1kb per face)

(POST /identify)
Find the closest match to the submitted face. Returns list of results by highest probable match. If no values are below .55,
it is highly probable the submitted face is not in the registry.

(POST /save)
Saves the current facial recognition data for use upon next launch of the server, or to be used by another server.
Saves data in source directory as "registry.p"

(POST /load)
Load the saved facial recognition data. Place file in source directory as "registry.p"



from flask import Flask, request, jsonify
import face_recognition
import operator
import pickle
import time


app = Flask(__name__)
known_faces = {}

# code based on:
# https://github.com/ageitgey/face_recognition/blob/master/examples/web_service_example.py
@app.route('/identify', methods=["POST"])
def identify_photo():
    start_time = time.time()
    image = face_recognition.load_image_file(request.files['image'])
    id_encoding = face_recognition.face_encodings(image)
    if len(id_encoding) != 1:
        return "error, none or too many faces"
    id_encoding = id_encoding[0]
    matches = {}
    face_enc_time = time.time()
    print(face_enc_time-start_time)
    for name, encoding in known_faces.items():
        matches[name] = (float(face_recognition.face_distance(encoding, id_encoding)))
        cur_time = time.time()
        print(cur_time-face_enc_time)
    results = sorted(matches.items(), key=lambda kv: kv[1])
    total_time = time.time()
    print(total_time-start_time)
    return jsonify(results)


@app.route('/register', methods=["POST"])
def register_face():
    name = str(request.form['name'])
    if name in known_faces:
        return 'name already registered'
    image = face_recognition.load_image_file(request.files['image'])
    encoding = face_recognition.face_encodings(image)
    if len(encoding) != 1:
        return "error, none or too many faces"
    known_faces[name] = encoding
    return 'registered as ' + name

@app.route('/save', methods=["POST"])
def save_known_faces():
    global known_faces
    output = open('registry.p', 'wb')
    pickle.dump(known_faces, output)
    output.close()
    return 'registry saved'


@app.route('/load', methods=["POST"])
def load_known_faces():
    load_faces()
    return 'registry_loaded'


def load_faces():
    global known_faces
    data_in = open('registry.p', 'rb')
    known_faces = pickle.load(data_in)
    data_in.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0')
import os
import face_recognition
import json

def detect_faces(input_folder):
    results = {}
    known_encodings = []

    for image_file in os.listdir(input_folder):
        image_path = os.path.join(input_folder, image_file)

        if image_file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
            image = face_recognition.load_image_file(image_path)
            
            
            face_locations = face_recognition.face_locations(image, number_of_times_to_upsample=1, model='cnn')
            face_encodings = face_recognition.face_encodings(image, face_locations)

            for i, face_encoding in enumerate(face_encodings):
                match = None

                for j, known_encoding in enumerate(known_encodings):
                    results_j = face_recognition.compare_faces([known_encoding], face_encoding)
                    if True in results_j:
                        match = j
                        break

                if match is not None:
                    person_key = f"person-{match + 1}"
                else:
                    known_encodings.append(face_encoding)
                    person_key = f"person-{len(known_encodings)}"

                if person_key not in results:
                    results[person_key] = {
                        "name": person_key,
                        "images": []
                    }

                results[person_key]["images"].append(image_path)

    return results

def main():
    
    input_folder = "/home/herbeth-lks/Downloads/faces"

    results = detect_faces(input_folder)

    
    json_result = json.dumps(results, indent=4)
    print(json_result)

    
    with open('output_otimizado.json', 'w') as json_file:
        json_file.write(json_result)

if __name__ == "__main__":
    main()

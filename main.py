import os
import face_recognition
import json
from PIL import Image

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
                        "images": [],
                        "face_positions": []  
                    }

                results[person_key]["images"].append(image_path)
                results[person_key]["face_positions"].append(face_locations[i]) 

    return results

def main():
    input_folder = "/home/herbeth-lks/Downloads/faces"

    results = detect_faces(input_folder)

    for person_key, person_data in results.items():
        for i, image_path in enumerate(person_data["images"]):
            face_location = person_data["face_positions"][i]

            original_image = Image.open(image_path)

            top, right, bottom, left = face_location

            face_image = original_image.crop((left, top, right, bottom))

           
            output_path = f"output_{person_key}_face_{i + 1}.jpg"
            face_image.save(output_path)

            print(f"Recorte de rosto salvo em {output_path}")

    json_result = json.dumps(results, indent=4)
    print(json_result)

    with open('output_otimizado.json', 'w') as json_file:
        json_file.write(json_result)

    print("Recortes de rostos e JSON salvos com sucesso.")

if __name__ == "__main__":
    main()

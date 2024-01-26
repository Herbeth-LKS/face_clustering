# Face Recognition Project

This GitHub repository contains a Python script for face recognition using the `face_recognition` library. The script detects faces in images, crops and saves the faces as individual images, and generates a JSON file with information about the recognized faces.

## Getting Started

To use this script, follow these steps:

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/face-recognition.git
   cd face-recognition
   ```

2. **Install Dependencies:**
   Make sure you have Python installed on your system. Install the required libraries using:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Script:**
   ```bash
   python face_recognition_script.py
   ```

## Usage

- Place the images you want to process in a folder and update the `input_folder` variable in the script with the path to your folder.

- The script will detect faces, crop them, save the cropped faces as individual images, and generate a JSON file (`output_otimizado.json`) with information about the recognized faces.

## Dependencies

- [face_recognition](https://github.com/ageitgey/face_recognition): A simple face recognition library.
- [Pillow (PIL Fork)](https://pillow.readthedocs.io/en/stable/): A powerful image processing library.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or create a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgments

- Special thanks to the authors of the `face_recognition` library for providing a simple and effective face recognition solution.

Feel free to customize this README according to your project's specific details and requirements.

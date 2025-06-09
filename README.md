Number Plate Detection using EasyOCR and OpenCV in Google Colab
This project performs automatic number plate detection from images using EasyOCR, OpenCV, and Python. It detects all text in an image and then filters out likely number plates based on a customizable regular expression (regex).

🚀 Features
Upload image directly from your local machine in Google Colab.

Detect text using EasyOCR.

Draw bounding boxes around detected text.

Filter potential number plates using a regex pattern (customizable by country).

Display and save output image with annotations.

Download the processed image directly from Colab.

🧰 Requirements
Python 3.x

Google Colab (recommended) or Jupyter Notebook

Required Python libraries:

easyocr

opencv-python-headless

numpy

matplotlib

re (Python built-in)

google.colab (for file upload/download in Colab)

🔧 Installation
If running in Google Colab:

python
Copy
Edit
!pip install easyocr
!pip install opencv-python-headless
If running locally:

bash
Copy
Edit
pip install easyocr opencv-python-headless matplotlib numpy
📸 How to Use
Upload your image using:

python
Copy
Edit
from google.colab import files
uploaded = files.upload()
OCR and Detection:

The image is converted to grayscale for better OCR results.

Text is detected with EasyOCR.

Bounding boxes are drawn for all detected texts.

Number Plate Filtering:

Text is filtered using a regex pattern designed for Indian number plates:

python
Copy
Edit
plate_pattern = r'^[A-Z]{2}[0-9]{1,2}[A-Z]{1,2}[0-9]{4}$'
You can adjust this regex pattern depending on your country’s license plate format.

Result Display:

The annotated image (with detected boxes) is shown using matplotlib.

The output image is saved and can be downloaded in Colab.

✅ Example Output
pgsql
Copy
Edit
--- All Detected Texts ---
Detected Text: 'MH12AB1234' with Confidence: 0.89

--- Possible Number Plates Detected ---
Number Plate: MH12AB1234
The image will show a bounding box around the detected plate.

⚠️ Notes
The regex pattern is currently set for Indian license plates. Modify as needed.

Low-confidence detections (probability < 0.5) are filtered out.

Best used in well-lit, high-resolution images for higher accuracy.

📝 To Customize:
Regex for your country's plates?
Change:

python
Copy
Edit
plate_pattern = r'^[A-Z]{2}[0-9]{1,2}[A-Z]{1,2}[0-9]{4}$'
Examples:

US Plates: r'^[A-Z0-9]{5,8}$'

EU Plates: r'^[A-Z]{1,3}-[A-Z]{1,2} [0-9]{1,4}$'

👨‍💻 Author
Created as an example of using EasyOCR + OpenCV for Number Plate Detection in Google Colab.


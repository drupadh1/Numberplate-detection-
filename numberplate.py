# Install dependencies
!pip install opencv-python-headless easyocr matplotlib

# Upload image
from google.colab import files
uploaded = files.upload()

# Import necessary libraries
import cv2
import easyocr
import numpy as np
from matplotlib import pyplot as plt

# Load image
image_path = next(iter(uploaded))
image = cv2.imread(image_path)

# Initialize EasyOCR reader
reader = easyocr.Reader(['en'])

# Perform OCR
results = reader.readtext(image)

# Draw boxes and display results
output_image = image.copy()
for (bbox, text, prob) in results:
    if prob > 0.5:  # Filter by confidence
        print(f"Detected: {text} (Confidence: {prob:.2f})")
        pts = np.array(bbox, dtype=np.int32)
        cv2.polylines(output_image, [pts], isClosed=True, color=(0, 255, 0), thickness=2)
        cv2.putText(output_image, text, tuple(pts[0]), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2)

# Show result
plt.figure(figsize=(10,6))
plt.imshow(cv2.cvtColor(output_image, cv2.COLOR_BGR2RGB))
plt.title("Number Plate Detection")
plt.axis('off')
plt.show()
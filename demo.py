import numpy as np
from PIL import Image
from tensorflow import keras

# Load the model
model = keras.models.load_model('mnist_model.h5')

# Load the image
image = Image.open('demo.png').convert('L')  # Convert to grayscale if needed
image = np.array(image)

# Preprocess the image
image = image / 255.0  # Scale pixel values to range [0, 1]
image = image.reshape(1, 28, 28)  # Reshape to match model input shape

# Make predictions
predictions = model.predict(image)

# Interpret the predictions
predicted_digit = np.argmax(predictions)
print("Predicted Digit:", predicted_digit)

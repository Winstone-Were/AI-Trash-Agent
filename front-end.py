import tensorflow as tf
import numpy as np
import cv2

# Load the TFLite model
interpreter = tf.lite.Interpreter(model_path='waste_sorting_model.tflite')
interpreter.allocate_tensors()

# Get input and output details
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

# Class names mapping (replace these with your actual class names)
class_names = {
    0: "battery",
    1: "biological",
    2: "brown-glass",
    3: "cardboard",
    4: "clothes",
    5: "green-glass",
    6: "metal",
    7: "paper",
    8: "plastic",
    9: "shoes",
    10: "trash",
    11: "white-glass"
}

cap = cv2.VideoCapture(0)  # Use 0 for the default camera, or 1 for an external camera
if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

# Set camera resolution (optional)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

def preprocess_frame(frame, input_size=(150, 150)):  # Replace (224, 224) with your model's input size
    frame_resized = cv2.resize(frame, input_size)
    frame_normalized = frame_resized / 255.0  # Normalize to [0, 1]
    frame_expanded = frame_normalized[np.newaxis, ...]  # Add batch dimension
    return frame_expanded.astype(np.float32)  # Convert to float32

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break

    # Preprocess the frame
    processed_frame = preprocess_frame(frame, input_size=(150, 150))  # Replace with your input size

    # Set input tensor
    interpreter.set_tensor(input_details[0]['index'], processed_frame)

    # Run inference
    interpreter.invoke()

    # Get predictions
    output_data = interpreter.get_tensor(output_details[0]['index'])
    class_id = output_data.argmax()  # Get the class with the highest probability
    confidence = output_data[0][class_id]
    class_name = class_names.get(class_id, "Unknown")  # Get class name
    
    # Display the results
    cv2.putText(frame, f"Class: {class_name}, Confidence: {confidence:.2f}", 
                (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.imshow("Camera Feed", frame)

    # Break on pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

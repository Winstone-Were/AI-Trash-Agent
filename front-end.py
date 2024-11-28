import tensorflow as tf
import numpy as np
import cv2
import time
import serial  # For serial communication with Arduino

# Initialize serial communication with Arduino
arduino = serial.Serial(port='/dev/ttyUSB0', baudrate=115200, timeout=1)  # Update '/dev/ttyUSB0' as needed

# Load the TFLite model
interpreter = tf.lite.Interpreter(model_path='waste_sorting_model.tflite')
interpreter.allocate_tensors()

# Get input and output details
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

# Class names mapping
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

# Initialize camera
cap = cv2.VideoCapture(0)  # Use 0 for default camera
if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

# Preprocessing function
def preprocess_frame(frame, input_size=(150, 150)):
    frame_resized = cv2.resize(frame, input_size)
    frame_normalized = frame_resized / 255.0
    frame_expanded = frame_normalized[np.newaxis, ...]
    return frame_expanded.astype(np.float32)

# Main loop
while True:
    # Read camera frame
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame.")
        break

    # Preprocess the frame
    processed_frame = preprocess_frame(frame)

    # Run inference
    interpreter.set_tensor(input_details[0]['index'], processed_frame)
    interpreter.invoke()
    output_data = interpreter.get_tensor(output_details[0]['index'])

    # Get predicted class and confidence
    class_id = output_data.argmax()
    confidence = output_data[0][class_id]
    class_name = class_names.get(class_id, "Unknown")

    # Display results
    cv2.putText(frame, f"Class: {class_name}, Conf: {confidence:.2f}",
                (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Check motion sensor (simulated via keyboard for testing)
    motion_detected = True  # Replace with actual GPIO input if needed

    # Determine LED state
    if motion_detected and class_name in ["plastic", "battery"] and confidence > 0.3:
        arduino.write(b"RED\n")
    else:
        arduino.write(b"GREEN\n")

    # Show camera feed
    cv2.imshow("Camera Feed", frame)

    # Quit on 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Cleanup
cap.release()
cv2.destroyAllWindows()

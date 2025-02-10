# Waste Sorting System Using AI and Arduino

## Overview

This project implements an **AI-powered waste sorting system** using **TensorFlow Lite (TFLite)** for real-time object classification and an **Arduino** to control LEDs based on the detected waste type. The system captures live images using a webcam, classifies them into one of 12 waste categories, and triggers an LED indicator for sorting guidance.

## Features

- **Real-time waste classification** using a deep learning model (DenseNet121-based).
- **Live video feed** processing with OpenCV.
- **TensorFlow Lite inference** for efficient on-device processing.
- **Arduino-controlled LED indicators** to assist sorting.
- **Serial communication** between Python and Arduino.
- **Motion detection support** (simulated via software, but can be integrated with a motion sensor).

---

## Hardware Requirements

- **Raspberry Pi / PC** (for running the AI model)
- **Arduino (Uno, Mega, or similar)** (for LED control)
- **Camera (USB Webcam or Pi Camera)**
- **LEDs** (Red & Green for classification feedback)
- **Wires & Breadboard** (for circuit connections)
- **Motion Sensor** (optional, for automation)

---

## Software Requirements

- **Operating System:** Linux (Ubuntu, Raspberry Pi OS, Manjaro, etc.) or Windows
- **Python 3.7+**
- **TensorFlow Lite**
- **OpenCV** (`cv2`)
- **NumPy**
- **PySerial** (for Arduino communication)
- **Arduino IDE** (for programming the microcontroller)

---

## Installation & Setup

## Running
### Aquire Dataset

Download dataset bellow
[!Dataset](https://www.kaggle.com/datasets/mostafaabla/garbage-classification)


### 1️⃣ Install Dependencies

Ensure Python and required libraries are installed:

```bash
pip install tensorflow numpy opencv-python pyserial
```

### 2️⃣ Connect Arduino

- Connect **Red LED** to **Pin 9** (indicates non-recyclable waste like batteries, plastic, etc.).
- Connect **Green LED** to **Pin 10** (indicates recyclable waste).
- Ensure the correct serial port is used (`/dev/ttyUSB0` on Linux or `COMX` on Windows).

### 3️⃣ Load TensorFlow Lite Model

Ensure the model `waste_sorting_model.tflite` is in the project directory.

### 4️⃣ Run the Waste Sorting System

```bash
python waste_sorting.py
```

---

## Code Explanation

### 1️⃣ **Preprocessing & Inference**

- Captures a live frame.
- Resizes and normalizes the image for the TFLite model.
- Runs inference and predicts the waste category.

### 2️⃣ **LED Control via Arduino**

- If detected waste is **plastic or battery** and confidence is **above 30%**, the Red LED turns **ON**.
- Otherwise, the Green LED turns **ON**.
- Communicates via **Serial UART (115200 baud rate)**.

### 3️⃣ **Real-time Display**

- Overlays classification results on the camera feed.
- Stops when `q` is pressed.

---

## Example Output

Upon detecting a waste item, the system displays:

```
Class: Plastic, Conf: 0.85
RED LED ON (Non-recyclable waste)
```

---

## Possible Enhancements

- Integrate a **conveyor belt** for automated sorting.
- Improve accuracy by **fine-tuning DenseNet121**.
- Add a **motion sensor** for event-driven classification.
- Deploy on **Raspberry Pi** for an embedded AI system.

---

## License

This project is open-source under the **MIT License**.

---

## Acknowledgments

- Inspired by AI-driven environmental sustainability projects.
- Uses **TensorFlow Lite** for optimized inference.

---

🚀 **Now, start sorting waste with AI-powered automation!**


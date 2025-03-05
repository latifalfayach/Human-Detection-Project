# Human Detection using HOG Algorithm and SVM 

This project demonstrates human detection using the Histogram of Oriented Gradients (HOG) algorithm and SVM algorithm. The application is built with Streamlit for the user interface, allowing you to detect humans in images, videos, or real-time video feeds from a webcam.


## Features

- Detect humans in images.
- Detect humans in pre-recorded videos.
- Real-time human detection using webcam.


## Installation

Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the Streamlit app:
    ```bash
    python -m streamlit run Human_Detection_app.py --server.enableXsrfProtection false
    ```

2. Open your web browser and go to `http://localhost:8501` to see the app.

3. Use the sidebar to select the application mode:
    - **About App**: Learn about the application.
    - **Run on Image**: Upload an image and detect humans in it.
    - **Run on Video**: Upload a video or use your webcam to detect humans in the video.


## File Descriptions

- **Human_detection.py**: Contains the code for detecting humans using the HOG algorithm.
- **Human_detection_app.py**: The main Streamlit app that provides the user interface.


## Example

### Detecting Humans in an Image
![Example Image](./Testing/Screenshot%20.png)

### Detecting Humans in a Video
[Example Video](./Testing/video.mp4)
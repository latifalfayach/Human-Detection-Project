import streamlit as st
import cv2
import numpy as np
from PIL import Image
from Human_Detection import Detector

DEMO_IMAGE = './Testing/people.jpg'
DEMO_VIDEO = './Testing/in.mp4'

st.title('Human Detection using HOG Algorithm')

st.markdown(
    """
    <style>
    [data-testid = "stSidebar"][aria-expanded="true"] > div:first-child{
        width: 350px
    }
    [data-testid = "stSidebar"][aria-expanded="false"] > div:first-child{
        width: 350px
        margin-left: -350px
    }
    </style>

    """,
    unsafe_allow_html=True,

)
st.sidebar.markdown("""
            <style>
                div[data-testid="column"] {
                    width: fit-content !important;
                    flex: unset;
                }
                div[data-testid="column"] * {
                    width: fit-content !important;
                }
            </style>
            """, unsafe_allow_html=True)

st.sidebar.title('Human Detection Sidebar')
st.sidebar.subheader('Parameters')

@st.cache()
def image_resize(image, width=None, height=None, inter=cv2.INTER_AREA):

    # initialize the dimensions of the image to be resized and
    # grab the image size
    dim = None
    (h, w) = image.shape[:2]

    # if both the width and height are None, then return the
    # original image
    if width is None and height is None :
        return image
    
    # check to see if the width is None
    if width is None:
        # calculate the ratio of the height and construct the
        # dimensions
        r = width/float(w)
        dim = (int(w*r), height)

    # otherwise, the height is None   
    else:
        # calculate the ratio of the width and construct the
        # dimensions
        r = width/float(w)
        dim = (width, int(h*r))

    #resize the image
    resized = cv2.resize(image, dim, interpolation=inter)
    
    # return the resized image
    return resized

app_mode = st.sidebar.selectbox('Choose the App mode',
                                ['About App', 'Run on Image', 'Run on Video']
                                )

if app_mode == 'About App':
    st.markdown('In this application we are using HOG algorithm technique to **detect human** in images, videos or real time videos using webcam')

    st.markdown(
        """
        <style>
        [data-testid = "stSidebar"][aria-expanded="true"] > div:first-child{
            width: 350px
        }
        [data-testid = "stSidebar"][aria-expanded="false"] > div:first-child{
            width: 350px
            margin-left: -350px
        }
        </style>

        """,
        unsafe_allow_html=True,

    )
    st.video('https://www.youtube.com/watch?v=b_DSTuxdGDw')

elif app_mode == 'Run on Image':
    st.sidebar.markdown('---')

    st.markdown(
        """
        <style>
        [data-testid = "stSidebar"][aria-expanded="true"] > div:first-child{
            width: 350px
        }
        [data-testid = "stSidebar"][aria-expanded="false"] > div:first-child{
            width: 350px
            margin-left: -350px
        }
        </style>

        """,
        unsafe_allow_html=True,

    )

    img_file_buffer = st.sidebar.file_uploader("Upload an Image", type=['jpg', 'jpeg', 'png'])
    if img_file_buffer is not None:
        image = np.array(Image.open(img_file_buffer))
        st.sidebar.text('Original Image')
        st.sidebar.image(image)
        output_image = Detector(image)
        st.image(output_image, caption='Processed Image', use_column_width=True)
    else :
        demo_image = DEMO_IMAGE
        image = np.array(Image.open(demo_image))
        st.sidebar.text('Original Image')
        st.sidebar.image(image)
        output_image  = Detector(image)
        st.image(output_image, caption='Processed Image', use_column_width=True)


elif app_mode == 'Run on Video':
    
    col1 ,col2 = st.sidebar.columns([1,1])
    
    with col1 :
       use_webcam = st.button('Use Webcam')
    with col2 :
        use_video = st.button('Use Video')

    st.sidebar.markdown('---')

    if use_webcam:
        st.session_state['action'] = 'use_webcam'
    elif use_video:
        st.session_state['action'] = 'use_video'


    st.markdown(
        """
        <style>
        [data-testid = "stSidebar"][aria-expanded="true"] > div:first-child{
            width: 350px
        }
        [data-testid = "stSidebar"][aria-expanded="false"] > div:first-child{
            width: 350px
            margin-left: -350px
        }
        </style>

        """,
        unsafe_allow_html=True,

    )
    
    if 'action' in st.session_state and st.session_state['action'] == 'use_webcam':

        st.title("Webcam Live Feed")
        

        cap = cv2.VideoCapture(0)
        frame_placeholder = st.empty()
        stop_button_pressed = st.button("Stop")
        
        while cap.isOpened() and not stop_button_pressed:
            ret, frame = cap.read()
            if not ret:
                st.write("Video Capture Ended")
                break
            frame = Detector(frame)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            frame_placeholder.image(frame,channels="RGB")
            if cv2.waitKey(1) & 0xFF == ord("q") or stop_button_pressed:
                break
        cap.release()
        cv2.destroyAllWindows()

    else :
        vid_file_buffer = st.sidebar.file_uploader("Upload an Video", type=['avi', 'mp4'])

        if vid_file_buffer is not None:

            st.sidebar.text('Original video')
            video = st.sidebar.video(vid_file_buffer)

            cap = cv2.VideoCapture(f'./Testing/{vid_file_buffer.name}')
            img=[]
                

            for i in range(24):
                ret, frame = cap.read()
                output_frame = Detector(frame)
                img.append(output_frame)

            height,width,layers=img[1].shape

            video=cv2.VideoWriter('video.mp4',-1,1,(width,height))

            for j in range(24):
                video.write(img[j])
        
            video.release()
            
            st.video('video.mp4')

        else :
            st.sidebar.text('Original video')
            st.sidebar.video(DEMO_VIDEO)


            cap = cv2.VideoCapture(DEMO_VIDEO)
            img=[]
                

            for i in range(24):
                ret, frame = cap.read()
                output_frame = Detector(frame)
                img.append(output_frame)

            height,width,layers=img[1].shape

            video=cv2.VideoWriter('video.mp4',-1,1,(width,height))

            for j in range(24):
                video.write(img[j])

            video.release()
        
            st.video('video.mp4')






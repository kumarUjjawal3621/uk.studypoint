import streamlit as st
import base64
from PIL import Image

st.set_page_config(layout="wide", page_title="ukstudypoint",initial_sidebar_state="expanded",)
############
st.title("UK STUDY POINT")
st.write(" ")       
st.write(" ") 


###################

image_path = "background.png"
image = open(image_path, "rb").read()
image_base64 = base64.b64encode(image).decode()
style = f"""
    <style>
    [data-testid="stAppViewContainer"] > .main {{
        background-image: url(data:image/jpg;base64,{image_base64});
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: local;
    }}
    </style>
    """

st.markdown(style, unsafe_allow_html=True)

container = st.container()
with container:
    image_file = "image4.png"
    image = Image.open(image_file)
    col1, col2,col3 = st.columns([0.49,0.39,0.12],gap="large")
    with col1:
        st.image(image,use_column_width=True)
    with col2:
        st.header("About Us")
        st.write("""
         <p style='text-align: justify; line-height: 2'>
         We are passionate about helping students reach their academic goals and excel in their studies. 
         With [X] years of experience in online education, we have honed our expertise in providing 
         personalized and effective tutoring in Mathematics, Science & Programming
         </p>
         """,
         unsafe_allow_html=True)
        
        
    st.write(" ")  
    st.write(" ")       
    st.write(" ")  
    st.write(" ")  
    st.header("Our Services")
    st.write(
            """<ul style='list-style-type: circle; font-size: 500px; color: white;line-height: 3;'>
            <li>Curate a wide range of courses spanning various subjects, levels, and skill sets.</li>
            <li>Video lectures, interactive quizzes, assignments, and hands-on projects.</li>
            <li>Ensure up-to-date curriculum that aligns with industry trends and academic standards.</li>
            </ul>""",
            unsafe_allow_html=True
        )
    st.write(" ")       
    st.write(" ")  
    st.write(" ")
    
 
    st.header("Our Team")
    st.write(" ")  
    st.write(" ")
    col1, col2, col3,col4 = st.columns(4, gap="large")

    with col1:
        p1 = Image.open("p1.png")
        st.image(p1, use_column_width=True)   
        st.markdown("<div style='text-align: center;'><a href='https://www.linkedin.com/in/ujjawal-kumar-295b5123b/'>Mr. Utkarsh</a></div>", unsafe_allow_html=True)
        
    with col3:
        p2 = Image.open("p2.png")
        st.image(p2, use_column_width=True)
        st.markdown("<div style='text-align: center;'><a href='https://www.linkedin.com/in/ujjawal-kumar-295b5123b/'>Mr. Pushpesh</a></div>", unsafe_allow_html=True)
        
    # Contact us
    st.write(" ")  
    st.write(" ")
    st.title("Contact Us")
    st.write("Email: kumarujjawal3621@gmail.com")
    st.write("Call Us: +917256854292")

        
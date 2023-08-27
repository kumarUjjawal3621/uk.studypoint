
import requests
import streamlit as st
#from streamlit_lottie import st_lottie
from PIL import Image


st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style.css")

# ---- LOAD ASSETS ----
lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")
img_contact_form = Image.open("Chemistry.png")
img_contact_form2 = Image.open("Math.png")
img_lottie_animation = Image.open("Physics.png")
img_contact_form3=Image.open("animation.png")

# ---- HEADER SECTION ----
with st.container():
    st.markdown("<h1 style='color: blue;'>Welcome to StudyPoint</h1>", unsafe_allow_html=True)
    st.markdown("<h2 style='color: purple;'>Empowering Minds: Unleashing Student Excellence through Learning", unsafe_allow_html=True)
    st.write(
        """
        We are passionate about helping students reach their academic goals and excel in their studies. 
        With [X] years of experience in online education, we have honed our expertise in providing personalized 
        and effective tutoring in Mathematics, Science & Programming.
        """
    )
    st.write("[Learn More >](https://pythonandvba.com)")

# ---- WHAT I DO ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Our Services")
        st.write("##")
        st.write(
            """
            We offer a variety of services like:
            - Curate a wide range of courses spanning various subjects, levels, and skill sets.
            - Video lectures, interactive quizzes, assignments, and hands-on projects.
            - Ensure up-to-date curriculum that aligns with industry trends and academic standards."

            If this sounds interesting to you, consider subscribing and turning on the notifications, so you don’t miss any content.
            """
        )
        st.write("[YouTube Channel >](https://youtube.com/c/CodingIsFun)")
    with right_column:
        st.image(img_contact_form3)

# ---- PROJECTS ----
with st.container():
    st.write("---")
    st.header("Subjects")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_lottie_animation)
    with text_column:
        st.subheader("Physics")
        st.write(
            """
            Embark on a captivating journey through the realm of physics with our immersive online classes. 
            Our expert instructors will demystify complex concepts, making physics an exhilarating adventure of discovery.
             Join us and unlock the secrets of the universe while honing critical problem-solving skills for a brighter academic future.
            """
        )
        st.markdown("[Watch Video...](https://youtu.be/CCsQa5Aiexk)")
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_contact_form)
    with text_column:
        st.subheader("Chemistry")
        st.write(
            """
            Dive into the fascinating world of chemistry through our dynamic online classes, where students explore the elements,
             reactions, and mysteries that shape our everyday lives. Join us to ignite your passion for scientific exploration and
              gain a solid foundation in this fundamental discipline."
            """
        )
        st.markdown("[Watch Video...](https://youtu.be/FOULV9Xij_8)")

with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_contact_form2)
    with text_column:
        st.subheader("Mathematics")
        st.write(
            """
            Embark on a journey of mathematical exploration with our engaging online classes, where students unravel
             the beauty of numbers, patterns, and problem-solving. Join us to build a strong mathematical foundation,
              boost analytical thinking, and unlock the door to a universe of endless possibilities.
            """
        )
        st.markdown("[Watch Video...](https://youtu.be/FOULV9Xij_8)")

# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Contact US")
    st.write("##")

    # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/utkarshstm2016@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Name" required>
        <input type="email" name="email" placeholder="Email" required>
        <input type="email" name="email" placeholder="Mobile Number" required>
        <textarea name="message" placeholder="Write Message" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()

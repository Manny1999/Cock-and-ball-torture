from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie

# Used emojies at this site: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="My webpage", page_icon="tada:", layout="wide")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# Uses for Local CSS


def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")

# --- LOAD ASSETS ----

lottie_coding = load_lottieurl("https://lottie.host/437dd554-fafb-451c-b0af-183547127ae7/VqJ5JUyBUd.json")
img_contact_form = Image.open("images/spongebobs-cock-and-ball-torture-v0-ZXRrdnFscmRvd2FiMY3KSi84CutxwUnD6qGEA9sO3o15lMk5mT8X1b6XLKID.webp")
img_lottie_animation= Image.open("images/cock-and-balls-torture-set-not-for-beginner-447622.webp")

# ---HEADER SECTION ---
with st.container():
    st.header("Hi, I am Manny :wave:")
    st.title("I'm here to advertise cock and ball torture.")
    st.write("I am passionate about learnig how to slam a hammer aganist someones nut sack")
    st.write("[Learn More >] (https://en.wikipedia.org/wiki/Cock_and_ball_torture")
    
# ---WHAT I DO ---

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(
        """
         This webssite will show you the true meaning of cock and ball tortrue:
        -are we looking to have your cock torture slaped and sucked on a day-to-day bases.
        -Want to learn on how to slam your dick agaisnt the wall?
        
        Consider learning more in the follwoing video.
        
        """
        )
        st.write("[YouTube >](https://www.youtube.com/watch?v=nOPIu7isD3s)")
        
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")
    
    
    
# --- ANIMATION PROJECT ---
with st.container():
    st.write("---")
    st.header("Introduction Animation")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_lottie_animation)
    with text_column:
        st.subheader("Ball Torture Device Turorial")
        st.write(
    
           """
    
            Learn how your balls are being squish!
            Animation video explanies how most people expericen these kinds of pleasures
            In this tutorial, I'll show you how your balls turn red.
    
            """
    
        )
        st.markdown("[Watch Video...](https://www.youtube.com/watch?v=nhsRJjBaDBU)")
        
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_contact_form)
    with text_column:
        st.subheader("Spongbob Animation Tutorial")
        st.write(
            """
       
            WARNNING VIEWER DICREPTION IS ADVISED!!!!!!!!
            
            In this video you will learn how spongbob and patrick deal with cock ball torture.
            Please enjoy.
        
            """
            
        )
        st.markdown("[Watch This Video...](https://www.youtube.com/watch?v=fROoki_muIA)")
        
 # --- CONTACT ---
    with st.container():
        st.write("---")
        st.header("Contact Me for Further Information!")
        st.write("##")
    
        contact_form = """
        <form action="https://formsubmit.co/codingisfun.maninsito2000gmail.com" method="POST">
            <input type="hidden" name="_captcha" value="false">
            <input type="text" name="name" placeholder="Your name" required>
            <input type="email" name="email" placeholder="Your email" required>
            <textarea name="message" placeholder="Your message here" required></textarea>
            <button type="submit">Send</button>
        </form>
        """

        left_column, right_column = st.columns(2)
        with left_column:
            st.markdown(contact_form, unsafe_allow_html=True)
        with right_column:
            st.empty()
st.subheader("Copyright©1994-2024 United Parcel Service of American, Inc. All rights reserved")

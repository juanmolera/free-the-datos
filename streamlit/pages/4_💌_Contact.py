# Streamlit
import streamlit as st

# Images
from PIL import Image

# Streamlit page configuration
st.set_page_config(layout='wide', initial_sidebar_state='collapsed', page_title='Contact', page_icon='💌')

col1, col2, col3 = st.columns(3)

with col1:

    pass

with col2:


    image = Image.open('../images/roberto_capucha.png')
    st.image(image, use_column_width=True)
    #st.markdown('<a href="mailto:juan.molera@gmail.com">Mail me!</a>', unsafe_allow_html=True)

    st.header(":mailbox: Mail me!")


    contact_form = """
    <form action="https://formsubmit.co/juan.molera@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here"></textarea>
        <button type="submit">Send</button>
    </form>
    """

    st.markdown(contact_form, unsafe_allow_html=True)

    # Use Local CSS File
    def local_css(file_name):
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    local_css("css/style_mail.css")
    

with col3:

    pass
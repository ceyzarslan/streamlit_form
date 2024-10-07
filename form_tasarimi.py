import streamlit as st

st.set_page_config(layout='wide')
c1, c2, c3 = st.columns(3, gap='small')
with c1:
    with st.form("numbers"):
        age = st.number_input("Your Age: ", min_value=0, max_value=100)
        height = st.slider("Your height?", min_value=100, max_value=250, step=1)
        city = st.selectbox("Your birth city", ["ISTANBUL", "IZMIR", "ANKARA", "SIVAS"])
        fav_color = st.radio("Your favorite color:", ["Red", "Green", "Blue"])
        smoking = st.checkbox("Smoking?")
        age_btn = st.form_submit_button("Send")
    if age_btn:
        st.write(f"Your Age:  {age}")
        st.write(f"Your height:  {height}")
        st.write(f"Your City of Birth: {city}")
        st.write(f"Your favorite color:  {fav_color}")
        st.write(f"Smoking?: {smoking}")
with c2:
    with st.form("my_form"):
        st.write("Sample form:")
        name = st.text_input("Fullname: ")
        email = st.text_input("Email: ")
        phone_number = st.text_input("Phone Number: ")
        subject = st.text_input("Subject: ")
        message = st.text_area("Message")

        btn = st.form_submit_button("Gönderelim")
    if btn:
        st.write(f"Fullname:{name}")
        st.write(f"E-mail:{email}")
        st.write(f"phone_number:{phone_number}")
        st.write(f"message:{message}")
with c3:
    with st.form("advance"):
        hobbies = st.multiselect("Select your hobbies: ", ['Swim', 'Run', 'Coffee', 'Gaming', 'Reading'])
        dt1, dt2 = st.columns(2, gap='small')  # yanyana oluşturmak için column oluşturuyoruz
        with dt1:
            start = st.date_input("Start date: ", )
        with dt2:
            end = st.date_input("End Date: ")

        color = st.color_picker("Select a color: ")
        file = st.file_uploader("Uplaoad an image:", type=['png', 'jpeg'])
        adv_btn = st.form_submit_button("Gönderelim")

    if file is not None:
        st.write("Başarıyla yüklendi")
        with open(file.name, "wb") as f:
            f.write(file.getbuffer())

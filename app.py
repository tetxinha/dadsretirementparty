import streamlit as st
from PIL import Image
import time
import datetime
import base64


st.title('🥳 Parabéns, Papá 🥳')


papa_image = Image.open('data/daddy.jpeg')
st.image(papa_image)
wait_string = st.text('')

def countdown(stop):
    while True:
        difference = stop - datetime.datetime.now()
        count_hours, rem = divmod(difference.seconds, 3600)
        count_minutes, count_seconds = divmod(rem, 60)

        if difference.days == 0 and count_hours == 0 and count_minutes == 0 and count_seconds == 0:
            wait_string.text("🏝 A REFORMA CEHEGOUUUUUUU 🏝")
            file_ = open("data/manel_cambalhota.gif", "rb")
            contents = file_.read()
            data_url = base64.b64encode(contents).decode("utf-8")
            file_.close()

            st.markdown(
                f'<img src="data:image/gif;base64,{data_url}" alt="cat gif">',
                unsafe_allow_html=True,
            )
            break
        wait_string.text(f'⏳ Falta(m) : '
                              f'{str(difference.days)}  dia(s)'
                              f'{str(count_hours)}  hora(s) '
                              f'{str(count_minutes)} minuto(s) '
                              f'{str(count_seconds)} segundo(s) '
                              f'para a reforma ⌛️')

        time.sleep(1)


end_time = datetime.datetime(2024, 12, 1, 00, 00, 00)
countdown(end_time)